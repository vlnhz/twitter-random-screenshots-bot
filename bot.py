from configparser import ConfigParser
import time
import tweepy
from tweepy import OAuthHandler
import os
import datetime
import random
import subprocess
import os.path

cwd = os.path.dirname(os.path.realpath(__file__))
os.chdir(cwd)

pathConfig = cwd + '\\config.ini'

parser = ConfigParser()
parser.read(pathConfig)

consumerKey = parser.get('config', 'API_KEY')
consumerSecret = parser.get('config', 'API_KEY_SECRET')
accessKey = parser.get('config', 'ACCESS_TOKEN')
accessSecret = parser.get('config', 'ACCESS_TOKEN_SECRET')

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessKey, accessSecret)
api = tweepy.API(auth)

def generate_thumbnail(in_filename, out_filename, timess):
        os.system(f"ffmpeg -ss {timess} -copyts -i {in_filename} -vf subtitles={nombreSubtitulos(in_filename)} -vframes 1 {out_filename}")

def get_length(input_video):
    result = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', input_video], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return float(result.stdout)

def convert(sec):
   return "{:0>8}".format(str(datetime.timedelta(seconds=round(sec))))    

def nombreSubtitulos(filename):
    nombreSinFormato = (filename.split('.')[0]).split('/')[-1]
    subtitleFolder = parser.get('config', 'subtitlePath')
    subtitlePath = subtitleFolder + nombreSinFormato + '.srt'
    return subtitlePath

def post_frame():
    path = parser.get('config', 'path')

    files = os.listdir(path)
    index = random.randrange(0, len(files)) #select random episode from folder
    path_new = path +str(files[index])#get video path

    duracion = get_length(path_new)

    frame_seq = random.uniform(2, duracion) #select random timestamp from video

    generate_thumbnail(path_new, 'captura.png', frame_seq) #generate screenshot

    media = api.media_upload('captura.png')#, tweetText)  also can post text

    api.update_status(status = '', media_ids=[media.media_id]) #tweet screenshot

    os.remove('captura.png') #then, after its posted, the algorithm removes it to avoid unnecessary memory use.

if(parser.get('config', 'alwaysRunning').strip().lower() == 'true'):
    tiempoEspera = int(parser.get('config', 'tiempoEspera'))
    while(True):
        print("Twitteando captura...")
        post_frame()
        print("Captura twitteada")
        print("Esperando {} segundos para volver a twittear...".format(tiempoEspera))
        time.sleep(tiempoEspera) #en segundos
else:
    print("Twitteando captura...")
    post_frame()
    print("Captura twitteada")