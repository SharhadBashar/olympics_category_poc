import os
import sys
import time

from att import Audio_To_Text
from category import Category

try:
    language = sys.argv[1].lower()
except IndexError:
    print('No language specified. Please pass -en for English or -fr for French. Type -h for information')
    exit()

if (language == '-h'):
    print()
    print('Instructions:')
    print('Pass two commands')
    print('1. First is the language. We only support English and French for now.')
    print('   type -en for English, and -fr fof French.')
    print('2. Next add the name of the audio file, with the extension.')
    print('System will analyze the audio and determine if its an Olympics category or not.')
    print()
    exit()





if (language == '-en'):
    try:
        audio_file = sys.argv[2].lower()
    except IndexError:
        print('No audio found. Please pass an audio file')
        exit()
        
    start = time.time()
    Audio_To_Text(audio_file, language = 'en')
    print('Finished transcribing in {} s'.format(round(time.time() - start, 2)))
    Category(text_file = audio_file.split('.')[0] + '_en.pkl', language = 'en')
    
elif (language == '-fr'):
    try:
        audio_file = sys.argv[2].lower()
    except IndexError:
        print('No audio found. Please pass an audio file')
        exit()

    start = time.time()
    Audio_To_Text(audio_file, language = 'fr')
    print('Finished transcribing in {} s'.format(round(time.time() - start, 2)))
    Category(text_file = audio_file.split('.')[0] + '_fr.pkl', language = 'fr')
    
else:
    print('Unknown language. Please pass -en for English or -fr for French. Type -h for information')
    exit()