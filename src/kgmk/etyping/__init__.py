from __future__ import (
  annotations,
)
from \
  selenium.webdriver \
  .common.by \
import (
  By,
)
from \
  selenium.webdriver \
  .common.keys \
import (
  Keys,
)

import typing
import dataclasses
from .category import (
  Category,
)
from .login import (
  Login,
  Auth,
)
from .register import (
  Register,
)
from .play import (
  Play,
  PlayCfg,
)

import time
from \
  selenium.webdriver.remote \
  .webdriver \
import (
  WebDriver,
)



@dataclasses.dataclass
class ETypingCfg():
  auth: Auth
  play: PlayCfg = PlayCfg()
  category: Category = (
    Category.ROMA
  )


class ETyping():
  def __call__(
    self,
    driver: WebDriver,
  ) -> typing.NoReturn:
    self.__driver = driver
    self.__open_website()
    self.__login()
    self.__open_page()
    self.__start_up_game()
    self.__start_game()
    self.__play()
    self.__register()
      

  def __init__(
    self,
    cfg: ETypingCfg,
  ) -> typing.NoReturn:
    self.__cfg = cfg
    self.__base_url = (
      'https://'
      'www.e-typing.ne.jp'
    )

  
  def __login(
    self,
  ) -> typing.NoReturn:
    fn = Login(self.__cfg.auth)
    fn(self.__driver)


  def __play(
    self,
  ) -> typing.NoReturn:
    fn = Play(self.__cfg.play)
    fn(self.__game)

  
  def __register(
    self,
  ) -> typing.NoReturn:
    Register()(self.__game)
  

  def __open_website(
    self,
  ) -> typing.NoReturn:
    self.__driver.get(
      self.__base_url,
    )


  def __open_page(
    self,
  ) -> typing.NoReturn: 
    cfg = self.__cfg
    self.__driver.get(
      f'{self.__base_url}/'
      'member/cht.asp?tp='
      f'{cfg.category.value}',
    )


  def __start_up_game(
    self,
  ) -> typing.NoReturn:
    driver = self.__driver
    id_ = 'level_check_member'
    driver.find_element(
      by=By.ID,
      value=id_,
    ).find_element(
      by=By.TAG_NAME,
      value='a',
    ).click()
    time.sleep(1)


  def __start_game(
    self,
  ) -> typing.NoReturn:
    driver = self.__driver
    driver.switch_to.frame(
      'typing_content',
    )
    driver.find_element(
      by=By.ID,
      value='start_btn',
    ).click()
    time.sleep(1 << 1)
    game = driver.find_element(
      by=By.TAG_NAME,
      value='body',
    )
    game.send_keys(Keys.SPACE)
    time.sleep(1 << 2)
    self.__game = game