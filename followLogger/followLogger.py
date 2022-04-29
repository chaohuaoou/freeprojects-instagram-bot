from instagrapi import Client
import json, time, os

# Reading the config file and converting it to a dictionary
with(open("./config.json", "r")) as f: config = json.load(f)
print("Config File Loaded")
USERNAME = config['username']
PASSWORD = config['password']

def logFollows(username, password):
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
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
    with open("follows.txt", "w") as file:
        for value in follows.values(): file.write(value.username + "\n")
    print("FINISHED")


logFollows(USERNAME, PASSWORD)
