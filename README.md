# SkyHub

Resize photos – SkyHub challenge

## Mission
1. Consume a webservice endpoint (http://54.152.221.29/images.json) that returns a JSON of
photos. There are 10 photos.
2. Generate three different formats for each photo. The dimensions are: small (320x240),
medium (384x288) and large (640x480).
3. Write a webservice endpoint that lists (in JSON format) all the ten photos with their
respective formats, providing their URLs.

You should use a non-relational database (MongoDB is preferred).


## Instalation 
The requirements can be supplied with pip in python 3. Is encouraged use virtualenv.
```
  pip install -r requirements.txt
```
It's necessary mongoDB service running. Modify config.cfg file to configure database connection.


## Ruunning
You can run use the follow command
```
  python app.py
```
Now, you access the system using: (http://127.0.0.1:5000/)

To request all photos resized by program: (http://127.0.0.1:5000/photo/)

## Explain
First step, when program is running, is get urls from webservice with photos. With this urls, the system get this photos and resize it. This resized photos are saved in a directory called 'photo' in system root directory and your metadatas is saved in mongoDB. 

After photo handling, the Flask is started with two endpoints: '/photo/' and '/photo/<name>'

1. The endpoint '/photo/' return a list of photos with your origin url and with 3 new dimenssion. 
The dimenssions are:  small (320x240), medium (384x288) and large (640x480).
2. The endpoint '/photo/<name>' return a photo in a new dimenssion to download.

In this case, I chose save files in filesystem and not in mongoDB because I prefer something more simple and faster. 

## Tests

You can run tests using:
```
  python TestPhotoMisc.py
  python TestWebservice.py
```
