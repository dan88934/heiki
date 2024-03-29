 FROM ubuntu:18.04

#Copy the source code in the current directory to the container.  Store it in a folder named /app.
ADD . /app

#Set working directory to /app so we can execute commands in it
WORKDIR /app

#Set timezone to fix hang on build issue
ENV TZ=Europe/London
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

#Install Tesseract (OCR), Python3, and Pip
RUN apt-get update \
    && apt-get install tesseract-ocr -y \
    python3.10 \
    python-setuptools \
    python3-pip \
    && apt-get clean \
    && apt-get autoremove

#Set static URL and path
ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static

#Install Pillow (Ubuntu version)
RUN apt-get install -y python3-pil

#Install wheel
RUN pip3 install -U wheel

#Install Jamdict
RUN pip3 install --upgrade jamdict

#Install other requirements
RUN pip3 install -r requirements.txt

#Add Jamdict DB to appropriate path 
ADD ./JPVL_jamdict/data /root/.jamdict/data

#Add Jamdict config file to appropriate directory 
ADD ./JPVL_jamdict/config.json /root/.jamdict

#Add tessdata files to correct path - for Tesseract OCR 
ADD ./tesseract/tessdata /usr/share/tesseract-ocr/4.00/tessdata

#Install Gunicorn
RUN pip3 install gunicorn[gevent]

#Expose port 
EXPOSE 5050 

#Start server
CMD gunicorn --timeout 1000 --worker-class gevent --workers 8 --bind 0.0.0.0:5050 wsgi:app --max-requests 10000 --keep-alive 5 --log-level info

