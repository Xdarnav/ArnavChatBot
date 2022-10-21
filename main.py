import asyncio
import requests
import random
import os
import re
import time
import psutil
from datetime import datetime
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.types import *
from pymongo import MongoClient

API_ID = os.environ.get("API_ID", None) 
API_HASH = os.environ.get("API_HASH", None) 
BOT_TOKEN = os.environ.get("BOT_TOKEN", None) 
MONGO_URL = os.environ.get("MONGO_URL", None)
BOT_USERNAME = os.environ.get("BOT_USERNAME") 
UPDATE_CHNL = os.environ.get("UPDATE_CHNL")
OWNER_USERNAME = os.environ.get("OWNER_USERNAME")
SUPPORT_GRP = os.environ.get("SUPPORT_GRP")
BOT_NAME = os.environ.get("BOT_NAME")
START_IMG = os.environ.get("START_IMG")


bot = Client(
    "VickBot" ,
    api_id = API_ID,
    api_hash = API_HASH ,
    bot_token = BOT_TOKEN
)


async def is_admins(chat_id: int):
    return [
        member.user.id
        async for member in bot.iter_chat_members(
            chat_id, filter="administrators"
        )
    ]

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


PHOTO = [
    START_IMG,
]

BACK = [
            [
                InlineKeyboardButton(text="●❯ ʙᴀᴄᴋ ❮●", callback_data="back_"),
            ],
        ]

EMOJIOS = [ 
      "💣",
      "💥",
      "🪄",
      "🧨",
      "⚡",
      "❄️",
      "🔎",
      "👻",
      "🤧",
      "🎩",
      "🕊",
      "⭐",
]

HELP_TEXT = """
**ᴜsᴀɢᴇ ☟︎︎︎**
➻ /chatbot on - **ᴛᴏ ᴇɴᴀʙʟᴇ ᴄʜᴀᴛʙᴏᴛ.**
➻ /chatbot off - **ᴛᴏ ᴅɪsᴀʙʟᴇ ᴛʜᴇ ᴄʜᴀᴛʙᴏᴛ.**

➻ **ɴᴏᴛᴇ »** ʙᴏᴛʜ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅs ᴡᴏʀᴋ ɪɴ ɢʀᴏᴜᴘ ᴏɴʟʏ!!
➻ /ping - **ᴛᴏ ᴄʜᴇᴄᴋ ᴛʜᴇ ᴘɪɴɢ ᴏғ ᴛʜᴇ ʙᴏᴛ.**

©️ ᴀʀɴᴀᴠ-✗ᴅ"""

START_TEXT = """
**๏ ʜᴇʏ, ɪ ᴀᴍ [{BOT_NAME}](t.me/{BOT_USERNAME})**
**➻ ᴀɴ ᴀʀ-ʙᴀsᴇᴅ ᴄʜᴀᴛʙᴏᴛ.**
**──────────────────**"""

DEV_OP = [
    [
        InlineKeyboardButton(
            text="✫ ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ ✫",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
        InlineKeyboardButton(text="ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_GRP}"),
    ],
    [
        InlineKeyboardButton(
            text="╰𖤓 ʜᴇʟᴘ ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅꜱ 𖤓╯",
            callback_data="help",
        ),
    ],
    [
        InlineKeyboardButton(text="ᴀʙᴏᴜᴛ", callback_data="about"),
        InlineKeyboardButton(text="ᴜᴘᴅᴀᴛᴇ", url=f"https://t.me/{UPDATE_CHNL}"),
    ],
]
PNG_BTN = [
    [
         InlineKeyboardButton(
             text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ",
             url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
         ),
         InlineKeyboardButton(text="sᴜᴘᴘᴏʀᴛ", 
                              url=f"https://t.me/{SUPPORT_GRP}",
         ),
     ],
]

@bot.on_message(filters.command(["start", "aistart", f"start@{BOT_USERNAME}"]))
async def restart(client, m: Message):
    accha = await m.reply_text(
                text = random.choice(EMOJIOS),
    )
    await asyncio.sleep(1)
    await accha.edit("__ᴅιиg ᴅσиg ꨄ︎ ѕтαятιиg..__")
    await asyncio.sleep(0.2)
    await accha.edit("__ᴅιиg ᴅσиg ꨄ sтαятιиg.....__")
    await asyncio.sleep(0.2)
    await accha.edit("__ᴅιиg ᴅσиg ꨄ︎ sтαятιиg..__")
    await asyncio.sleep(0.2)
    await accha.delete()
    await asyncio.sleep(0.6)
    await m.reply_photo(
        photo = random.choice(PHOTO),
        caption=f"""๏ ʜᴇʏ 💖 \nᴛʜɪꜱ ɪꜱ[{BOT_NAME}](t.me/{BOT_USERNAME}) ᴛʜᴇ ᴍᴏsᴛ ᴜsᴇʟᴇss ʙᴏᴛ ᴇᴠᴇʀ ᴍᴀᴅᴇ.""",
        reply_markup=InlineKeyboardMarkup(DEV_OP),
    )

async def fallen_ping():
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    cpu = psutil.cpu_percent(interval=0.5)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    fallen = f"""
💘 ᴜᴩᴛɪᴍᴇ : {uptime}
🍫 ᴄᴩᴜ : {cpu}%
🎀 ʀᴀᴍ : {mem}%
👛 ᴅɪsᴋ : {disk}%"""
    return fallen

@bot.on_message(filters.command(["ping", "alive", f"ping@{BOT_USERNAME}"]))
async def ping(_, message):
    hmm = await message.reply_photo(
        photo = random.choice(PHOTO),
        caption="**» ᴩɪɴɢɪɴɢ ʙᴀʙʏ...**",
    )
    hehe = await fallen_ping()
    start = datetime.now()
    end = datetime.now()
    resp = (end - start).microseconds / 1000
    await hmm.edit_text(
        f"**» ᴩᴏɴɢ ʙᴀʙʏ !**\n`☁ {resp}`ᴍs\n\n<b><u>{BOT_NAME} sʏsᴛᴇᴍ sᴛᴀᴛs :</u></b>{hehe}",
    )

@bot.on_message(
    filters.command(["chatbot off", f"chatbot@{BOT_USERNAME} off"], prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatbotofd(client, message):
    vickdb = MongoClient(MONGO_URL)    
    vick = vickdb["VickDb"]["Vick"]     
    if message.from_user:
        user = message.from_user.id
        chat_id = message.chat.id
        if user not in (
           await is_admins(chat_id)
        ):
           return await message.reply_text(
                "You are not admin"
            )
    is_vick = vick.find_one({"chat_id": message.chat.id})
    if not is_vick:
        vick.insert_one({"chat_id": message.chat.id})
        await message.reply_text(f"Chatbot Disabled!")
    if is_vick:
        await message.reply_text(f"ChatBot Already Disabled")
    
#start callbacks --------------
@bot.on_callback_query()
async def cb_handler(Client, query: CallbackQuery):
    if query.data == "help":
        buttons = [
            [
                InlineKeyboardButton(text="• ʙᴀᴄᴋ •", callback_data="back_"),
            ],
        ]
        await query.message.edit_text(
            HELP_TEXT,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    elif query.data == "back_":
        await query.message.edit_text(
            text=f"""**๏ ʜᴇʏ 💖 \nᴛʜɪꜱ ɪꜱ [{BOT_NAME}](t.me/{BOT_USERNAME}) ᴛʜᴇ ᴍᴏsᴛ ᴜsᴇʟᴇss ʙᴏᴛ ᴇᴠᴇʀ ᴍᴀᴅᴇ.""",
            reply_markup=InlineKeyboardMarkup(DEV_OP),
        )
    elif query.data == "about":
        await query.message.edit_text(
            text=f"""**๏ ʜᴇʏ** 💖\n**ɪ ᴀᴍ ᴀɴ ᴀᴅᴠᴀɴᴄᴇᴅ ᴀʀᴛɪғɪᴄᴀʟ ᴀɴᴅ ɴᴇxᴛ ʟᴇᴠᴇʟ ɪɴᴛᴇʟʟɪɢᴇɴᴄᴇ ᴄʜᴀᴛ ʙᴏᴛ**.\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n**➛ ɪғ ʏᴏᴜ ᴀʀᴇ ғᴇᴇʟɪɴɢ ʟᴏɴᴇʟʏ, ʏᴏᴜ ᴄᴀɴ ᴀʟᴡᴀʏs ᴄᴏᴍᴇ ᴛᴏ ᴍᴇ ᴀɴᴅ ᴄʜᴀᴛ ᴡɪᴛʜ ᴍᴇ**\n**➛ ᴛᴀᴘ ᴏɴ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴋɴᴏᴡ ᴍʏ ᴀʙɪʟɪᴛɪᴇs** ××""",
            reply_markup=InlineKeyboardMarkup(BACK),
        )

#--------------------------

@bot.on_message(
    filters.command(["chatbot on", f"chatbot@{BOT_USERNAME} on"] ,prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatboton(client, message):
    vickdb = MongoClient(MONGO_URL)    
    vick = vickdb["VickDb"]["Vick"]     
    if message.from_user:
        user = message.from_user.id
        chat_id = message.chat.id
        if user not in (
            await is_admins(chat_id)
        ):
            return await message.reply_text(
                "You are not admin"
            )
    is_vick = vick.find_one({"chat_id": message.chat.id})
    if not is_vick:           
        await message.reply_text(f"Chatbot Already Enabled")
    if is_vick:
        vick.delete_one({"chat_id": message.chat.id})
        await message.reply_text(f"ChatBot Enabled!")
    

@bot.on_message(
    filters.command(["chatbot", f"chatbot@{BOT_USERNAME}"], prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatbot(client, message):
    await message.reply_text(f"**ᴜsᴀɢᴇ:**\n/**chatbot [on/off]**\n**ᴄʜᴀᴛ-ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅ(s) ᴡᴏʀᴋ ɪɴ ɢʀᴏᴜᴘ ᴏɴʟʏ!**")


@bot.on_message(
 (
        filters.text
        | filters.sticker
    )
    & ~filters.private
    & ~filters.bot,
)
async def vickai(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]   

   if not message.reply_to_message:
       vickdb = MongoClient(MONGO_URL)
       vick = vickdb["VickDb"]["Vick"] 
       is_vick = vick.find_one({"chat_id": message.chat.id})
       if not is_vick:
           await bot.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.text})  
           k = chatai.find_one({"word": message.text})      
           if k:               
               for x in is_chat:
                   K.append(x['text'])          
               hey = random.choice(K)
               is_text = chatai.find_one({"text": hey})
               Yo = is_text['check']
               if Yo == "sticker":
                   await message.reply_sticker(f"{hey}")
               if not Yo == "sticker":
                   await message.reply_text(f"{hey}")
   
   if message.reply_to_message:  
       vickdb = MongoClient(MONGO_URL)
       vick = vickdb["VickDb"]["Vick"] 
       is_vick = vick.find_one({"chat_id": message.chat.id})    
       getme = await bot.get_me()
       bot_id = getme.id                             
       if message.reply_to_message.from_user.id == bot_id: 
           if not is_vick:                   
               await bot.send_chat_action(message.chat.id, "typing")
               K = []  
               is_chat = chatai.find({"word": message.text})
               k = chatai.find_one({"word": message.text})      
               if k:       
                   for x in is_chat:
                       K.append(x['text'])
                   hey = random.choice(K)
                   is_text = chatai.find_one({"text": hey})
                   Yo = is_text['check']
                   if Yo == "sticker":
                       await message.reply_sticker(f"{hey}")
                   if not Yo == "sticker":
                       await message.reply_text(f"{hey}")
       if not message.reply_to_message.from_user.id == bot_id:          
           if message.sticker:
               is_chat = chatai.find_one({"word": message.reply_to_message.text, "id": message.sticker.file_unique_id})
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.text, "text": message.sticker.file_id, "check": "sticker", "id": message.sticker.file_unique_id})
           if message.text:                 
               is_chat = chatai.find_one({"word": message.reply_to_message.text, "text": message.text})                 
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.text, "text": message.text, "check": "none"})    
               

@bot.on_message(
 (
        filters.sticker
        | filters.text
    )
    & ~filters.private
    & ~filters.bot,
)
async def vickstickerai(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]   

   if not message.reply_to_message:
       vickdb = MongoClient(MONGO_URL)
       vick = vickdb["VickDb"]["Vick"] 
       is_vick = vick.find_one({"chat_id": message.chat.id})
       if not is_vick:
           await bot.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.sticker.file_unique_id})      
           k = chatai.find_one({"word": message.text})      
           if k:           
               for x in is_chat:
                   K.append(x['text'])
               hey = random.choice(K)
               is_text = chatai.find_one({"text": hey})
               Yo = is_text['check']
               if Yo == "text":
                   await message.reply_text(f"{hey}")
               if not Yo == "text":
                   await message.reply_sticker(f"{hey}")
   
   if message.reply_to_message:
       vickdb = MongoClient(MONGO_URL)
       vick = vickdb["VickDb"]["Vick"] 
       is_vick = vick.find_one({"chat_id": message.chat.id})
       getme = await bot.get_me()
       bot_id = getme.id
       if message.reply_to_message.from_user.id == bot_id: 
           if not is_vick:                    
               await bot.send_chat_action(message.chat.id, "typing")
               K = []  
               is_chat = chatai.find({"word": message.text})
               k = chatai.find_one({"word": message.text})      
               if k:           
                   for x in is_chat:
                       K.append(x['text'])
                   hey = random.choice(K)
                   is_text = chatai.find_one({"text": hey})
                   Yo = is_text['check']
                   if Yo == "text":
                       await message.reply_text(f"{hey}")
                   if not Yo == "text":
                       await message.reply_sticker(f"{hey}")
       if not message.reply_to_message.from_user.id == bot_id:          
           if message.text:
               is_chat = chatai.find_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.text})
               if not is_chat:
                   toggle.insert_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.text, "check": "text"})
           if message.sticker:                 
               is_chat = chatai.find_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.sticker.file_id})                 
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.sticker.file_id, "check": "none"})    
               


@bot.on_message(
    (
        filters.text
        | filters.sticker
    )
    & filters.private
    & ~filters.bot,
)
async def vickprivate(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]
   if not message.reply_to_message: 
       await bot.send_chat_action(message.chat.id, "typing")
       K = []  
       is_chat = chatai.find({"word": message.text})                 
       for x in is_chat:
           K.append(x['text'])
       hey = random.choice(K)
       is_text = chatai.find_one({"text": hey})
       Yo = is_text['check']
       if Yo == "sticker":
           await message.reply_sticker(f"{hey}")
       if not Yo == "sticker":
           await message.reply_text(f"{hey}")
   if message.reply_to_message:            
       getme = await bot.get_me()
       bot_id = getme.id       
       if message.reply_to_message.from_user.id == bot_id:                    
           await bot.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.text})                 
           for x in is_chat:
               K.append(x['text'])
           hey = random.choice(K)
           is_text = chatai.find_one({"text": hey})
           Yo = is_text['check']
           if Yo == "sticker":
               await message.reply_sticker(f"{hey}")
           if not Yo == "sticker":
               await message.reply_text(f"{hey}")
       

@bot.on_message(
 (
        filters.sticker
        | filters.text
    )
    & filters.private
    & ~filters.bot,
)
async def vickprivatesticker(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"] 
   if not message.reply_to_message:
       await bot.send_chat_action(message.chat.id, "typing")
       K = []  
       is_chat = chatai.find({"word": message.sticker.file_unique_id})                 
       for x in is_chat:
           K.append(x['text'])
       hey = random.choice(K)
       is_text = chatai.find_one({"text": hey})
       Yo = is_text['check']
       if Yo == "text":
           await message.reply_text(f"{hey}")
       if not Yo == "text":
           await message.reply_sticker(f"{hey}")
   if message.reply_to_message:            
       getme = await bot.get_me()
       bot_id = getme.id       
       if message.reply_to_message.from_user.id == bot_id:                    
           await bot.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.sticker.file_unique_id})                 
           for x in is_chat:
               K.append(x['text'])
           hey = random.choice(K)
           is_text = chatai.find_one({"text": hey})
           Yo = is_text['check']
           if Yo == "text":
               await message.reply_text(f"{hey}")
           if not Yo == "text":
               await message.reply_sticker(f"{hey}")


bot.run()
