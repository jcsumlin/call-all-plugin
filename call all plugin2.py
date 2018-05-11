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
config.read('auth.ini') #All my usernames and passwords for the api
#the config file is
reddit = praw.Reddit(client_id=config.get('auth', 'reddit_client_id'),
                     client_secret=config.get('auth', 'reddit_client_secret'),
                     password=config.get('auth', 'reddit_password'),
                     user_agent=config.get('auth', 'reddit_user_agent'),
                     username=config.get('auth', 'reddit_username'))
bot_message = "\r\r^(I am a script. If I did something wrong, ) [^(let me know)](/message/compose/?to=J_C___&subject=all_seeing_eye_bot)"
print("Posting as: ", reddit.user.me())
SUBREDDIT = 'starvstheforcesofevil' #config.get('auth', 'reddit_subreddit')
LIMIT = 1000 #config.get('auth', 'reddit_limit')

#If the call_all_posts text file dosn't exist, create it and initilize the enpty list.
if not os.path.isfile("call_all_posts.txt"):
    call_all_posts = []
#If the file does exist import the contents into a list
else:
    with open("call_all_posts.txt", "r") as f:
       call_all_posts = f.read()
       call_all_posts = call_all_posts.split("\n")
       call_all_posts = list(filter(None, call_all_posts))
comment = []
def scan_submissions(call_all_posts):
    global usernames
    global message
    global new_list
    subreddit = reddit.subreddit(SUBREDDIT)
    #for each submission that is new (up to x (limit=x) posts)
    for submission in subreddit.new(limit=25):
        # if the user prefix is in the submission body and isn't a post I've seen before (prevents infinate looping)
        if 'u/' in submission.selftext and submission.id not in call_all_posts:
            print('Submission has a user!')
            usernames = re.findall('u\/[A-Za-z0-9_-]{3,20}', submission.selftext)  # RegEx that pulls the username from the body
            if len(usernames) >= 3:
                new_list = []
                reply = None
                i = 0
                while i < len(usernames):
                    new_list.append(usernames[i:i + 3])
                    i += 3
                for group in new_list:
                    message = ''
                    for user in group:
                        message = message + str(user) + " "
                    if reply == None:
                        print(message)
                        reply = submission.reply(message + bot_message)
                    elif reply != None:
                        print(message)
                        next_reply = reddit.comment(id=reply).reply(message + bot_message)
            elif len(usernames) <= 2 and len(usernames) > 0:
                message = ''
                for user in usernames:
                    message = message + str(user) + " "
                print(message)
                submission.reply(message + bot_message)




#            call_all_posts.append(submission.id)

def update_files(call_all_posts):
    #writes the post IDs to the file call_all_posts.txt
    with open("call_all_posts.txt", "w") as f:
        for x in call_all_posts:
            f.write(x + "\n")
#START
try:
    while True: #indeffinate looping
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
    print('Interrupted, files updated')
