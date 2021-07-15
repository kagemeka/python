
import pandas as pd 


from .. import (
  Path_,
  PathManager as PM,
)

# from .. import (
#   DFFormats as DF,
# )

from ... import (
  FileFormat as FF,
)



class DFWriter:


  def __call__(
    self,
    df: pd.DataFrame,
    path: Path_,
    *args,
    **kwargs,
  ) -> pd.DataFrame:
    return self.write(
      df,
      path,
      *args,
      **kwargs,
    )
  

  @classmethod
  def write(
    cls,
    df: pd.DataFrame,
    path: Path_,
    *args,
    **kwargs,
  ) -> None:
    from .. import (
      DFFormats as DF,
    )

    f = DF.get_fmt(path)
    if f is None:
      return 
    
    f = f.name

    if f == FF.CSV:
      cls.csv(
        df,
        path,
        *args,
        **kwargs,
      )

    if f == FF.EXCEL_WORKBOOK:
      cls.excel(
        df,
        path,
        *args,
        **kwargs,
      )

    if f == FF.PICKLE:
      cls.pkl(
        df,
        path,
        *args,
        **kwargs,
      )
    
    if f == FF.DB:
      cls.db(
        df,
        path,
        *args,
        **kwargs,
      )


  @staticmethod
  def csv(
    df: pd.DataFrame,
    path: Path_,
    *args,
    index=False,
    **kwargs,
  ) -> pd.DataFrame:
    from .. import (
      DFFormats as DF,
    )
    ok = DF.assert_csv(path)
    if not ok:
      return
    PM.prepare_dir(path)
    df.to_csv(
      path,
      *args,
      **kwargs,
      index=index,
    )


  @staticmethod
  def excel(
    df: pd.DataFrame,
    path: Path_,
    *args,
    index=False,
    **kwargs,
  ) -> pd.DataFrame:
    from .. import (
      DFFormats as DF,
    )
    ok = DF.assert_excel(path)
    if not ok:
      return
    PM.prepare_dir(path)
    df.to_excel(
      path,
      *args,
      **kwargs,
      index=index,
    )
    
  

  @staticmethod
  def pkl(
    df: pd.DataFrame,
    path: Path_,
    *args,
    index=False,
    **kwargs,
  ) -> pd.DataFrame:
    from .. import (
      DFFormats as DF,
    )
    ok = DF.assert_pkl(path)
    if not ok:
      return
    PM.prepare_dir(path)
    df.to_pickle(
      path,
      *args,
      **kwargs,
      index=index,
    )


  @staticmethod
  def db(
    df: pd.DataFrame,
    path: Path_,
    *args,
    **kwargs,
  ) -> pd.DataFrame:
    from .. import (
      DFFormats as DF,
    )
    ok = DF.assert_db(path)
    if not ok:
      return
    ...

'''TODO 
excelに関しては、
途中ファイル書き込みもできるようにする。
'''