from pyrogram.types import *
from env import CHANNEL

class re_b:
	res = InlineKeyboardMarkup([[InlineKeyboardButton(text='- بدء استخراج جلسه .',callback_data='generate')],[InlineKeyboardButton(text='- Channel .',url=f"https://t.me/{CHANNEL}")],])
	
	