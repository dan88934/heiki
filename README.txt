README

============
Description:
============
Heiki is a flask-based web app which allows users to generate Japanese language vocabulary lists from image(s) or document(s). The vocabulary list can be downloaded by the user, and will be in a Word document (.docx) format.

The program contains a customised version of the Jamdict package (Japanese-to-English dictionary for Python).

There are some sample images and documents in the sample_files folder which can be used to test the application.

This repository contains the core code which is on the server hosting http://heiki.pythonanywhere.com/.

============
Installation/Usage (running the code on a Flask development server):
============

Note: I have been unable to get this working on Windows 10 as an error occurs when installing a dependency of the docx package. So, please run the program on Mac OS or Linux. Alternatively, you can find the web app version of this app at http://heiki.pythonanywhere.com/ 

1. Install tesseract and ensure that the tesseract executable is in '/usr/local/Cellar/tesseract/'

2. Create a virtual environemnt and then install this projects dependencies (in the requirements.txt) in it.

3. Follow the installation guidance for Sudachipy on https://pypi.org/project/SudachiPy/ 

4. Follow the install instructions for Jamdict on https://pypi.org/project/jamdict/

5. Following the dependencies being installed in a virtual environment, the FLASK_APP environment variable can be set as follows 'export FLASK_APP=Heiki_V1/__init__.py'. 


============
Tests Usage:
============
Two tests are included in the tests folder, test_front_end.py and test_back_end.py. These have been written using Unittest and Selenium. 

To run one of the tests individually, enter 'python -m unittest tests.(file name here)' from the heiki directory. Alternatively, both tests can be ran at once by typing python -m unittest.
