This package can be used to make your own twitter bot with less code <br />

_import the package using pip install_ <br />

`pip install simpletwitter`

PyPi Link :
[https://pypi.org/project/simpletwitter/](https://pypi.org/project/simpletwitter/)

Google Groups Link: 
[https://groups.google.com/g/simpletwitter](https://groups.google.com/g/simpletwitter)

[![Downloads](https://static.pepy.tech/personalized-badge/simpletwitter?period=total&units=international_system&left_color=black&right_color=brightgreen&left_text=Users%20Total)](https://pepy.tech/project/simpletwitter)
[![Downloads](https://static.pepy.tech/personalized-badge/simpletwitter?period=month&units=international_system&left_color=black&right_color=brightgreen&left_text=Users%20This%20Month)](https://pepy.tech/project/simpletwitter)
[![Downloads](https://static.pepy.tech/personalized-badge/simpletwitter?period=week&units=international_system&left_color=black&right_color=brightgreen&left_text=Users%20This%20Week)](https://pepy.tech/project/simpletwitter)
[![Downloads](https://static.pepy.tech/personalized-badge/simpletwitter?period=total&units=none&left_color=black&right_color=brightgreen&left_text=User%20in%20Numbers)](https://pepy.tech/project/simpletwitter)

`usage:`

```
from simpletwitter import SimpleTwitter
bot = SimpleTwitter(email, password, no_of_tweets, username)
bot.login()
bot.like_tweet(hashtags) #like the twitte
bot.unlike_liked_tweets(5) #unlike the liked tweet
bot.tweet(tweetmessage) #put some tweet
```

### Users Currently Using as of (01-11-2022):

| **Total Downloads** | **Monthly Downloads** | **Weekly Downloads** |
| ------------------- | --------------------- | -------------------- |
| 11,233              | 884                   | 175                  |

### Current Version 1.2.6

### Users Graph

![image](https://github.com/pravee42/simpletwitter/assets/65100038/08ac5b6c-5137-482e-8824-ff712a177379)

#### Packages used

| **Tool Name** | **Purpose**       |
| ------------- | ----------------- |
| Selenium      | Chrome Automation |

| Feature Update | 3 feature update added on 15th May 2022                               |
| -------------- | ------------------------------------------------------------------ |
| Update 1       | `Added function to retweet`                                        |
| Update 2       | `Added feature to like the top tweets of the particular hash tags` |
| Update 3       | `Added Tech News feature to post news on twitter account` |

#### Code Usage of Updates

---

##### Update 1

```
from simpletwitter import SimpleTwitter
bot = SimpleTwitter(email, password, no_of_tweets, username)
bot.login()
hashtags = ["#reactjs", "abipravi"]
bot.only_like_top_tweet(hashtags)
```

##### Update 2

```
from simpletwitter import SimpleTwitter
bot = SimpleTwitter(email, password, no_of_tweets, username)
bot.login()
hashtags = ["#reactjs", "abipravi"]
bot.retweet(hashtags)
```

##### Update 3

Post Tech News from [NEWSAPI](https://newsapi-abipravi.herokuapp.com/tech)

```
from simpletwitter import SimpleTwitter
bot = SimpleTwitter(email, password, no_of_tweets, username)
bot.login()
no_of_news_to_be_posted = 1
# if no of tweets to be posted ==> 1 {Post 12 news} it will post '12' news for value =>> 1 <<=
x = bot.post_tech_news(no_of_news_to_be_posted)
```

#### Features

- [ ] Scrape Data for analytics
- [x] Tech News post in twitter
- [ ] Twitter APi also using Twitter API keys
