import os
import pickle

class Category:
    def __init__(self, text_file, language = 'en', text_data_path = None):
        self.text_data_path = text_data_path if text_data_path else '../data/text/'
        self.category_data_path = '../data/words/'
        
        text = self.load_file(self.text_data_path, text_file)
        words = self.load_file(self.category_data_path, 'olympics_' + language + '.txt')
        
    def load_file(self, folder, file):
        return set(pickle.load(open(os.path.join(folder, file), 'rb')))
    
    def check_category(self, text, words):
        for word in words:
            if word in text:
                return True
        return False