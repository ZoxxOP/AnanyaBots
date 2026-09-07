                                                             
                                                              
  
                                         
                                                       
                                                                
  
                                      
                                                             

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from AnanyaMusic import app

@app.on_message(filters.command("privacy"))
async def privacy_command(client: Client, message: Message):
    await message.reply_photo(
          has_spoiler=True,
        photo="https://files.catbox.moe/u140i6.jpg",
        caption="**➻ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴋɪʀᴛɪ ʙᴏᴛѕ ᴘʀɪᴠᴀᴄʏ ᴘᴏʟɪᴄʏ.**\n\n**⊚ ᴄʟɪᴄᴋ ᴛʜᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛʜᴇɴ ꜱᴇᴇ ᴘʀɪᴠᴀᴄʏ ᴘᴏʟɪᴄʏ 🔏**",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("˹ᴘʀᴏᴍᴏ˼", url="https://t.me/Dakshwanshi_Akash?text=𝖧ᴇʏ%20ʙᴀʙʏ%20%20😄%20ɪ%20ᴡᴀɴᴛ%20ᴘᴀɪᴅ%20ᴘʀᴏᴍᴏᴛɪᴏɴ,%20ɢɪᴠᴇ%20ᴍᴇ%20ᴘʀɪᴄᴇ%20ʟɪsᴛ%20😙")]
            ]
        )
    )

                                                             
                                                              
  
                                    
                                                 
                                      
                                                             
