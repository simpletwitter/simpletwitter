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
