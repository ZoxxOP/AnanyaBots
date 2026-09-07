import re

from pyrogram import filters
from pyrogram.types import Message

from AnanyaMusic import app
from AnanyaMusic.plugins.misc.guest import ADD_ME_PROMO_TEXT, _add_me_markup

                                            
                              
                                            
                                                                   
                                                              
 
                                                                    
                                                                     
                                                                  
                                                              
                                                                  

_MENTION_PATTERN = re.compile(
    r"(?<![\w])@" + re.escape(app.username) + r"(?![\w])",
    flags=re.IGNORECASE,
)


@app.on_message(filters.text & ~filters.bot & ~filters.via_bot, group=7)
async def member_chat_username_mention(client, message: Message):
    text = message.text or ""
    if not _MENTION_PATTERN.search(text):
        return

    try:
        await message.reply_text(
            ADD_ME_PROMO_TEXT,
            reply_markup=_add_me_markup(),
            disable_web_page_preview=True,
        )
    except Exception as e:
        print(f"Member-chat mention reply error: {e}")
