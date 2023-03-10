from pyrogram import Client, filters
import asyncio
from pyrogram.types import *
from pymongo import MongoClient
import requests
import random
from pyrogram.errors import (
    PeerIdInvalid,
    ChatWriteForbidden
)
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
import os
import re


API_ID = os.environ.get("API_ID", "17066403") 
API_HASH = os.environ.get("API_HASH", "a2d657aa05504a1ff984494d2cb1b82e") 
SESSION_NAME = os.environ.get("SESSION_NAME", "BQBM13o626Y0mvZ7COqYTxGW1fiWpRfAL2JQEE4QtgCoh7h3HJBYCNvvvnHAfotZcorWnuLLU-uy5hPo8ZpgoS2uYFtbYuUdAm2NVnLhXRZoUvtfZ6YyiK9V6aC_tC1eRiOZQF43-LB1kxltp7iks0mkbJhdS4gpe-5oshpr0NdOrTY_kn-5Q9ych03bFv6F3qhh-MvuEPTTn-OlvU_S7a05VRO7PeIlPA6pEP8Ki-6m88S4CBbJgpAbEzWz-5DCU3lVwDW2CzRI9vrRnFgbgYmokrHMhN5JpVRna2OLNoqBvZciGdTEK853Q4_sNyUFpPVUz07h6JLo4WzXjhXiuiABAAAAAVPNwMAA")
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://TITAN09:TITAN09@cluster0.xud0wjz.mongodb.net/?retryWrites=true&w=majority") 


client = Client(SESSION_NAME, API_ID, API_HASH)


@client.on_message(
    filters.command("repo", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatbot(client, message):
    await message.delete()
    candyai = await message.reply("๐คญ๐คโ๏ธ")
    await asyncio.sleep(1)
    await candyai.edit("**สแดสแดแด แดแดษชแด สแด สแดแดแด แดสแดสษชสแด**")
    await asyncio.sleep(1)
    await candyai.edit("**ษช แดแด แดแดษชษดษข แดส สแดแด แด ๐**")
    await candyai.delete()
    await asyncio.sleep(2)
    umm = await message.reply_sticker("CAACAgIAAxkBAAEForNjAykaq_efq4Wd-9KZv-nNxJRn3AACIgMAAm2wQgO8x8PfoXC1eCkE")
    await asyncio.sleep(2)
    await message.reply_photo(
        photo=f"https://telegra.ph/file/3f7c8a1feb6ae7e41e925.jpg",
        caption=f"""โโโโโโโโโโโโโโโโโโโโโโโโ
๐ฅ A แดแดแดกแดสาแดส แดษช สแดแด
แดา โป๏ธ ๐๐๐๐ ๐ฉ๐ฝ๐ช ๐๐๐ ๐ฅ
โโโโโโโโโโโโโโโโโ
แดแดแดแดสแดsแด สแดแดแดแดษดแด สแดแด าแดส แดษข...
โโโโโโโโโโโโโโโโโโโ
โฃโ แดสแดแดแดแดส [๐๐๐๐ ๐ฉ๐ฝ๐ช ๐๐๐](https://t.me/its_star_boi)
โฃโ สแดแด แดแดแดแดแดแดs [แดแดส แดแดสแดส สแดแดs](https://t.me/Star_X_Network)
โฃโ sแดแดแดแดสแด ษขสแดแดแด [แดสแดแด](https://t.me/Best_FriendsFor_Ever)
โโโโโโโโโโโโโโโโโโโ
๐ 
IF HAVE ANY QUESTION THEN CONTACT ยป TO ยป MY ยป [OWNER] @Its_star_boi""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("๐ผ sแดแดแดแดสแด ษขสแดแดแด ๐ฎ", url=f"https://t.me/Best_FriendsFor_Ever")]]
        ),
    ) 


@client.on_message(
    filters.command("alive", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def start(client, message):
    await message.reply_text(f"**แดแดษดแดส วซแดแดแดษด ษชs แดสษชแด แด**")
    
    
@client.on_message(
 (
        filters.text
        | filters.sticker
    )
    & ~filters.private
    & ~filters.me
    & ~filters.bot,
)
async def candyai(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]   

   if not message.reply_to_message:
       candydb = MongoClient(MONGO_URL)
       candy = candydb["CandyDb"]["Candy"] 
       is_candy = candy.find_one({"chat_id": message.chat.id})
       if not is_candy:
           await client.send_chat_action(message.chat.id, "typing")
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
       candydb = MongoClient(MONGO_URL)
       candy = candydb["CandyDb"]["Candy"] 
       is_candy = candy.find_one({"chat_id": message.chat.id})    
       getme = await client.get_me()
       user_id = getme.id                             
       if message.reply_to_message.from_user.id == user_id: 
           if not is_candy:                   
               await client.send_chat_action(message.chat.id, "typing")
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
       if not message.reply_to_message.from_user.id == user_id:          
           if message.sticker:
               is_chat = chatai.find_one({"word": message.reply_to_message.text, "id": message.sticker.file_unique_id})
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.text, "text": message.sticker.file_id, "check": "sticker", "id": message.sticker.file_unique_id})
           if message.text:                 
               is_chat = chatai.find_one({"word": message.reply_to_message.text, "text": message.text})                 
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.text, "text": message.text, "check": "none"})                                                                                                                                               

@client.on_message(
 (
        filters.sticker
        | filters.text
    )
    & ~filters.private
    & ~filters.me
    & ~filters.bot,
)
async def candystickerai(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]   

   if not message.reply_to_message:
       candydb = MongoClient(MONGO_URL)
       candy = candydb["CandyDb"]["Candy"] 
       is_candy = candy.find_one({"chat_id": message.chat.id})
       if not is_candy:
           await client.send_chat_action(message.chat.id, "typing")
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
       candydb = MongoClient(MONGO_URL)
       candy = candydb["CandyDb"]["Candy"] 
       is_candy = candy.find_one({"chat_id": message.chat.id})
       getme = await client.get_me()
       user_id = getme.id
       if message.reply_to_message.from_user.id == user_id: 
           if not is_candy:                    
               await client.send_chat_action(message.chat.id, "typing")
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
       if not message.reply_to_message.from_user.id == user_id:          
           if message.text:
               is_chat = chatai.find_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.text})
               if not is_chat:
                   toggle.insert_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.text, "check": "text"})
           if message.sticker:                 
               is_chat = chatai.find_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.sticker.file_id})                 
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.sticker.file_id, "check": "none"})    
              


@client.on_message(
    (
        filters.text
        | filters.sticker
    )
    & filters.private
    & ~filters.me
    & ~filters.bot,
)
async def candyprivate(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]
   if not message.reply_to_message: 
       await client.send_chat_action(message.chat.id, "typing")
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
       getme = await client.get_me()
       user_id = getme.id       
       if message.reply_to_message.from_user.id == user_id:                    
           await client.send_chat_action(message.chat.id, "typing")
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
                     
@client.on_message(
 (
        filters.sticker
        | filters.text
    )
    & filters.private
    & ~filters.me
    & ~filters.bot,
)
async def candyprivatesticker(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"] 
   if not message.reply_to_message:
       await client.send_chat_action(message.chat.id, "typing")
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
       getme = await client.get_me()
       user_id = getme.id       
       if message.reply_to_message.from_user.id == user_id:                    
           await client.send_chat_action(message.chat.id, "typing")
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
               

client.run()
