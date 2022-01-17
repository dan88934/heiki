FROM ubuntu:18.04

# STEP 2: Copy the source code in the current directory to the container.  Store it in a folder named /app.
ADD . /app

# STEP 3: Set working directory to /app so we can execute commands in it
WORKDIR /app


#Set timezone to fix hang on build issue
ENV TZ=Europe/London
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update \
    && apt-get install tesseract-ocr -y \
    python3.10 \
    python-setuptools \
    python3-pip \
    && apt-get clean \
    && apt-get autoremove



#FROM tiangolo/uwsgi-nginx-flask:python3.8-alpine:3.11
#RUN apk --update add bash nano
ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static



#Install Ruby (required for installing homebrew) 
#RUN apk upgrade
#RUN apk add ruby=2.6.8-r0
#RUN apk add ruby
#Set Ruby path

#Install git (required for installing homebrew)
#RUN apk add git

#Install Homebrew (required for installing Tesseract)
#RUN /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
#Install Tesseract
#RUN brew install tesseract-lan

#Install Pillow (Ubuntu version)
#RUN apt-get install -y python3-imaging
RUN apt-get install -y python3-pil

#Install wheel
RUN pip3 install -U wheel

#Install Jamdict
#RUN pip3 install --upgrade jamdict jamdict-data
RUN pip3 install --upgrade jamdict

#Install Jamdict DB data (if required) 
#COPY ./jamdict-data /.jamdict/data/

#Install requirements.txt
#COPY ./requirements.txt /var/www/requirements.txt
#RUN pip3 install -r /var/www/requirements.txt
RUN pip3 install -r requirements.txt

#Add Jamdict DB to appropriate path 
#ADD ./JPVL_jamdict/data/jamdict.db /root/.jamdict/data
#Try moving all the data files into the root data folder 
#. /Users/dan/.jamdict/data/jamdict.db
ADD ./JPVL_jamdict/data /root/.jamdict

RUN pip3 install gunicorn[gevent]


EXPOSE 5000 

CMD gunicorn --worker-class gevent --workers 8 --bind 0.0.0.0:5000 wsgi:app --max-requests 10000 --timeout 5 --keep-alive 5 --log-level info



#CMD ["/bin/bash"]
