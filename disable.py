import requests

def send_message(user_token, user_id, message_content):
    url = f"https://discord.com/api/v10/users/@me/channels"
    headers = {
        "Authorization": user_token,
        "Content-Type": "application/json"
    }
    payload = {
        "recipient_id": user_id
    }
    
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        channel_id = response.json().get("id")
        send_url = f"https://discord.com/api/v10/channels/{channel_id}/messages"
        send_payload = {
            "content": message_content
        }
        send_response = requests.post(send_url, headers=headers, json=send_payload)
        if send_response.status_code == 200:
            print("Message sent successfully!")
        else:
            print("Failed to send message.")
    else:
        print("Failed to create DM channel.")

# Usage example
user_token = "token"
user_id = "userID"
message_content = "Force me down!!!!"

send_message(user_token, user_id, message_content)
