import dataclasses
import typing 
import selenium
from \
  selenium.webdriver \
  .common.by \
import (
  By,
)



@dataclasses.dataclass
class LoginFormID():
  email: str = 'mail'
  passwd: str = 'password'
  submit: str = 'login_btn'



@dataclasses.dataclass
class Auth():
  email: str
  passwd: str



class Login():
  def __call__(
    self,
    driver: (
      selenium
      .webdriver
      .remote
      .webdriver
      .WebDriver
    ), 
  ) -> typing.NoReturn:
    auth = self.__auth
    ids = LoginFormID()
    driver.find_element(
      by=By.ID,
      value=ids.email,
    ).send_keys(auth.email)
    driver.find_element(
      by=By.ID,
      value=ids.passwd,
    ).send_keys(auth.passwd)
    driver.find_element(
      by=By.ID,
      value=ids.submit,
    ).click()


  def __init__(
    self,
    auth: Auth,
  ):
    self.__auth = auth