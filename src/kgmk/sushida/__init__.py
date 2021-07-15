from __future__ import (
  annotations,
)
import time
import dataclasses
import pyautogui
from PIL import (
  Image,
  ImageOps,
)
import typing
from selenium.webdriver import(
  ActionChains,
)
from \
  selenium.webdriver \
  .common.by \
import (
  By,
)
from \
  selenium.webdriver.remote \
  .webdriver \
import (
  WebDriver,
)



@dataclasses.dataclass
class SushidaCfg():
  repetitions: int = 1 << 7
  interval: float = 0.2 
  result_path: typing.Optional[
    str
  ] = None



class Sushida():
  def __call__(
    self,
    driver: WebDriver,
  ) -> typing.NoReturn:
    self.__driver = driver
    self.__open_game()
    self.__start_game()
    self.__play()
    self.__save_result()
    cfg = self.__cfg


  def __init__(
    self,
    cfg: SushidaCfg,
  ) -> typing.NoReturn:
    self.__cfg = cfg


  def __open_game(
    self,
  ) -> typing.NoReturn:
    driver = self.__driver
    driver.get(
      'http://typingx0.net'
      '/sushida/',
    )
    time.sleep(1)
    driver.find_element(
      by=By.CLASS_NAME,
      value='main_play',
    ).find_elements(
      by=By.TAG_NAME,
      value='a',
    )[0].click()
    time.sleep(6)
    game = driver.find_element(
      by=By.ID,
      value='#canvas',
    )
    self.__game = game

  
  def __save_result(
    self,
  ) -> typing.NoReturn:
    cfg = self.__cfg 
    p = cfg.result_path
    if p is None: return
    from kgmk.path import (
      PrepareDir,
    )
    PrepareDir()(p)
    self.__game.screenshot(p)


  def __start_game(
    self,
  ) -> typing.NoReturn:
    ActionChains(
      self.__driver,
    ).move_to_element_with_offset(
      self.__game,
      250,
      250,
    ).click().release().perform()
    time.sleep(1)
    ActionChains(
      self.__driver,
    ).move_to_element_with_offset(
      self.__game,
      250,
      320,
    ).click().release().perform()
    time.sleep(1)
    pyautogui.press('space')
    time.sleep(3)


  def __play(
    self,
  ) -> typing.NoReturn:
    cfg = self.__cfg
    n = cfg.repetitions
    t = cfg.interval
    for i in range(n):
      self.__eat()
      time.sleep(t) 
    time.sleep(
      120 + n * (0.7 - t)
    )


  def __screenshot(
    self,
  ) -> typing.NoReturn:
    from base64 import (
      b64decode,
    )
    from io import BytesIO
    bytes_img = b64decode(
      self.__game
      .screenshot_as_base64,
    )
    self.__img = Image.open(
      BytesIO(bytes_img),
    )

  
  def __process_img(
    self,
  ) -> typing.NoReturn:
    img = self.__img
    w, _ = img.size
    pad = 76   
    img = img.crop((
      pad, 228, w - pad, 256,
    ))
    img = ImageOps.grayscale(img)
    img = img.convert('L')
    img = img.point(
      lut=lambda x: (
        (1 << 8) - 1 
        if x >= 1 << 7 else 0
      ),
    )
    img = ImageOps.invert(img)
    self.__img = img
  

  def __ocr(
    self,
  ) -> typing.NoReturn:
    import string
    from pytesseract import (
      image_to_string,
    )
    tol = (
      string.ascii_lowercase
      + string.digits
      + '!?-,'
    )
    txt = image_to_string(
      self.__img,
      config=f'-c tessedit_char_whitelist={tol}',
    ).strip()
    self.__txt = txt 
    print(self.__txt)
    

  def __eat(
    self,
  ) -> typing.NoReturn:
    self.__screenshot()
    self.__process_img()
    self.__ocr()
    pyautogui.write(self.__txt)
