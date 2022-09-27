from pyrogram.types import * 
from env import CHANNEL

class Id:
	ID_buttons = InlineKeyboardMarkup([[InlineKeyboardButton(text='source -',url=f'https://t.me/{CHANNEL}')],])
	
	