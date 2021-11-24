from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Python package for making twitter bot with less code'
LONG_DESCRIPTION = 'this package can be used to create your own twitter bot with less code'

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
