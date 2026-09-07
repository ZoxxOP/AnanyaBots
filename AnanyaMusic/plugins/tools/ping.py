                                                 
                        
                                                                                
                                          
 
            
                                                                       
                                                                                            
                                                                                  
                                                   
 
                                                     
                                                 

import random
from datetime import datetime
from pyrogram import filters
from pyrogram.types import Message
from AnanyaMusic import app
from AnanyaMusic.core.call import Shivi
from AnanyaMusic.utils import bot_sys_stats
from AnanyaMusic.utils.decorators.language import language
from AnanyaMusic.utils.inline import supp_markup
from config import BANNED_USERS, PING_IMG_URL

Shivi_PIC = [
    "https://files.catbox.moe/fh7vw7.jpg",
    "https://files.catbox.moe/lckxh6.jpg",
    "https://files.catbox.moe/smteo6.jpg",
    "https://files.catbox.moe/7enu2i.jpg",
    "https://files.catbox.moe/n6hkvd.jpg",
    "https://files.catbox.moe/ej1p7t.jpg",
    "https://files.catbox.moe/fh7vw7.jpg",
    "https://files.catbox.moe/lckxh6.jpg",
    "https://files.catbox.moe/smteo6.jpg",
    "https://files.catbox.moe/7enu2i.jpg",
    "https://files.catbox.moe/n6hkvd.jpg",
    "https://files.catbox.moe/ej1p7t.jpg"
]

@app.on_message(filters.command(["ping", "alive"]) & ~BANNED_USERS)
@language
async def ping_com(client, message: Message, _):
    start = datetime.now()
    response = await message.reply_photo(
        photo=random.choice(Shivi_PIC),
        has_spoiler=True,
        caption=_["ping_1"].format(app.mention),
    )
    pytgping = await Shivi.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await response.edit_text(
        _["ping_2"].format(resp, app.mention, UP, RAM, CPU, DISK, pytgping),
        reply_markup=supp_markup(_),
    )
