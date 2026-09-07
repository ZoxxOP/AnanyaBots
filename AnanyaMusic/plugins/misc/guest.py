from pyrogram.enums import ParseMode
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQueryResultArticle,
    InputTextMessageContent,
    Message,
)

from AnanyaMusic import app


                                                            
               
                                                            

ADD_ME_PROMO_TEXT = (
    "❖ <a href=\"https://t.me/{username}\">˹{name}˼ ♪</a> — <b>𝐘ᴏᴜʀ 𝐏ʀᴇᴍɪᴜᴍ 𝐌ᴜsɪᴄ 𝐒ᴛʀᴇᴍᴀʀ 𝐁ᴏᴛ 🍂</b>\n\n"
    
    "<blockquote><b>▸ 𝐅ᴀsᴛ • 𝐋ᴀɢ 𝐅ʀᴇᴇ • 𝐍ᴏ 𝐀ᴅs 🍂</b>\n"
    "<b>▸ 𝐀ᴜᴛᴏ-𝐏ʟᴀʏ • 𝐀ᴜᴅɪᴏ • 𝐕ɪᴅᴇᴏ 🎥</b></blockquote>\n\n"
    
    "<b>◼️ 𝐀ᴅᴅ</b> <a href=\"https://t.me/{username}\">˹{name}˼ ♪</a> <b>𝐓ᴏ 𝐘ᴏᴜʀ 𝐆ʀᴏᴜᴘ & 𝐄ɴᴊᴏʏ 𝐇ɪɢʜ 𝐐ᴜᴀʟɪᴛʏ 𝐒ᴏɴɢ ❄️</b>"
)


                                                            
         
                                                            

def _add_me_markup(username: str):

    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="✙ ʌᴅᴅ ϻє ɪη ʏσυʀ ɢʀσυᴘ ✙",
                    url=f"https://t.me/{username}?startgroup=true",
                )
            ]
        ]
    )


                                                            
            
                                                            

@app.on_guest_message()
async def guest_username_mention(_, message: Message):

    guest_query_id = getattr(
        message,
        "guest_query_id",
        None,
    )

    if not guest_query_id:
        return

    try:

                                                            
                              
                                                            

        me = await app.get_me()

                        
        name = me.first_name or "Music Bot"

        if me.last_name:
            name = f"{name} {me.last_name}"

                      
        username = me.username

        if not username:
            return

                                                            
                        
                                                            

        promo_text = ADD_ME_PROMO_TEXT.format(
            name=name,
            username=username,
        )

                                                            
                  
                                                            

        keyboard = _add_me_markup(username)

                                                            
                       
                                                            

        result = InlineQueryResultArticle(
            title=f"❖ {name} ♪",
            description=f"@{username} • Add Me In Your Group 🎶",
            thumb_url="https://files.catbox.moe/qv2ob4.jpg",

            input_message_content=InputTextMessageContent(
                message_text=promo_text,
                parse_mode=ParseMode.HTML,
                disable_web_page_preview=True,
            ),

            reply_markup=keyboard,
        )

                                                            
                            
                                                            

        await app.answer_guest_query(
            guest_query_id,
            result=result,
        )

    except Exception as e:

        print(
            f"Guest Mode Error: {type(e).__name__}: {e}"
        )
        
