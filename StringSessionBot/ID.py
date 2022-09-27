from pyrogram import * 
from pyrogram.types import *
from helpers.i import ID_MESSAGE
from Buttons.id_b import Id
import time 

@Client.on_message(filters.command('id'))
async def idx(bot:Client,message:Message):
	ida = message.from_user.id
	namea = message.from_user.mention
	usera = message.from_user.username
	cha = message.chat.id
	timea = time.strftime("%p %H:%M")
	datea = time.strftime("%Y/%m/%d")
	fira = message.from_user.first_name
	
	await bot.send_message(
	chat_id=message.chat.id , 
	text=ID_MESSAGE.ID_ME.format(fira,usera,ida,cha,timea,datea,namea),
	reply_markup=Id.ID_buttons,
	disable_web_page_preview=True, 
	reply_to_message_id=message.id,
	disable_notification=False
	)
	
	
	