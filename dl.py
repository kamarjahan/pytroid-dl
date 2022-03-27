import youtube_dl
import os
from sample_config import Config


video = {}
url = Config.dl_link,
with youtube_dl.YoutubeDL(video) as ydl:
 ydl.download([url])
