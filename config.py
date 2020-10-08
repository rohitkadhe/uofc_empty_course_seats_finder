from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import sys

SCHEDULE_BUILDER_URL = 'https://vsb.my.ucalgary.ca/criteria.jsp'
THIRTY_SECONDS = 30
if sys.platform == "win32":
    DRIVER = webdriver.Chrome()
else:
    DRIVER = webdriver.Chrome("./chromedriver")
WAIT = WebDriverWait(DRIVER, THIRTY_SECONDS)
