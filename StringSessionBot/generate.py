from Buttons.gnerate_b import Generate
from pyrogram.types import Message
from telethon import TelegramClient
from pyrogram import Client, filters
from pyrogram1 import Client as Client1
from asyncio.exceptions import TimeoutError
from telethon.sessions import StringSession
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import (
    ApiIdInvalid,
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid
)
from pyrogram1.errors import (
    ApiIdInvalid as ApiIdInvalid1,
    PhoneNumberInvalid as PhoneNumberInvalid1,
    PhoneCodeInvalid as PhoneCodeInvalid1,
    PhoneCodeExpired as PhoneCodeExpired1,
    SessionPasswordNeeded as SessionPasswordNeeded1,
    PasswordHashInvalid as PasswordHashInvalid1
)
from telethon.errors import (
    ApiIdInvalidError,
    PhoneNumberInvalidError,
    PhoneCodeInvalidError,
    PhoneCodeExpiredError,
    SessionPasswordNeededError,
    PasswordHashInvalidError
)

gn = Generate.generate_buttons

ask_ques = "**الرجاء اختار نوع المكتبه لاستخراج الكود الخاص بها**"
buttons_ques = [
    [
        InlineKeyboardButton("- بـايـروجـرام .", callback_data="pyrogram1"),
        InlineKeyboardButton("- تـلـيـثـون .", callback_data="telethon"),
    ],
    [
        InlineKeyboardButton("- بـايـروجـرام v2 .", callback_data="pyrogram"),
    ],
    # [
    #     InlineKeyboardButton("Pyrogram Bot", callback_data="pyrogram_bot"),
    #     InlineKeyboardButton("Telethon Bot", callback_data="telethon_bot"),
    # ],
]


@Client.on_message(filters.private & ~filters.forwarded & filters.command('generate'))
async def main(_, msg):
    await msg.reply(ask_ques, reply_markup=InlineKeyboardMarkup(buttons_ques))


async def generate_session(bot: Client, msg: Message, telethon=False, old_pyro: bool = False, is_bot: bool = False):
    if telethon:
        ty = "Telethon"
    else:
        ty = "Pyrogram"
        if not old_pyro:
            ty += " v2"
    if is_bot:
        ty += " Bot"
    await msg.reply(f"بـدء {ty} استخـراج الجلسـه ⌬....")
    user_id = msg.chat.id
    api_id_msg = await bot.ask(user_id, '- حسنـا الان يرجى ارسـال كـود `API_ID`', filters=filters.text)
    if await cancelled(api_id_msg):
        return
    try:
        api_id = int(api_id_msg.text)
    except ValueError:
        await api_id_msg.reply('API_ID غير صحيح (والذي يجب أن يكون عددًا صحيحًا). يرجى البدء في إنشاء الجلسة مرة أخرى.', quote=True, reply_markup=gn)
        return
    api_hash_msg = await bot.ask(user_id, '- حسنـا الان يرجى ارسـال كـود `API_HASH`', filters=filters.text)
    if await cancelled(api_hash_msg):
        return
    api_hash = api_hash_msg.text
    if not is_bot:
        t = "Now - حسنـا الان يرجى ارسـال `رقــم هــاتــفـــك`. \nمــثــال : `+20***********`"
    else:
        t = "Now - حسنـا الان يرجى ارسـال `تــوكــن الــبــوت` \nمــثــال : `12345:abcdefghijklmnopqrstuvwxyz`'"
    phone_number_msg = await bot.ask(user_id, t, filters=filters.text)
    if await cancelled(phone_number_msg):
        return
    phone_number = phone_number_msg.text
    await msg.reply("- جـاري ارسـال الكـود ⎙...")
    if telethon and is_bot:
        client = TelegramClient(StringSession(), api_id, api_hash)
        await client.start(bot_token=phone_number)
    elif telethon:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif is_bot:
        client = Client(name="bot", api_id=api_id, api_hash=api_hash, bot_token=phone_number, in_memory=True)
    elif old_pyro:
        client = Client1(":memory:", api_id=api_id, api_hash=api_hash)
    else:
        client = Client(name="user", api_id=api_id, api_hash=api_hash, in_memory=True)
    await client.connect()
    try:
        code = None
        if not is_bot:
            if telethon:
                code = await client.send_code_request(phone_number)
            else:
                code = await client.send_code(phone_number)
    except (ApiIdInvalid, ApiIdInvalidError, ApiIdInvalid1):
        await msg.reply('`- عذرا معلومات ال API_HASH وال API_ID غير صالحة يرجى اعادة الخطوات كامله .', reply_markup=gn)
        return
    except (PhoneNumberInvalid, PhoneNumberInvalidError, PhoneNumberInvalid1):
        await msg.reply('`- رقم هاتفك غير صالح ! يرجى اعادة الخطوات كامله .', reply_markup=gn)
        return
    try:
        phone_code_msg = None
        if not is_bot:
            phone_code_msg = await bot.ask(user_id, "يرجى التحقق من وجود كلمة مرور في حسابك. إذا كان هناك تحقق بخطوتين( المرور ) ، أرسل كلمة المرور هنا بعد ارسال كود الدخول بالتنسيق أدناه.\n- اذا كانت كلمة المرور او الكود  هي ``12345`` يرجى ارسالها بالشكل التالي ``1 2 3 4 5`` مع وجود مسـافـات بين الارقام اذا احتجت مساعدة @JS_J6", filters=filters.text, timeout=600)
            if await cancelled(phone_code_msg):
                return
    except TimeoutError:
        await msg.reply('بلغ الحد الزمني 10 دقائق. يرجى البدء في إنشاء الجلسة مرة أخرى.', reply_markup=gn)
        return
    if not is_bot:
        phone_code = phone_code_msg.text.replace(" ", "")
        try:
            if telethon:
                await client.sign_in(phone_number, phone_code, password=None)
            else:
                await client.sign_in(phone_number, code.phone_code_hash, phone_code)
        except (PhoneCodeInvalid, PhoneCodeInvalidError, PhoneCodeInvalid1):
            await msg.reply('OTP غير صالح. يرجى البدء في إنشاء الجلسة مرة أخرى.', reply_markup=gn)
            return
        except (PhoneCodeExpired, PhoneCodeExpiredError, PhoneCodeExpired1):
            await msg.reply('انتهت صلاحية كلمة المرور لمرة واحدة. يرجى البدء في إنشاء الجلسة مرة أخرى.', reply_markup=gn)
            return
        except (SessionPasswordNeeded, SessionPasswordNeededError, SessionPasswordNeeded1):
            try:
                two_step_msg = await bot.ask(user_id, 'لقد مكّن حسابك التحقق على خطوتين. يرجى تقديم كلمة المرور.', filters=filters.text, timeout=300)
            except TimeoutError:
                await msg.reply('بلغ الحد الزمني 5 دقائق. يرجى البدء في إنشاء الجلسة مرة أخرى.', reply_markup=gn)
                return
            try:
                password = two_step_msg.text
                if telethon:
                    await client.sign_in(password=password)
                else:
                    await client.check_password(password=password)
                if await cancelled(api_id_msg):
                    return
            except (PasswordHashInvalid, PasswordHashInvalidError, PasswordHashInvalid1):
                await two_step_msg.reply('- أدخلت كلمة مرور غير صالحة. يرجى البدء في إنشاء الجلسة مرة أخرى.', quote=True, reply_markup=gn)
                return
    if telethon:
        string_session = client.session.save()
    else:
        string_session = await client.export_session_string()
    text = f"**{ty.upper()} كود تيرمكس** \n\n`{string_session}` \n\تم الاستخـراج بواسطـة @JS_J6 ."
    try:
        if not is_bot:
            await client.send_message("me", text)
        else:
            await bot.send_message(msg.chat.id, text)
    except KeyError:
        pass
    await client.disconnect()
    await bot.send_message(msg.chat.id, "تم الاستخـراج بنجاح {} كود تيرمكس. \n\nالرجـاء التحـقق مـن حافظـة حسـابك! \n\nبواسطـة @JS_J6".format("telethon" if telethon else "pyrogram"))


async def cancelled(msg):
    if "/cancel" in msg.text:
        await msg.reply("- تم الالغاء .", quote=True, reply_markup=gn)
        return True
    else:
        return False
