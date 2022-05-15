This package can be used to make your own twitter bot with less code <br />

_import the package using pip install_ <br />

`pip install simpletwitter`

PyPi Link :
[https://pypi.org/project/simpletwitter/](https://pypi.org/project/simpletwitter/)

[![Downloads](https://static.pepy.tech/personalized-badge/simpletwitter?period=total&units=abbreviation&left_color=yellowgreen&right_color=yellow&left_text=Total%20Users)](https://pepy.tech/project/simpletwitter)

`usage:`

```
from simpletwitter import SimpleTwitter
bot = SimpleTwitter(email, password, no_of_tweets, username)
bot.login()
bot.like_tweet(hashtags) #like the twitte
bot.unlike_liked_tweets(5) #unlike the liked tweet
bot.tweet(tweetmessage) #put some tweet
```

### Users Currently Using:

| **Total Downloads** | **Monthly Downloads** | **Weekly Downloads** |
| ------------------- | --------------------- | -------------------- |
| 7,065               | 785                   | 166                  |

### Users Graph

![image](https://user-images.githubusercontent.com/65100038/162125199-bf98ad10-0c00-476b-b98d-b13fbff5d48a.png)

#### Packages used

| **Tool Name** | **Purpose**       |
| ------------- | ----------------- |
| Selenium      | Chrome Automation |

| Feature Update | 2 feature update added on 28/11/2021                               |
| -------------- | ------------------------------------------------------------------ |
| Update 1       | `Added function to retweet`                                        |
| Update 2       | `Added feature to like the top tweets of the particular hash tags` |

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
