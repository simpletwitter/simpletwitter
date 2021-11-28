This package can be used to make your own twitter bot with less code <br />

_import the package using pip install_ <br />

`usage:`

```
from simpletwitter import SimpleTwitter
bot = SimpleTwitter(email, password, no_of_tweets, username)
bot.login()
bot.like_tweet(hashtags) #like the twitte
bot.unlike_liked_tweets(5) #unlike the liked tweet
bot.tweet(tweetmessage) #put some tweet
```
