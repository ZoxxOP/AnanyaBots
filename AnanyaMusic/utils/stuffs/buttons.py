                                                             
                                                              
  
                                         
                                                       
                                                                
  
                                      
                                                             

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 
from pyrogram.enums import ButtonStyle
import config

class BUTTONS(object):
    ABUTTON = [
    [
        InlineKeyboardButton("˹ sυᴘᴘσʀᴛ ˼", url="https://t.me/AnanyaSupportChat", style=ButtonStyle.PRIMARY),
        InlineKeyboardButton("˹ υᴘᴅᴧᴛєs ˼", url="https://t.me/TeamAnanyaBots", style=ButtonStyle.SUCCESS)
    ],
    [
        InlineKeyboardButton("˹ ❍ᴡηєʀ ˼", user_id=config.OWNER_ID, style=ButtonStyle.PRIMARY),
        InlineKeyboardButton("˹ ʙᴧᴄᴋ ˼", callback_data="settingsback_helper", style=ButtonStyle.DANGER)
    ]
]

    INFO_BUTTON = [
    [
        InlineKeyboardButton("˹ ʀєᴘσ ˼", callback_data="gib_source", style=ButtonStyle.PRIMARY),
        InlineKeyboardButton("˹ ʏᴛ-ᴀᴘɪ ˼", callback_data="bot_info_data", style=ButtonStyle.SUCCESS),
        InlineKeyboardButton("˹ ʟᴧηɢᴜᴧɢє ˼", callback_data="LG", style=ButtonStyle.PRIMARY),
    ],
    [
        
        InlineKeyboardButton("˹ ᴘʀɪᴠᴧᴄʏ ˼", url="https://telegra.ph/Privacy-Policy-10-12-225", style=ButtonStyle.PRIMARY),
        InlineKeyboardButton("˹ ʙᴧᴄᴋ ˼", callback_data="settingsback_helper", style=ButtonStyle.DANGER),
    ]
    ]
    


    INFO_NEW = [
    [
        InlineKeyboardButton("˹ ʙᴧᴄᴋ ˼", callback_data="settings_back_helper", style=ButtonStyle.DANGER)
    ],
    ]
    
    

                                                             
                                                              
  
                                    
                                                 
                                      
                                                             
