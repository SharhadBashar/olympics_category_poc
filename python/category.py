import os
import pickle

class Category:
    def __init__(self, text_file, language = 'en', text_data_path = None):
        self.text_data_path = text_data_path if text_data_path else '../data/text/'
        self.category_data_path = '../data/words/'
        
        text = self.load_file(self.text_data_path, text_file)
        words = self.load_file(self.category_data_path, 'olympics_' + language + '.txt', type = 'txt')
        
        check_category = self.check_category(text, words)
        print()
        if check_category:
            print('This is an olympics podcast')
        else:
            print('This is not olympics podcast')
        print()
        
    def load_file(self, folder, file, type = 'pkl'):
        if (type == 'pkl'):
            return pickle.load(open(os.path.join(folder, file), 'rb'))
        else:
            with open(os.path.join(folder, file)) as file:
                words = [line.rstrip().lower() for line in file]  
            file.close()
            words = set(words)
            return words
    
    def check_category(self, text, words):
        for word in words:
            if word in text:
                return True
        return False