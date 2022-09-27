from pyrogram import * 
from pyrogram.types import * 
import time
from Buttons.restart_b import re_b

@Client.on_message(filters.command('restart'))
async def restart(bot:Client,message:Message):
	x = await bot.send_message(
	chat_id=message.chat.id, 
	text="♻️ جارى اعادة تشغيل البوت يرجي الانتظار ."
	,reply_to_message_id=message.id
	)
	time.sleep(2)
	x1 = await bot.edit_message_text(
	chat_id=message.chat.id , 
	message_id=x.id, 
	text="_▰▱▱▱▱▱▱▱▱▱ 0%_"
	)
	time.sleep(2)
	x2 = await bot.edit_message_text(
	chat_id=message.chat.id, 
	message_id=x1.id,
	text="_▰▰▱▱▱▱▱▱▱▱ 10%_"
	)
	time.sleep(2)
	x3 = await bot.edit_message_text(
	chat_id= message.chat.id,
	message_id=x2.id,
	text="_▰▰▰▱▱▱▱▱▱▱ 19%_"
	)
	time.sleep(2)
	x4 = await bot.edit_message_text(
	chat_id=message.chat.id,
	message_id=x3.id,
	text="_▰▰▰▰▱▱▱▱▱▱ 28%_"
	)
	time.sleep(2)
	x5 = await bot.edit_message_text(
	chat_id=message.chat.id,
	message_id=x4.id,
	text="_▰▰▰▰▰▱▱▱▱▱ 40%_"
	)
	time.sleep(2)
	x6 = await bot.edit_message_text(
	chat_id=message.chat.id,
	message_id=x5.id,
	text="_▰▰▰▰▰▰▱▱▱▱ 47%_"
	)
	time.sleep(2)
	x7 = await bot.edit_message_text(
	chat_id=message.chat.id,
	message_id=x6.id,
	text="_▰▰▰▰▰▰▰▱▱▱ 56%_"
	)
	time.sleep(2)
	x8 = await bot.edit_message_text(
	chat_id=message.chat.id,
	message_id=x7.id,
	text="_▰▰▰▰▰▰▰▰▱▱ 67%_"
	)
	time.sleep(2)
	x9 = await bot.edit_message_text(
	chat_id=message.chat.id,
	message_id=x8.id,
	text="_▰▰▰▰▰▰▰▰▰▱ 88%_"
	)
	time.sleep(2)
	x10 = await bot.edit_message_text(
	chat_id=message.chat.id,
	message_id=x9.id,
	text="_▰▰▰▰▰▰▰▰▰▰ 100%_"
	)
	time.sleep(1)
	await bot.edit_message_text(
	chat_id=message.chat.id,
	message_id=x10.id,
	text="✅ تمت اعادة تشغيل البوت بنجاح يمكنك الان الاستخراج بدون اي مشاكل .",
	reply_markup=re_b.res
	)
	