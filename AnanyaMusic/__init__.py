                                                             
                                                              
  
                                         
                                                       
                                                                
  
                                      
                                                             

from AnanyaMusic.core.bot import Shivi
from AnanyaMusic.core.dir import dirr
from AnanyaMusic.core.git import git
from AnanyaMusic.core.userbot import Userbot
from AnanyaMusic.misc import dbb, heroku
from .logging import LOGGER

dirr()
      
dbb()
heroku()

app = Shivi()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()

                                                             
                                                              
  
                                    
                                                 
                                      
                                                             
