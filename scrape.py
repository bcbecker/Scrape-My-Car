# This program is a nice little web scraper being used in hopes of tracking down your dream car
# NOTE: using user agents is not the most effective, try a parser that detects user agent (Like MobileDetect in PHP)

import requests
from bs4 import BeautifulSoup
import smtplib
import time
from config import Config


#Sentinel
run = True

#target URL/tags for platforms, define yours here
BAT_URL = 'https://bringatrailer.com/auctions/'
BAT_TAG = "a"
BAT_TAG_CLASS = {"class": "auctions-item-image-link"}



def check_target(URL, tag, tag_class):

    target_webpage = requests.get(URL)
    target_webpage_content = target_webpage.content
    soup = BeautifulSoup(target_webpage_content, 'html.parser')

    #found via web inspector
    target = soup.find_all(tag, tag_class)
    lst = []
    years = ['1995', '1996', '1997', '1998']
    search_term = 'carrera'

    for link in target:
        temp = link.get('href')
        if search_term in temp and any(year in temp for year in years):
            print(temp)
            lst.append(temp)
    if lst:
        send_email(lst)



def send_email(list):
    #set up server connection, encypt, login, set/send email, disconnect
    server = smtplib.SMTP(Config.MAIL_SERVER, Config.MAIL_PORT)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(Config.MAIL_USERNAME, Config.MAIL_PASSWORD)

    email_subject = "We've Scraped Something!"
    email_body = "There have been new listings of your dream car. Check it out and see what's new.\n\n" + str(*list)
    email_Full = 'Subject: {}\n\n{}'.format(email_subject, email_body)

    server.sendmail(Config.MAIL_USERNAME, Config.MAIL_TO_USER, email_Full)
    print("\n\nEmail Sent.\n\n")

    server.quit()




#executes in infinite loop (bad coding conv), checking price every 24h (86400 seconds), then sleeping and repeating
while(run):
    check_target(BAT_URL, BAT_TAG, BAT_TAG_CLASS)
    print("\nSleeping...\n")
    time.sleep(86400)
