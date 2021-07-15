
import sys
import os
import shutil
import requests
import re, unicodedata

import pandas as pd 
import runpy 
from typing import (
  final,
  NoReturn,
)

from ....gen import (
  Reader,
  Lang,
)

from tempfile import (
  mkdtemp
)

from tqdm import (
  tqdm,
)

from . import (
  JPTokenizer as JT,
)



@final
class WikiCorpusGen:

  @classmethod
  def get_url(
    cls,
    lang: Lang,
  ) -> str:
    code = lang.iso_639_1.name
    code = code.lower()
    fmt = cls.url_format()
    url = fmt.format(
      iso_639_1=code,
    )
    return url


  @staticmethod 
  def url_format() -> str:
    url = (
      'https://'
      'dumps.wikimedia.org/'
      '{iso_639_1}wiki/latest/'
      '{iso_639_1}wiki-'
      'latest-pages-articles-'
      'multistream.xml.bz2'
    )
    return url


  def generate(
    self,
    lang: str,
  ):
    self.url = self.get_url(
      lang=lang,
    )
    root = mkdtemp()
    self.dst_dump = (
      f'{root}/wiki.xml.bz2'
    )
    self.root = root 
    self.download()
    self.extract()
    self.merge()
    self.rm_doc_tag()
    self.tokenize()
    shutil.rmtree(root)


  def download(
    self,
    bufsize: int=1 << 10,
  ) -> NoReturn:
    res = requests.get(
      url=self.url,
      stream=True,
    )
    total = res.headers.get(
      'content-length',
      0,
    )
    total = int(total)
    pbar = tqdm(
      total=total,
      unit='iB',
      unit_scale=True,
    )
    with open(
      file=self.dst_dump,
      mode='wb',
    ) as f:
      for chunk in (
        res.iter_content(
          chunk_size=bufsize,
        )
      ):
        if not chunk:
          continue 
        f.write(chunk)
        pbar.update(bufsize)
    pbar.close()            
    print('download: done.')


  def extract(
    self,
  ) -> NoReturn:
    sys.argv = [
      '', 
      f'-o {self.root}/text',
      '-b 32M', 
      self.dst_dump,
    ]
    module = (
      'wikiextractor'
      '.WikiExtractor'
    )
    runpy.run_module(
      mod_name=module,
      run_name='__main__',
    )
    print('extraction: done.')
  

  def merge(
    self,
  ) -> NoReturn:
    root = self.root 
    wiki_tmp = (
      f'{root}/wiki_tmp.txt'
    )
    cmd = (
      f'find {root}/text/ | '
      'grep wiki | '
      'awk '
      '\'{system('
      '"cat "$0" >> '
      f'{wiki_tmp}"'
      ')}\''
    )
    os.system(cmd)
    self.wiki_tmp = wiki_tmp
    print('merge: done.')


  def rm_doc_tag(
    self,
  ) -> NoReturn:
    wiki_tmp = self.wiki_tmp
    root = self.root 
    wiki = f'{root}/wiki.txt'
    cmd = (
      f'cat {wiki_tmp} | ' \
      'sed \'/^<[^>]*>$/d\' '
      f'> {wiki}'
    )
    os.system(cmd)
    self.wiki = wiki
    print(
      'remove doc tag: done.'
    )
  

  def tokenize(
    self,
  ) -> NoReturn:
    wiki_corpus = (
      'wiki_corpus.txt'
    )
    reader = Reader(
      self.wiki,
    )
    tokenizer = JT()
    with reader as r:
      lines = r.lines
      df = pd.DataFrame(
        {'text': lines},
      )
      del lines
      df['text'] = df.text.map(
        tokenizer,
      )
      df.dropna(inplace=True)
      lines = df.text.values
      del df 
    with open(
      wiki_corpus,
      mode='w',
    ) as f:
      f.writelines(
        lines,
      )
    self.wiki_corpus = (
      wiki_corpus,
    )
    print('tokenize: done.')