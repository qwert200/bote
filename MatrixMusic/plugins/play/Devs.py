import asyncio
import os
import time
import requests
import aiohttp
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from MatrixMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from MatrixMusic import app
from asyncio import gather
from pyrogram.errors import FloodWait
from config import OWNER_ID
from random import  choice, randint

def get_file_id(msg: Message):
    if msg.media:
        for message_type in (
            "photo",
            "animation",
            "audio",
            "document",
            "video",
            "video_note",
            "voice",
            # "contact",
            # "dice",
            # "poll",
            # "location",
            # "venue",
            "sticker",
        ):
            obj = getattr(msg, message_type)
            if obj:
                setattr(obj, "message_type", message_type)
                return obj

@app.on_message(
    command(["المبرمج","حمد","مبرمج السورس","الـمبرمج])
    & filters.group
  
)
async def yas(client, message):
    usr = await client.get_chat("ah_2_v")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"<b>⦗ الـمبرمج ⦘<b>\n<b>↯︙𝖣𝖾𝗏 ↬ ⦗ {name} ⦘<b>\n<b>↯︙𝖴𝗌𝖤𝗋 ↬ ⦗ @{usr.username} ⦘<b>\n<b>↯︙𝖨𝖣 ↬ ⦗ {usr.id} ⦘<b>\n<b>↯︙𝖡𝗂𝖮 ↬ ⦗ {usr.bio} ⦘<b>",  
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )




