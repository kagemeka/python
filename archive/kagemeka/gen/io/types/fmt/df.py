from dataclasses import (
  dataclass,
)

from . import (
  BaseFormats,
  BaseFormat,
)

from .... import (
  FileFormat as FF,
)

from .. import (
  Path_,
)



@dataclass 
class DFFormat(
  BaseFormat,
):
  ...


@dataclass 
class DFFormats(
  BaseFormats,
):
  csv: DFFormat = DFFormat(
    name=FF.CSV,
  )

  xlsx: DFFormat = DFFormat(
    name=FF.XLSX,
  )

  pkl: DFFormat = DFFormat(
    name=FF.PICKLE,
  )

  sql: DFFormat = DFFormat(
    name=FF.SQL,
  )

  db: DFFormat = DFFormat(
    name=FF.DB,
  )

  @classmethod 
  def get_fmt(
    cls,
    path: Path_,
  ) -> DFFormat:
    fmt = super().get_fmt(path)
    return fmt


  @classmethod
  def assert_csv(
    cls,
    path: Path_,
  ) -> bool:
    f = cls.get_fmt(path)
    ok = (
      f.name == FF.CSV
    )
    return ok

    
  @classmethod
  def assert_excel(
    cls,
    path: Path_,
  ) -> bool:
    f = cls.get_fmt(path)
    ok = (
      f.name 
      == FF.EXCEL_WORKBOOK
    )
    return ok
    

  @classmethod
  def assert_pkl(
    cls,
    path: Path_,
  ) -> bool:
    f = cls.get_fmt(path)
    ok = (
      f.name == FF.PICKLE
    )
    return ok


  @classmethod
  def assert_db(
    cls,
    path: Path_,
  ) -> bool:
    f = cls.get_fmt(path)
    ok = (
      f.name == FF.DB
    )
    return ok