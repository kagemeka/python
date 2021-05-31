
import pandas as pd 


from .. import (
  Path_,
  PathManager as PM,
)


from ... import (
  FileFormat as FF,
)



class DFReader:

  
  def __call__(
    self,
    path: Path_,
    *args,
    **kwargs,
  ) -> pd.DataFrame:
    return self.read(
      path,
      *args,
      **kwargs,
    )
  

  @classmethod
  def read(
    cls,
    path: Path_,
    *args,
    **kwargs,
  ) -> pd.DataFrame:
    from .. import (
      DFFormats as DF,
    )

    f = DF.get_fmt(path)
    if f is None:
      return 
    
    f = f.name

    if f == FF.CSV:
      df = cls.csv(
        path,
        *args,
        **kwargs,
      )
      return df 

    if f == FF.EXCEL_WORKBOOK:
      df = cls.excel(
        path,
        *args,
        **kwargs,
      )
      return df

    if f == FF.PICKLE:
      df = cls.pkl(
        path,
        *args,
        **kwargs,
      )
      return df
    
    if f == FF.DB:
      df = cls.db(
        path,
        *args,
        **kwargs,
      )
      return df


  @staticmethod
  def csv(
    path: Path_,
    *args,
    **kwargs,
  ) -> pd.DataFrame:
    from .. import (
      DFFormats as DF,
    )
    ok = DF.assert_csv(path)
    if not ok:
      return
    df = pd.read_csv(
      path,
      *args,
      **kwargs,
    )
    return df 


  @classmethod
  def excel(
    cls,
    path: Path_,
    *args,
    **kwargs,
  ) -> pd.DataFrame:
    from .. import (
      DFFormats as DF,
    )
    ok = DF.assert_excel(path)
    if not ok:
      return
    df = pd.read_excel(
      path,
      *args,
      **kwargs,
    )
    df = cls.remove_unnamed(df)
    return df
  

  @staticmethod
  def pkl(
    path: Path_,
    *args,
    **kwargs,
  ) -> pd.DataFrame:
    from .. import (
      DFFormats as DF,
    )
    ok = DF.assert_pkl(path)
    if not ok:
      return
    df = pd.read_pickle(
      path,
      *args,
      **kwargs,
    )
    return df 


  @staticmethod
  def db(
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


  @staticmethod
  def remove_unnamed(
    df: pd.DataFrame,
  ) -> pd.DataFrame:
    ok = ~(
      df
      .columns
      .str
      .contains('^Unnamed')
    )
    df = df.loc[
      :, 
      ok,
    ]
    return df