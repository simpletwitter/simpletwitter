import requests
import re
from bs4 import BeautifulSoup
import json
from lxml import etree
import string
from datetime import datetime, timedelta
import html2text


def summarize(content):

    API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
    headers = {"Authorization": f"Bearer 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"}

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()
        
    output = query({
        "inputs": content + "Convert this into an Amazing Tweet with some Hashtags",
    })   

    return output[0]['summary_text']


def LinkedInTwitter(posturl):

    page = requests.get(posturl)
    soup = BeautifulSoup(page.content, "html.parser")
    m1 = None
    l = soup.select(".main-feed-activity-card-with-comments > div:nth-child(3) > p:nth-child(1)")
    if len(l) > 0:
        m = BeautifulSoup(str(l[0]), "html.parser")
        m1 = summarize(m.get_text())
    else:
        l = soup.select("div.share-update-card:nth-child(1) > p:nth-child(3)")
        m = BeautifulSoup(str(l[0]), "html.parser")
        m1 = summarize(m.get_text())
    return m1 


