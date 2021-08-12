import subprocess



class Neologd():
  @staticmethod
  def check_root() -> str:
    cmd = (
      'echo '
      '`mecab-config --dicdir`'
    )
    stdout = subprocess.Popen(
      cmd,
      shell=True,
      stdout=subprocess.PIPE,
    ).stdout
    rt = stdout.read().rstrip()
    return rt.decode()
  

  @classmethod
  def find_path(cls) -> str:
    return (
      f'{cls.check_root()}/'
      'mecab-ipadic-neologd'
    )