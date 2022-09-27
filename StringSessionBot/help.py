from pyrogram import *
from helpers.h import help
from pyrogram.types import * 
from Buttons.help_b import Help

@Client.on_message(filters.command('help'))
async def helpx(bot:Client,message:Message):
	await message.reply(
	help.HELP,
	reply_markup=Help.help_buttons,
	reply_to_message_id=message.id
	)
	
	