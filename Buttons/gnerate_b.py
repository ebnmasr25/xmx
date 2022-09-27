from pyrogram.types import *


class Generate:
	generate_buttons = InlineKeyboardMarkup(
	[
		[
			InlineKeyboardButton(text='- بايروجرام ',
			callback_data='pyrogram1'),
			InlineKeyboardButton(text='- تليثون ',
			callback_data='telethon')
		],
		[
			InlineKeyboardButton(text='- بايروجرام V2 ',
			callback_data='pyrogram')
		],
		[
			InlineKeyboardButton(text='Source -',
			url='https://t.me/em_source')
		],
	]
)

