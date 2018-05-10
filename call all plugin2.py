# -*- coding: utf-8 -*-
"""
Created on Wed May  9 16:48:48 2018

@author: J_C___
"""

import praw
import io
import os
import re
import time
import configparser
config = configparser.ConfigParser()
config.read('auth.ini')

reddit = praw.Reddit(client_id=config.get('auth', 'reddit_client_id'),
                     client_secret=config.get('auth', 'reddit_client_secret'),
                     password=config.get('auth', 'reddit_password'),
                     user_agent=config.get('auth', 'reddit_user_agent'),
                     username=config.get('auth', 'reddit_username'))

print("Posting as: ", reddit.user.me())
SUBREDDIT = "StarVStheForcesofEvil"
LIMIT = 1000


if not os.path.isfile("call_all_posts.txt"):
    call_all_posts = []
else:
    with open("call_all_posts.txt", "r") as f:
       call_all_posts = f.read()
       call_all_posts = call_all_posts.split("\n")
       call_all_posts = list(filter(None, call_all_posts))
comment = []
def scan_submissions(call_all_posts):
    global usernames
    subreddit = reddit.subreddit(SUBREDDIT)
    for submission in subreddit.new(limit=25):
        if 'u/' in submission.selftext and submission.id not in call_all_posts:
            print('Submission has a user!')
            usernames = []
            username = re.findall("u\/[A-Za-z0-9_-]{3,20}", submission.selftext)
            while len(username) > 3:
                print(username[:3])
                username.pop()
                username.pop()
                username.pop()
#                Shes not ready to make actual replys yet
#                my_reply = submission.reply(username.pop() +" "+ username.pop() + " " + username.pop())
#                print('\tSent!')
            while len(username) > 0:
                print("\t", username[:len(username)])
#                reddit.comment(id=my_reply).reply(username[:len(username)])
                while len(username) > 0:
                    username.pop()
                

                    
#            call_all_posts.append(submission.id)
            
def update_files(call_all_posts):
    with open("call_all_posts.txt", "w") as f:
        for x in call_all_posts:
            f.write(x + "\n")

try:
    while True:
        scan_submissions(call_all_posts)
        print('No posts match... sleeping for 60s')
        #Makes it easier to interupt script fast
        time.sleep(5)
        time.sleep(5)
        time.sleep(5)
        time.sleep(5)
        time.sleep(5)
        time.sleep(5)
        time.sleep(5)
        time.sleep(5)
        time.sleep(5)
        time.sleep(5)
        time.sleep(5)
        time.sleep(5)
        time.sleep(5)
        time.sleep(5)
        time.sleep(5)
        time.sleep(5)
        time.sleep(5)
        time.sleep(5)
        time.sleep(5)
        time.sleep(5)
except KeyboardInterrupt:
    update_files(call_all_posts)
    print('Interrupted')