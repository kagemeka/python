from selenium.webdriver import(
  Chrome,
  Firefox,
  ChromeOptions,
)


# TODO chrome
from webdriver_manager.chrome \
import (
  ChromeDriverManager,
)

options = ChromeOptions()
opts = [
  '--no-sandbox',
  # '--headless',
  # '--disable-dev-shm-usage',
]

for x in opts:
  options.add_argument(x)


manager = ChromeDriverManager()

driver = Chrome(
  manager.install(),
  options=options,
)
driver.get(
  'https://twitter.com'
)
driver.close()




# TODO firefox 
driver = Firefox()
driver.get(
  'https://twitter.com'
)
driver.close()