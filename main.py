from instagrapi import Client
import json, time, random, os

# Reading the config file and converting it to a dictionary
config = {}
with(open("config.json", "r")) as f: config = json.load(f)
print("Config File Loaded")
USERNAME = config['username']
PASSWORD = config['password']
USERS_TO_SCRAPE = config['usernameToScrape']

def runBot(username, password):
    if os.name == 'nt': 
        os.system('cls')
    else: 
        os.system('clear')
    
    print("Logging into: " + username + "...")
    # Logging into the account using the config
    cl = Client()
    cl.login(username, password)
    print("Logged into: " + username)
    for user in USERS_TO_SCRAPE:
        print("Scraping User: " + user)
        # Getting the user's info
        userID = cl.user_id_from_username(user)

        # Getting the user's posts
        posts = cl.user_medias(userID, amount=5)

        # Looping through the posts
        for post in posts:
            print("    Scraping post: https://www.instagram.com/p/" + post.code)
            # Getting all the users who liked the post
            mediaLikers = cl.media_likers(post.id)    
            # Loop through the likers
            for liker in mediaLikers:
                # Getting the userID from their username
                userID = cl.user_id_from_username(liker.username)
                # Checking if user is a bot (or a private account)
                userDict = cl.user_info_by_username(liker.username).dict()
                if str(userDict['is_private']) == "False" and userDict['profile_pic_url'] != "":
                    cl.user_follow(userID)
                    userPosts = cl.user_medias(userID, amount=2)
                    for userPost in userPosts:
                        cl.media_like(userPost.id)
                    print("        Followed & Liked: " + str(liker.username))
                    # Generate a random number between 5 and 10
                    time.sleep(5 + (random.random() * 5))
                else:
                    print("        Skipping Bot/Private Account: " + str(liker.username))
    print("FINISHED")

runBot(USERNAME, PASSWORD)