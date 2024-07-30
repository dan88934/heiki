import unittest
from flask import Flask
from process_file import get_japanese_only, tokenize_into_words, list_concat, remove_duplicate_items, remove_irrelevant_characters, remove_single_katakana, remove_single_hiragana, add_items_to_original_word_list, get_reading_and_eng
from app import app
from io import BytesIO, StringIO


#The methods in the below class test the functions in file_processing.py
class TestFileProcessing(unittest.TestCase): 
    def test_get_japanese_only(self): 
        #Test that it removes eng and symbols from the string
        string = 'Hello今日、!!日本語を勉強した。^]'
        result = get_japanese_only(string)
        self.assertEqual(result, '今日日本語を勉強した')

    def test_tokenize_into_words(self):
        #Test that it takes each word from the sentence and creates a list of these words (in the mannar desired)
        string = '今日日本語を勉強した'
        result = tokenize_into_words(string)
        self.assertEqual(result, ['今日','日本','語','を','勉強','する', 'た']) #We can see that due to the Sudachipy settings, the past verb is changed to the root dict form

    # def test_list_concat(self):
    #     #This joins two list together - unsure of how to test it 
    #     master_list = [['今日','日本','語','を','勉強','する', 'た'], ['カタカナ','必死','避難']]
    #     result = list_concat(master_list)
    #     self.assertEqual(result, ['今日','日本','語','を','勉強','する', 'た','カタカナ','必死','避難'])
    
    def test_remove_duplicate_items(self):
        #Test that this removes all but the first instance of the word
        test_list = ['今日','日本','語','語','勉強','を','勉強','する', 'た']
        result = remove_duplicate_items(test_list)
        self.assertEqual(result, ['今日','日本','語','勉強','を','する', 'た']) 

    def test_remove_irrelevant_characters(self):
        #Test that this removes characters which do not have a meaning on their own
        test_list = ['今日','日本','語','ます','勉強','を','する','って']
        result = remove_irrelevant_characters(test_list)
        self.assertEqual(result, ['今日','日本','語','勉強','を','する'])
    
    def test_remove_single_katakana(self):
        #Test that all single katanaka characters are removed from the list (they do not have a meaning on their own)
        test_list = ['今日','日本','語','勉強','く','を','する', 'コ']
        result = remove_single_katakana(test_list)
        self.assertEqual(result, ['今日','日本','語','勉強','を','する'])

    def test_remove_single_hiragana(self):
        #Test that all single hiragana characters are removed from the list (they do not have a meaning on their own)
        test_list = ['今日','日本','語','は','勉強','を','する', 'め']
        result = remove_single_hiragana(test_list)
        self.assertEqual(result, ['今日','日本','語','勉強','する'])

    def test_add_items_to_original_word_list(self):
        #Test that words in list passed in as argument are all appended to the new list
        test_list = ['今日','日本','語','勉強','する']
        result = add_items_to_original_word_list(test_list)
        self.assertEqual(result, ['今日','日本','語','勉強','する'])

    # def test_get_reading_and_eng(self):
           #This checks that the output contains an english definition matching to one of the JP words in list - unsure of how to carry this out
    #     test_list = ['今日','日本','語','勉強','する']
    #     # test_string = 'Today'
    #     result = get_reading_and_eng(test_list)
    #     self.assertIn('language', result) #'語' means 'language' (usually when added on to the name of a country i.e. イタリア語)


class TestInput(unittest.TestCase): 
    #Setup code 
    def setUp(self):    
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        self.app = app.test_client()
    #Helper method
    def submit(self, title, filetype, file): #This will post the data which is passed into the tests below
        return self.app.post('/', 
                                data=dict(title=title, filetype=filetype, file=file),
                                follow_redirects=True
        )
    #Test cases 
    def test_main_page(self): 
        #test that 200 reponse happens when index is loaded 
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    #The below two are covered more comprehensively in the front_end_test file using Selenium
    def test_title_input(self): 
        #Checks to make sure that the user cannot submit form without title value
        response = self.submit('', 'Image', './sample_files/IMG_2443.PNG')
        self.assertNotEqual(response.status_code, 200)

    def test_file_input(self): 
        #test that the user cannot submit form without file selected
        response = self.submit('Test', 'Image', '')
        self.assertNotEqual(response.status_code, 200)


    #One situation which is not error handled in the code is a situation in which the user selects the wrong file type 
    #Another not handled situation would involve the user selecting a file and then deleting the file from the directory in question before posting the form by clicking 'submit'


if __name__ == '__main__':
    unittest.main()