This package can be used to make your own twitter bot with less code <br />

_import the package using pip install_ <br />

`pip install simpletwitter`

PyPi Link :
[https://pypi.org/project/simpletwitter/](https://pypi.org/project/simpletwitter/)

[![Downloads](https://static.pepy.tech/personalized-badge/simpletwitter?period=month&units=abbreviation&left_color=yellowgreen&right_color=yellow&left_text=Downloads)](https://pepy.tech/project/simpletwitter)


`usage:`

```
from simpletwitter import SimpleTwitter
bot = SimpleTwitter(email, password, no_of_tweets, username)
bot.login()
bot.like_tweet(hashtags) #like the twitte
bot.unlike_liked_tweets(5) #unlike the liked tweet
bot.tweet(tweetmessage) #put some tweet
```

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
