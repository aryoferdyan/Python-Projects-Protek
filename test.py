###############################################################
## Auto Login Igracias                                       ##
## Created with Love by Yasri Ridho                          ##
###############################################################

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

class IgraciasBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://igracias.telkomuniversity.ac.id')
        time.sleep(3)
        log_button = bot.find_element_by_class_name('dropbtn')
        action = ActionChains(bot)
        action.move_to_element(log_button).perform()
        bot.find_element_by_id('login_button_general').click()
        time.sleep(2)
        username = bot.find_element_by_name('textUsername')
        password = bot.find_element_by_name('textPassword')
        username.clear()
        password.clear()
        username.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)

ed = IgraciasBot('your username', 'your password') # Jangan lupa diganti!
ed.login()