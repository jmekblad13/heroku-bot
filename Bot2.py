# Dependencies
import tweepy
import random
import time

# Twitter API Keys
from config import (consumer_key, 
                    consumer_secret, 
                    access_token, 
                    access_token_secret)

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

# Quotes to Tweet
happy_quotes = [
    "(Repeat) For every minute you are angry you lose sixty seconds of happiness. - Ralph Waldo Emerson",
    "(Repeat) Folks are usually about as happy as they make their minds up to be. - Abraham Lincoln",
    "(Repeat) Happiness is when what you think, what you say, and what you do are in harmony. - Mahatma Gandhi",
    "(Repeat) Count your age by friends, not years. Count your life by smiles, not tears. - John Lennon",
    "(Repeat) Happiness is a warm puppy. - Charles M. Schulz",
    "(Repeat) The happiness of your life depends upon the quality of your thoughts. - Marcus Aurelius",
    "(Repeat) Now and then it's good to pause in our pursuit of happiness and just be happy. - Guillaume Apollinaire"]

# Create function for tweeting
def happy_it_up():
    """Tweet a Random Happiness Quote."""

    # Tweet a random quote
    msg = f"Happiness Tweet {time.time()}: {random.choice(happy_quotes)}"
    api.update_status(msg)

    # Print success message
    print("Tweeted successfully!")
    print(msg)

# Set timer to run every minute for 5 minutes max
t_end = time.time() + 60 * 5
while time.time() < t_end:
    happy_it_up()
    time.sleep(60)