from pyrogram import Client, filters

bot_token = "6376389952:AAEF9IcywFK5jzITCMUQ6zA-w3rCKzl_nyk"

api_id = "20747544"
api_hash = "e9b10ac697383b967033d698f3750213"
app = Client("nb", api_id, api_hash, bot_token=bot_token)


app.start()


@app.on_message(filters.command("start"))
def start(client, message):
    message.reply_text(f"Hello")


app.run()

