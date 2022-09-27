from pyrogram import *
from pyrogram.types import *
from Buttons.tasteb import tst
import time

keb = tst.TST

@Client.on_message(filters.command('refresh'))
async def refreshx(bot:Client,message:Message):
	xm8 = await bot.send_message(
	chat_id=message.chat.id,
	text="♻️ جارى تحديث جميع ملفات البوت الرجاء عدم التحديث مرة اخرى خلال 3 دقائق لتجنب حدوث اخطاء ⚠️"
	,reply_to_message_id=message.id
	)
	time.sleep(180)
	await bot.delete_messages(
	chat_id=message.chat.id,
	message_ids=xm8.id
	)
	await bot.send_message(
	chat_id=message.chat.id,
	text="✅ تم تحديث جميع الملفات الي تم تسطيبها .\n\nstart.py\nid.py\ngenerate.py\nrestart.py\nrefresh.py\nButtons.py\nData.py\nxm8.py\n\n•♡ .وجميع الملفات الاخرى ."
	,reply_to_message_id=message.id,
	reply_markup=keb,
	disable_notification=False
	)
	
	
	