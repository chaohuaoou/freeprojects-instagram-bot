from instagrapi import Client
import os, json, time

with(open(os.path.split(os.getcwd())[0] + "config.json", "r")) as f: config = json.load(f)
print("Config File Loaded")
USERNAME = config['username']
PASSWORD = config['password']

def unfollow(username: str, password: str):
    if os.name == 'nt': os.system('cls')
    else: os.system('clear')
    
    print("Logging into: " + username + "...")
    # Logging into the account using the config
    cl = Client()
    cl.login(username, password)
    print("Logged into: " + username)
    print("Entering 30 seconds wait")
    time.sleep(30)
    # Get all the users the client follows
    clId = cl.user_id_from_username(username)
    follows = cl.user_following(clId)
    # Save all their usernames to a file
    with(open(os.path.split(os.getcwd())[0] + "/followLogger/follows.txt", "r")) as file:
        exceptions = file.readlines
    for value in follows.values(): 
        userID = cl.user_id_from_username(value.username)
        if value not in exceptions:
            x = cl.user_unfollow(userID)
            if x: print("Successfully Unfollowed: " + value.username)
            else: print("Error couldnt unfollow: " + value.username)

    print("FINISHED")