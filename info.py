import requests

# Replace with your Slack app's OAuth token
oauth_token = "xoxb-..."  

#ID of your Slack channel
channel_id = "C0W68DQBS"  

# Get the list of user IDs in the channel
response = requests.get(
    "https://slack.com/api/conversations.members",
    headers={"Authorization": f"Bearer {oauth_token}"},
    params={"channel": channel_id}
)

# Check if the request was successful
if response.status_code == 200:
    members = response.json().get("members", [])
    print("User IDs in channel:", members)
else:
    print(f"Failed to retrieve members: {response.status_code}")

# Optionally, get detailed information for each user
for user_id in members:
    response = requests.get(
        "https://slack.com/api/users.info",
        headers={"Authorization": f"Bearer {oauth_token}"},
        params={"user": user_id}
    )
    if response.status_code == 200:
        user_info = response.json().get("user", {})
        print(f"User Info for {user_id}:", user_info)
    else:
        print(f"Failed to retrieve user info for {user_id}: {response.status_code}")
