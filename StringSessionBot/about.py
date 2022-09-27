from pyrogram import *
from pyrogram.types import *
from helpers.a import about
from Buttons.about_b import About

@Client.on_message(filters.command('about'))
async def aboutx(bot:Client,message:Message):
	await message.reply(
	about.ABOUT,
	reply_markup=About.about_buttons,
	reply_to_message_id=message.id
	)
	
	