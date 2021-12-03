### Privacy Policy

**This is an usage and disclamir of the `simple twitter`   module**

- The simple twitter module is highly secure 
- The depedency file in `requirements.txt` will not be installed in you computer only ```'APScheduler',
        'selenium',
        'requests',
        'tweepy',
        'webdriver-manager'
        ``` will be installed for requirements in your computer
        
- The **simpletwitter** module will not store any of you passwords in our cloud as you see in the `__init__.py` there you can confrim this _policy_

- the `simpletwitter` will not take any responciblity unless you leaked the password as you own 

- [x] In case of any leakeage of password found on the internet but it is not in your fault you can contact us on any time here : [Contact Developer](mailto:abipravi11@outlook.com)   
    
   ###### We will take the necessary action on the leakage of you twitter account details unless it is not leaked by you
   ###### You can also see the twitter login activity in you official twitter account or in the twitter app
   
   ###### By this you can know any other devices rather than your is logged in or not it logged in into the other devices which is not identified by you please report it to the developer here : [Contact Developer](mailto:abipravi11@outlook.com)
          

- We have created this module completly using chrome driver automation tool named `selenium`
  - By this you can know that the password is completly an temproary one 
  - if you are going to deploy this in any other webserver you need to give the credientials as `.env` file then it will be safe and also use you own authendication system
    since it is an module we many not take any responcibility of the password security since the password is enterd at the time of function call itself there is no storage of the password there,
    So you need to make the password secure by providing `encoding` systems to the passwords
    
  **For Example**
    ```
    You can encode you password and store it inside the db or anyother **.env** file
    later decode at the time of function call and make the bit functionable
    ```


#### Why we dont ask for API instead Password

This may seems suspecious to all of them i know that,
** Answer => **
This complete module is created using the `selenium` module it need to login into you account and then performs the operation of the normal user who do in the actual twitter

If you see the code that there is no sending os password to anyone or storing the password in any other cloud it is just simply using selinium to login and all the stuff
Just like Data Analylist do while scraping the Data

**Here is the Proff of the code **

For Full Code: [Visite File](https://github.com/pravee42/simpletwitter/blob/master/simpletwitter/__init__.py)

``` py
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
        bot.get("https://twitter.com/login")
        time.sleep(3)
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

        login_xpath = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div'))).click()

        time.sleep(5)
```
