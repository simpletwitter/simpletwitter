from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time


class SimpleTwitter:
    def __init__(self, email, password, no_of_tweets, user_name):
        self.email = email
        self.password = password
        self.no_of_tweets = no_of_tweets
        self.user_name = user_name
        self.s = Service(ChromeDriverManager().install())
        self.bot = webdriver.Chrome(service=self.s)
        self.wait = WebDriverWait(self.bot, 20)

    def login(self):
        bot = self.bot
        bot.get("https://twitter.com/i/flow/login")
        try:
            email_input = self.wait.until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="layers"]/div/.../input'))
            ).send_keys(self.email)
            next_button = self.wait.until(
                EC.presence_of_element_located((By.XPATH, '// *[@id="layers"]/div/.../div[6]'))
            ).click()

            password_input = self.wait.until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="layers"]/div/.../input'))
            ).send_keys(self.password)
            next_button = self.wait.until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="layers"]/div/.../div[2]/div'))
            ).click()
        except:
            print("Login failed")
        time.sleep(5)

    def retweet(self, hashtag):
        for x in hashtag:
            search_button = self.wait.until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/.../input'))
            ).send_keys(x)
            search_button.send_keys(Keys.ENTER)
            time.sleep(1)

            for i in range(self.no_of_tweets):
                try:
                    retweet = self.wait.until(
                        EC.presence_of_element_located((By.XPATH, "//div[@data-testid='retweet']"))
                    ).click()
                    retweet_confirm = self.wait.until(
                        EC.presence_of_element_located((By.XPATH, "//div[@data-testid='retweetConfirm']"))
                    ).click()
                    print(f"Retweeted {i + 1} tweet under {x}")
                    time.sleep(1)
                except Exception as e:
                    print(f"Failed to retweet tweet {i + 1} under {x}: {e}")
                    self.bot.execute_script("window.scrollTo(0, document.body.scrollHeight/1.5);")
                    time.sleep(1)
