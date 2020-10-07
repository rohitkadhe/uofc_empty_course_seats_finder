from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

SCHEDULE_BUILDER_URL = 'https://vsb.my.ucalgary.ca/criteria.jsp'
THIRTY_SECONDS = 30
DRIVER = webdriver.Chrome()
WAIT = WebDriverWait(DRIVER, THIRTY_SECONDS)
