FROM python:3.11

RUN sudo apt-get install python3-libtorrent -y

RUN python3 -m pip install -U -r requirements.txt 

CMD [ "python3" , "-m AAB"]