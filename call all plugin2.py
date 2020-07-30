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
from loguru import logger
from datetime import datetime
import random


__author__ = 'jcsumlin'
__version__ = '0.3.1'
log_date = str(datetime.now().month)+"-"+str(datetime.now().day)+"-"+str(datetime.now().year)
logger.add('file_{}.log'.format(log_date), rotation="12:00", colorize=True, backtrace=False)
config = configparser.ConfigParser()
config.read('auth.ini')  # All my usernames and passwords for the api

reddit = praw.Reddit(client_id=config.get('auth', 'reddit_client_id'),
                     client_secret=config.get('auth', 'reddit_client_secret'),
                     password=config.get('auth', 'reddit_password'),
                     user_agent='All-Seeing Eye (by u/J_C___)',
                     username=config.get('auth', 'reddit_username'))

SUBREDDIT = config.get('auth', 'reddit_subreddit')
LIMIT = int(config.get('auth', 'reddit_limit'))

'''
Static variables for bot.
'''
subject = "All-Seeing Eye Bot: You have been summoned!"
message = f"Hey there %s! %s has just mentioned you in a post on r/{config.get('auth', 'reddit_subreddit')} titled \"**%s**\".\r\rYou can find the post at this link here: [HERE!](%s)"
bot_message = "\r\r___ \r ^(If you think you are recieving this message in error please) [^(let me know)](/message/compose/?to=J_C___&subject=all_seeing_eye_bot) ^| [^Feedback](https://goo.gl/forms/DSPuGXV8SuKu1pV13) ^| [^Source](https://github.com/jcsumlin/call-all-plugin)"
faces = ["(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ ✧ﾟ･: *ヽ(◕ヮ◕ヽ)", "(づ｡◕‿‿◕｡)づ", "| (• ◡•)| (❍ᴥ❍ʋ)", "ᕙ(⇀‸↼‶)ᕗ", ""]
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
        if ('u/' in submission.selftext or '/u/' in submission.selftext) and submission.id not in call_all_posts:
            logger.info('Submission has a user!: ' + submission.id)
            # RegEx that pulls the username from the body
            usernames = re.findall('[\/]?u\/[A-Za-z0-9_-]+', submission.selftext)
            if submission.author in usernames:
                usernames.remove(submission.author)
            # Makes sure there are no duplicates in the list
            duplicate_checker = []
            for user in usernames:
                if user.startswith("/"):
                    user = user[1:]
                if user not in duplicate_checker and user is not str(submission.author):
                    duplicate_checker.append(user)

            # Send Messages to users
            count = 0
            for user in duplicate_checker:
                try:
                    if count == 10:
                        time.sleep(60)
                        count = 0
                    reddit.redditor(user).message(subject, (message % (user, submission.author.name, submission.title, submission.url)) + bot_message)
                    logger.info('Sent to: %s' % user)
                    count += 1
                except TypeError as e:
                    logger.error('Ran into a type error: %s' % e)
                    pass
                except Exception as e:
                    logger.critical('Ran into an unknown error! %s' % e)
                    pass
            # if len(usernames) >= 3:
            #     new_list = []
            #     reply = None
            #     i = 0
            #     while i < len(usernames):
            #         new_list.append(usernames[i:i + 3])
            #         i += 3
            #     for group in new_list:
            #         message = ''
            #         for user in group:
            #             message = message + str(user) + " "
            #         if reply is None:
            #             logging.info(message)
            #             reply = submission.reply(message + bot_message)
            #             logging.info("Reply sent")
            #         elif reply is not None:
            #             reply = reddit.comment(id=reply).reply(message + bot_message)
            #             logging.info("Sub Reply sent")
            # elif len(usernames) <= 2 and len(usernames) > 0:
            #     message = ''
            #     for user in usernames:
            #         message = message + str(user) + " "
            #     logging.info("Reply sent")
            #     submission.reply(message + bot_message)

            submission.reply("All users have been called! " + random.choice(faces) + bot_message)
            call_all_posts.append(submission.id)
            update_files(call_all_posts)


def update_files(call_all_posts):
    # Writes the post IDs to the file call_all_posts.txt
    with open("call_all_posts.txt", "w") as f:
        for x in call_all_posts:
            f.write(x + "\n")


if __name__ == "__main__":
    # START
    try:
        logger.info("------Starting Call All Bot------")
        logger.info("Logged in and posting as:%s" % reddit.user.me())
        while True:
            try:
                scan_submissions()
                # Makes it easier to interrupt script fast
                time.sleep(15)
            except KeyboardInterrupt:
                logger.info('Run interrupted')
            except Exception as e:
                logger.critical("Uncaught error: %s" % e)
                time.sleep(30)
                pass
    finally:
        update_files(call_all_posts)
        logger.info("Files Updated")
