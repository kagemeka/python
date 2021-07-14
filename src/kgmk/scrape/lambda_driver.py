from selenium.webdriver import(
  Chrome,
  ChromeOptions,
)
from \
  selenium.webdriver.remote \
  .webdriver \
import (
  WebDriver,
)



class CreateLambdaDriver():
  def __call__(
    self,
    headless_chromium: str=(
      '/opt/headless-chromium'
    ),
    chromedriver: str=(
      '/opt/chromedriver'
    ),
  ) -> WebDriver:
    opt = ChromeOptions()
    opts = [
      '--no-sandbox',
      '--single-process',
      '--disable-dev-shm-usage',
      '--homedir=/tmp',
    ]
    opt.headless = True
    for o in opts:
      opt.add_argument(o)
    opt.binary_location = (
      headless_chromium
    )
    driver = Chrome(
      chromedriver,
      options=opt,
    )
    return driver