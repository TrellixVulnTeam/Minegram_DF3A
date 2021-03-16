from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from random import randrange


class BotComment:
    def __init__(self, accont_logged, url):
        self._account_logged = accont_logged
        self._url = url
        # FOR SELENIUM USAGE
        self.driver = webdriver.Chrome()
        self.user_name_location = '[name="username"]'
        self.user_password_location = '[name="password"]'
        self.comment_location = 'Ypffh'
        self.comment_buton = "//buton[contains(text(), 'publicar')]"

    def login_instagram(self):
        try:
            self.driver.get('https://www.instagram.com')
            sleep(3)
            user_login = WebDriverWait(self.driver, 10).until(
                ec.visibility_of_element_located((By.CSS_SELECTOR, self.user_name_location)))
            user_login.clear()
            user_login.send_keys(self._account_logged._user)
            sleep(3)
            user_password = WebDriverWait(self.driver, 10).until(
                ec.visibility_of_element_located((By.CSS_SELECTOR, self.user_password_location)))
            user_password.clear()
            user_password.send_keys(self._account_logged._password)
            user_password.send_keys(Keys.RETURN)
            sleep(5)
            return True
        except():
            return False

    def acess_url(self):
        try:
            self.driver.get(self._url)
            sleep(3)
            return True
        except():
            return False

    def comment(self, commentary):
        try:
            self.driver.find_element_by_class_name(self.comment_location).click()
            sleep(randrange(1, 3))
            self.driver.find_element_by_class_name(self.comment_location).send_keys(commentary)
            sleep(randrange(1, 3))
            self.driver.find_element_by_xpath(self.comment_buton).click()
            sleep(3)
            return True
        except():
            return False
