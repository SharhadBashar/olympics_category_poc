import os
import time
import pickle
import whisper

import warnings
warnings.filterwarnings('ignore')

class Audio_To_Text:
	def __init__(self, audio_file, language = 'en', audio_data_path = None, text_data_path = None):
		self.audio_data_path = audio_data_path if audio_data_path else '../data/audio/'
		self.text_data_path = text_data_path if text_data_path else '../data/text/'
		self.model_types = ['tiny.en', 'tiny']
		
		model_type = 'tiny.en' if language == 'en' else 'tiny'

		if (not os.path.isfile(os.path.join(self.audio_data_path, audio_file))):
			print('Audio file does not exist. Please check again')
			return None
		if (model_type not in self.model_types):
			print('Model does not exist. Please check again')
			return None

		self.model = whisper.load_model(model_type)
		text = self.transcribe(audio_file, self.audio_data_path, model = self.model)

		self.save_text(text['text'].lower(), audio_file.split('.')[0] + '_' + language + '.pkl', self.text_data_path)

	def transcribe(self, audio_file, audio_data_path, model = 'tiny.en'):
		return model.transcribe(os.path.join(audio_data_path, audio_file))

	def save_text(self, text, text_file, text_data_path):
		with open(os.path.join(text_data_path, text_file), 'wb') as file: 
			pickle.dump(text, file) 
		print('Transcribed text saved at:', os.path.join(text_data_path, text_file))
