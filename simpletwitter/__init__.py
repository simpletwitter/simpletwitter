from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time


class Twitterbot:
    def __init__(self, email, password, no_of_tweets, user_name):
        self.email = email
        self.password = password
        self.no_of_tweets = no_of_tweets
        self.user_name = user_name
        self.s = ChromeDriverManager().install()
        self.bot = webdriver.Chrome(self.s)
        self.wait = WebDriverWait(self.bot, 20)

    def login(self):
        bot = self.bot
        bot.get("https://twitter.com/i/flow/login")
        time.sleep(3)
        try:
            email_xpath = self.wait.until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input'))).send_keys(self.email)
            next_button = self.wait.until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[6]/div'))).click()
        except:
            email_xpath = self.wait.until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id = "layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input'))).send_keys(self.email)
            next_button = self.wait.until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div'))).send_keys(Keys.ENTER)
        try:
            print("email Entring")
            enter_email = self.wait.until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input'))).send_keys(self.user_name)
            next_click = self.wait.until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div'))).send_keys(Keys.ENTER)
        except:
            pass
        password_xpath = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div/input'))).send_keys(self.password)
        try:
            login_xpath = self.wait.until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id = "layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div'))).click()
        except:
            login_xpath = self.wait.until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div'))).click()
        time.sleep(5)

    def like_tweet(self, hashtag):
        for x in hashtag:
            tweet_button_XPATH = self.wait.until(EC.presence_of_element_located((
                By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[2]'))).click()
            search_button_XPATH = self.wait.until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/label/div[2]/div/input'))).send_keys(x)
            search_button_Click_XPATH = self.wait.until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/label/div[2]/div/input'))).send_keys(Keys.ENTER)
            time.sleep(1)
            go_to_photos_XPATH = self.wait.until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[2]/nav/div/div[2]/div/div[4]/a'))).click()
            time.sleep(5)
            print("sleeping")
            for i in range(self.no_of_tweets):
                print(i)
                try:
                    like = self.wait.until(EC.presence_of_element_located(
                        (By.XPATH, "//div[@data-testid='like']"))).click()
                    print('liked_image')
                    time.sleep(1)
                except:
                    time.sleep(1)
                    print('liked_image_failed_except')
                    self.bot.execute_script(
                        "window.scrollTo(0, document.body.scrollHeight/1.5);")
                    time.sleep(1)
        time.sleep(1)
        print("Next hashtag")

    def only_like_top_tweet(self, hashtag):
        for x in hashtag:
            tweet_button_XPATH = self.wait.until(EC.presence_of_element_located((
                By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[2]'))).click()
            search_button_XPATH = self.wait.until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/label/div[2]/div/input'))).send_keys(x)
            search_button_Click_XPATH = self.wait.until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/label/div[2]/div/input'))).send_keys(Keys.ENTER)
            time.sleep(5)
            print("sleeping")
            for i in range(self.no_of_tweets):
                print(i)
                try:
                    like = self.wait.until(EC.presence_of_element_located(
                        (By.XPATH, "//div[@data-testid='like']"))).click()
                    print('liked_image')
                    time.sleep(1)
                except:
                    time.sleep(1)
                    print('liked_image_failed_except')
                    self.bot.execute_script(
                        "window.scrollTo(0, document.body.scrollHeight/1.5);")
                    time.sleep(1)
        time.sleep(1)
        print("Next hashtag")

    def tweet(self, tweet_body):
        tweet_button_XPATH = self.wait.until(EC.presence_of_element_located((
            By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div/span/div/div/span/span'))).click()
        print("Tweet Button Clicked", tweet_body)
        message_XPATH = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div/div/div/div'))).send_keys(tweet_body)
        send_tweet_XPATH = self.wait.until(EC.presence_of_element_located((
            By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]'))).click()

    def Unlike_liked_tweets(self, length):
        goto_profile_XPATH = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[5]'))).click()
        goto_liked_tweets_XPATH = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/nav/div/div[2]/div/div[4]/a'))).click()
        for i in range(length):
            try:
                unlike = self.wait.until(EC.presence_of_element_located(
                    (By.XPATH, "//div[@data-testid='unlike']"))).click()
                print('unliked_image')
                time.sleep(1)
            except:
                time.sleep(1)
                print('unliked_image_failed_except')
                self.bot.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight/1.5);")
                time.sleep(1)
        time.sleep(1)
        print("Next hashtag")

    def retweet(self, hashtag):
        for x in hashtag:
            tweet_button_XPATH = self.wait.until(EC.presence_of_element_located((
                By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[2]'))).click()
            search_button_XPATH = self.wait.until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/label/div[2]/div/input'))).send_keys(x)
            search_button_Click_XPATH = self.wait.until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/label/div[2]/div/input'))).send_keys(Keys.ENTER)
            time.sleep(1)
            go_to_latest_XPATH = self.wait.until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[2]/nav/div/div[2]/div/div[2]/a'))).click()
            time.sleep(5)
            print("sleeping")
            for i in range(self.no_of_tweets):
                print(i)
                try:
                    retweet = self.wait.until(EC.presence_of_element_located(
                        (By.XPATH, "//div[@data-testid='retweet']"))).click()
                    retweet_click = self.wait.until(EC.presence_of_element_located(
                        (By.XPATH, "//div[@data-testid='retweetConfirm']"))).click()
                    print('retweet')
                    time.sleep(1)
                except:
                    time.sleep(1)
                    print('retweet_tweet_failed_except')
                    self.bot.execute_script(
                        "window.scrollTo(0, document.body.scrollHeight/1.5);")
                    time.sleep(1)
        time.sleep(1)
        print("Next hashtag")
