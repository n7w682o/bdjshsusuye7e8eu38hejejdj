import requests

chat_id = "2046706111"
urlp = "https://t.me/o6o6l"
url = f"https://api.telegram.org/bot/getChat?chat_id={chat_id}"

req = requests.get(url).json()
print(req)
