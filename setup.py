from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Python package for making twitter bot with less code'
LONG_DESCRIPTION = '''
This package can be used to make your own twitter bot with less code

import the package using pip install

usage:

    bot = Twitterbot(email, password, no_of_tweets, username)
    bot.login()
    bot.like_tweet(hashtags) #like the twitte
    bot.Unlike_liked_tweets(5) #unlike the liked tweet

This bot module was created by Abipravi
any one who want to ugrate and add more feature to the module can create an issue in github repository and make your PR's
'''

setup(
    name="twitterbot_abipravi",
    version=VERSION,
    author="Abipravi",
    author_email="darkparadise877@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    keywords=['python', 'first package', 'twitter', 'twitterbot_abipravi', 'make you own bot'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
     project_urls={
        'Homepage': 'https://github.com/pravee42/Twitter_bot_module',
    },
    install_requires=[
        'APScheduler',
	'selenium',
	'requests',
	'tweepy',
	'webdriver-manager',
    ]

)
