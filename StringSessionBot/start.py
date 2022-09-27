from helpers.s import Data
from pyrogram import *
from pyrogram.types import *
import requests
from env import CHANNEL,BOT_TOKEN
from Buttons.main import main

@Client.on_message(filters.command('start'))
async def strx(bot:Client,message:Message):
	do = requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/getChatMember?chat_id=@{CHANNEL}&user_id={message.from_user.id}").text
	if do.count("left") or do.count("Bad Request: user not found"):
	   	await message.reply(
    	"**⌁ : عَمࢪي ﭑشترك باݪقناه ﯡ ﭑسـتعمل ﭑݪبوت .**",
    	reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Channel -",url=f'https://t.me/{CHANNEL}')],]),
    	reply_to_message_id=message.id
    	)
	else:
	   await bot.send_message(
	   message.chat.id,
	   text=Data.START.format(message.from_user.mention),
	   reply_markup=main.main_buttons,
	   reply_to_message_id=message.id
	   )
	   
	   