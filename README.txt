README

============
Description:
============
Heiki is a flask-based web app which allows users to generate Japanese language vocabulary lists from image(s) or document(s). The vocabulary list can be downloaded by the user, and will be in a Word document (.docx) format.

Below is an example of an input image: 
![Japanese input document](https://github.com/dan88934/heiki/blob/main/heiki/static/img/DocumentExample.png)

![Japanese input document](https://github.com/dan88934/heiki/blob/main/DocumentExample.png?raw=true)

Heiki will use OCR to process the text from the above image and will use tokenisation to split the text up into indvidiual words. It will then get the English definition of each word and insert the main Japanese text (usually Kanji), the reading (usually Hiragana), and the English definition into a a table. This produces the vocabulary list that can be seen below:

<img src="https://github.com/dan88934/heiki/blob/main/heiki/static/img/VocabListExample.png" width="128"/>

https://github.com/dan88934/heiki/blob/main/heiki/static/img/VocabListExample.png?raw=true

The program contains a customised version of the Jamdict package (Japanese-to-English dictionary for Python).

There are some sample images and documents in the sample_files folder which can be used to test the application.

============
Installation/Usage (running the code on a Flask development server):
============


1. Install tesseract and ensure that the tesseract executable is in '/usr/local/Cellar/tesseract/'

2. Create a virtual environemnt and then install this projects dependencies (in the requirements.txt) in it.

3. Follow the installation guidance for Sudachipy on https://pypi.org/project/SudachiPy/ 

4. Follow the install instructions for Jamdict on https://pypi.org/project/jamdict/


============
Tests Usage:
============
Two test files are included, test_front_end.py and test_back_end.py. These have been written using Unittest and Selenium. 

To run one of the tests individually, enter 'python -m unittest (file name here)' from the heiki directory. Alternatively, both tests can be ran at once by typing python -m unittest in the heiki directory.
