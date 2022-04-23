from instagrapi import Client
from instagrapi.types import StoryMention, StoryMedia, StoryLink, StoryHashtag
import json, time, random

# Reading the config file and converting it to a dictionary
config = ""
with(open("config.json", "r")) as f: config = json.load(f)

USERNAME = config['username']
PASSWORD = config['password']
USERNAME_TO_SCRAPE = config['usernameToScrape']

# Logging into the account using the config
cl = Client()
cl.login(USERNAME, PASSWORD)

# Getting the user's info
userID = cl.user_id_from_username(USERNAME_TO_SCRAPE)

# Getting the user's posts
posts = cl.user_medias(userID, amount=5)

# Looping through the posts
for post in posts:
    # Getting all the users who liked the post
    mediaLikers = cl.media_likers(post.id)    
    # Loop through the likers
    for liker in mediaLikers:
        # Getting the userID from their username
        userID = cl.user_id_from_username(liker.username)
        # Following the user
        cl.user_follow(userID)
        # Gets their two recent posts
        userPosts = cl.user_medias(userID, amount=2)
        # Looping through those posts
        for userPost in userPosts:
            # Liking the post
            cl.media_like(userPost.id)
        # Simply printing their username
        print(liker.username)
        # Generate a random number between 5 and 10
        time.sleep( 5 + (random.random() * 5))
    break

print("FINISHED")