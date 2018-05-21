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
config.read('auth.ini')  # All my usernames and passwords for the api

reddit = praw.Reddit(client_id=config.get('auth', 'reddit_client_id'),
                     client_secret=config.get('auth', 'reddit_client_secret'),
                     password=config.get('auth', 'reddit_password'),
                     user_agent='All-Seeing Eye bot (by u/J_C___)',
                     username=config.get('auth', 'reddit_username'))
print("Posting as: ", reddit.user.me())
SUBREDDIT = config.get('auth', 'reddit_subreddit')
LIMIT = int(config.get('auth', 'reddit_limit'))

'''
Static variables for bot.
'''
bot_message = "\r\r^(I am a script. If I did something wrong, ) [^(let me know)](/message/compose/?to=J_C___&subject=all_seeing_eye_bot)"

if not os.path.isfile("call_all_posts.txt"):
    call_all_posts = []
else:
    with open("call_all_posts.txt", "r") as f:
        call_all_posts = f.read()
        call_all_posts = call_all_posts.split("\n")
        call_all_posts = list(filter(None, call_all_posts))


def scan_submissions():
    global usernames
    global message
    global new_list
    subreddit = reddit.subreddit(SUBREDDIT)
    # For each submission that is new (up to x (limit=x) posts)
    for submission in subreddit.new(limit=LIMIT):
        # If the user prefix is in the submission body and isn't a post I've seen before (prevents infinate looping)
        if (' u/' in submission.selftext or ' /u/' in submission.selftext) and submission.id not in call_all_posts:
            print('Submission has a user!')
            # RegEx that pulls the username from the body
            usernames = re.findall('u\/[A-Za-z0-9_-]{3,20}', submission.selftext)
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
                    if reply is None:
                        print(message)
                        reply = submission.reply(message + bot_message)
                    elif reply is not None:
                        print(message)
                        reply = reddit.comment(id=reply).reply(message + bot_message)
            elif len(usernames) <= 2 and len(usernames) > 0:
                message = ''
                for user in usernames:
                    message = message + str(user) + " "
                print(message)
                submission.reply(message + bot_message)
            call_all_posts.append(submission.id)
            update_files(call_all_posts)


def update_files(call_all_posts):
    # Writes the post IDs to the file call_all_posts.txt
    with open("call_all_posts.txt", "w") as f:
        for x in call_all_posts:
            f.write(x + "\n")


# START
try:
    debug = input('debug mode?(1/0): ')
    while True:  # Indefinite looping
        scan_submissions()
        if debug == 1:
            print('No posts match... sleeping for 60s')
        # Makes it easier to interrupt script fast
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
