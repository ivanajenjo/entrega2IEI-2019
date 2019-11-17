from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


def whaitforpageload(wdriver):
    wait = WebDriverWait(wdriver, 60)
    pageLoaded = Predicate<WebDriver>()