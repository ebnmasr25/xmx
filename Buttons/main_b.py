from pyrogram.types import *
class main:
	
	main_buttons = InlineKeyboardMarkup(
	[
		[
			InlineKeyboardButton("- بـدء إستخـراج كـود .", callback_data="generate")
		],
		[
			InlineKeyboardButton("- قنـاة السـورس .", url="https://t.me/em_source")
		],
		[
			InlineKeyboardButton("- التعـليمـات ؟! .", callback_data="help"),
            InlineKeyboardButton("- حـول البـوت .", callback_data="about")
        ],
        [
        	InlineKeyboardButton("قناة البوستات .",url='https://t.me/Y9959')
        ],
        [
        	InlineKeyboardButton("#،𝙆𝒌 𝙊𝒐 𝙆𝒌 𝘼𝒂 💎⛓࿃", user_id=5411099822),
			InlineKeyboardButton("[⛥ .✘𝙀𝘽𝙉 𝙈𝘼𝙎𝙍 🇪🇬⛧’!×",user_id=5279877050)
		],
	]
)

