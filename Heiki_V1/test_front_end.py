import time
import os
import glob
import unittest
from flask import url_for
from selenium import webdriver
from selenium.webdriver.support.ui import Select
# from Heiki_V1.app import app
from app import app
import pathlib
import time

class TestInput(unittest.TestCase): 
    def setUp(self):    
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        self.app = app.test_client()
        # self.driver = webdriver.Chrome('./tests/chromedriver')
        self.driver = webdriver.Chrome('./test_resources/chromedriver')
        self.driver.get('http://127.0.0.1:5000/')
        time.sleep(2)

    def tearDown(self): 
        for filename in os.listdir("./uploaded_files"): #This removes the files which the tests can upload
            r_file = "./uploaded_files/" + filename #Removes all the files in a directory
            os.remove(r_file)

    def test_main_page(self): #1. Test that 200 reponse happens when index is loaded 
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_title_input(self): #Checks to make sure that the user cannot submit form without title value
        #1. count number of files in dir (uploaded_files)
        start_count = 0
        for path in pathlib.Path("./uploaded_files").iterdir():
            if path.is_file():
                start_count += 1
        #2. Enter the data and click submit
        title = self.driver.find_element_by_id("title")
        title.click()
        title.send_keys('')
        time.sleep(1)
        file_type = Select(self.driver.find_element_by_id('file-type'))
        file_type.select_by_value('image')
        file_input = self.driver.find_element_by_id("file")
        absolute_file_path = os.path.abspath("./test_resources/img_04.png")
        file_input.send_keys(absolute_file_path)
        time.sleep(1)
        upload_button = self.driver.find_element_by_id("upload")
        upload_button.click()
        time.sleep(1)
        #3. Count again - test fails if there is a 404 or if an additional file has been added
        finish_count = 0
        for path in pathlib.Path("./uploaded_files").iterdir():
            if path.is_file():
                finish_count += 1
        self.assertEqual(start_count, finish_count) #Test fails if an extra file is added to uploaded_files
        response = self.app.get('/', follow_redirects=True)
        time.sleep(1)
        self.assertEqual(response.status_code, 200) #Test fails if there is a 404 error

    def test_file_input(self): #test that the user cannot submit form without file selected
        #1. count number of files in dir (uploaded_files)
        start_count = 0
        for path in pathlib.Path("./uploaded_files").iterdir():
            if path.is_file():
                start_count += 1
        #2. Enter the data and click submit
        title = self.driver.find_element_by_id("title")
        title.click()
        title.send_keys('d')
        time.sleep(1)
        file_type = Select(self.driver.find_element_by_id('file-type'))
        file_type.select_by_value('image')
        upload_button = self.driver.find_element_by_id("upload")
        upload_button.click()
        time.sleep(1)
        #3. Count again - test fails if there is a 404 or if an additional file has been added
        finish_count = 0
        for path in pathlib.Path("./uploaded_files").iterdir():
            if path.is_file():
                finish_count += 1
        self.assertEqual(start_count, finish_count) #Test fails if an extra file is added to uploaded_files
        response = self.app.get('/', follow_redirects=True)
        time.sleep(1)
        self.assertEqual(response.status_code, 200) #Test fails if there is a 404 error

    def test_all_correct_input(self): #Test that file arrives in output_files when correct input is given
        #1. count number of files in dir (output_files)
        start_count = 0
        for path in pathlib.Path("./output_files").iterdir(): 
            if path.is_file():
                start_count += 1

        #2. Enter the data and click submit
        title = self.driver.find_element_by_id("title")
        title.click()
        title.send_keys('test')
        time.sleep(1)
        file_type = Select(self.driver.find_element_by_id('file-type'))
        file_type.select_by_value('image')
        file_input = self.driver.find_element_by_id("file")
        absolute_file_path = os.path.abspath("./test_resources/img_04.png")
        file_input.send_keys(absolute_file_path)
        time.sleep(1)
        upload_button = self.driver.find_element_by_id("upload")
        upload_button.click()
        time.sleep(1)
        #3. Count again - test fails if there is a 404 or if an additional file has been added
        finish_count = 0
        for path in pathlib.Path("./output_files").iterdir():
            if path.is_file():
                finish_count += 1
        self.assertEqual(finish_count, start_count + 1) #Test fails if an extra file is added to uploaded_files
        response = self.app.get('/', follow_redirects=True)
        time.sleep(1)
        self.assertEqual(response.status_code, 200) #Test fails if there is a 404 error
        #4. Clean up created file from output_files
        for filename in os.listdir("./output_files/"): #This removes the files which the tests can upload
            r_file = "./output_files/" + filename #Removes all the files in a directory
            os.remove(r_file)
            
        #Ideally I would also test if file arrives in user's local downloads folder (since it is possible for the file to be in output_files but still not get served to the user)  
        #Probably could have made use of inheritance in the above code to avoid repetition, following DRY
if __name__ == '__main__':
    unittest.main() 