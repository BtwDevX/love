from pyrogram import Client, filters
import requests
import random

api_id = 24960183 #--Add your Api Id here
api_hash = '0e2d0364c5b460ab2c7ba477a40595de' #--Enter Api Hash Here

token = '7248526463:AAGGVO1jhqQ8lzYu3xhbKv2T0uDmJouoQe0' #--Enter Bot Token Here.

emojis = ["👍", "👎", "❤", "🔥", "🥰", "👏", "😁", "🤔", "🤯", "😱", "🤬", "😢", "🎉", "🤩", "🤮", "💩", "🙏", "👌", "🕊", "🤡", "🥱", "🥴", "😍", "🐳", "❤‍🔥", "🌚", "🌭", "💯", "🤣", "⚡", "🍌", "🏆", "💔", "🤨", "😐", "🍓", "🍾", "💋", "🖕", "😈", "😴", "😭", "🤓", "👻", "👨‍💻", "👀", "🎃", "🙈", "😇", "😨", "🤝", "✍", "🤗", "🫡", "🎅", "🎄", "☃", "💅", "🤪", "🗿", "🆒", "💘", "🙉", "🦄", "😘", "💊", "🙊", "😎", "👾", "🤷‍♂", "🤷", "🤷‍♀", "😡"]

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=token)

@app.on_message()
async def react_to_message(client, message):
    chat_id = message.chat.id
    message_id = message.id
    
    # Choose a random emoji from the list
    random_emoji = random.choice(emojis)
    
    url = f'https://api.telegram.org/bot{token}/setMessageReaction'

    # Parameters for the request
    params = {
        'chat_id': chat_id,
        'message_id': message_id,
        'reaction': [{
            "type": "emoji",
            "emoji": random_emoji
        }]
    }

    response = requests.post(url, json=params)

    if response.status_code == 200:
        print("Reaction set successfully!")
        print("Response content:", response.content)
    else:
        print(f"Failed to set reaction. Status code: {response.status_code}")
        print("Response content:", response.content)
    
app.run()
