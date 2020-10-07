from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

SCHEDULE_BUILDER_URL = 'https://vsb.my.ucalgary.ca/criteria.jsp'
TEST = "https://www.google.com/"
HTML_PARSER = 'html.parser'
TWO_MINS = 120
DRIVER = webdriver.Chrome()
WAIT = WebDriverWait(DRIVER, TWO_MINS)
