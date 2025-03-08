# Python Microservice

This microservice is part of the microservice pipline in [inseri](https://github.com/nie-ine/inseri). The service provides the possibility to use/create Python code, use it to transform a response received by an API call into the needed data structure and pass the result to another inseri app.

## Run and Develop Locally

### Install and Run
1. Create a virtual environment
1. Activate your created virtual environment
1. ``pip3 install -r requirements.txt``
1. Run with ``python3 python-task.py``
1. Go to http://localhost:50000

## Run with Docker

1. Build the image: ``[sudo] docker build -t nieine/microservice-python-task .``
1. Run the container: ``[sudo] docker run -p 50000:50000 nieine/microservice-python-task``
1. Go to http://localhost:50000

## Call the Service in a RESTful Way

If the service is running, you can POST a body with JSON data from any application. 

Body:
```
{
  "datafile": "[The name of the JSON file]",
  "data": "[The content of the JSON file]",
  "codefile": "[The name of the Python file]",
  "code": "[The content of the Python file]"
}
```
Response:
```
{
  "output": "...", 
}
```

E.g.: 
```
{
  "datafile":"yourData.json",
  "data":"{\n    \"message\": \"Hello World!\"\n}\n",
  "codefile":"yourCode.py",
  "code":"# Your python 3 code goes here\nimport json\n\ndef show_message(json_file):\n    with open(json_file, 'r') as f:\n        content = json.load(f)\n\n    return content['message']\n\nif __name__ == \"__main__\":\n    print(show_message(\"yourData.json\"))\n"
}

```

```
{
  "output": "Hello World!"
}
```

## Publish on Dockerhub

1. Build the image: ``[sudo] docker build -t nieine/microservice-python-task:YYYY-MM-DD .``
1. Push the image: ``[sudo] docker push nieine/microservice-python-task:YYYY-MM-DD``

## Python Packages

Currently, the below-listed Python packages are installed. To add more packages, add them to the requirements.txt file and re-build the Docker image. 

### Installed Packages

- apturl==0.5.2
- arrow==0.17.0
- asn1crypto==0.24.0
- beautifulsoup4==4.9.3
- Brlapi==0.6.6
- certifi==2020.12.5
- chardet==3.0.4
- click==7.1.2
- command-not-found==0.3
- cryptography==2.1.4
- cupshelpers==1.0
- cycler==0.10.0
- decorator==4.4.2
- defer==1.0.6
- flashtext==2.7
- Flask==1.1.2
- Flask-Cors==3.0.9
- graphviz==0.14
- html5lib==0.999999999
- httplib2==0.9.2
- idna==2.10
- isodate==0.6.0
- itsdangerous==1.1.0
- Jinja2==2.11.2
- joblib==0.17.0
- kazam==1.4.5
- keyring==10.6.0
- keyrings.alt==3.0
- kiwisolver==1.3.1
- language-selector==0.1
- launchpadlib==1.10.6
- lazr.restfulclient==0.13.5
- lazr.uri==1.0.3
- louis==3.5.0
- lxml==4.2.1
- macaroonbakery==1.1.3
- Mako==1.0.7
- MarkupSafe==1.1.1
- matplotlib==3.3.3
- netifaces==0.10.4
- nltk==3.5
- numpy==1.19.4
- oauth==1.0.1
- olefile==0.45.1
- pexpect==4.2.1
- Pillow==8.0.1
- protobuf==3.0.0
- pycairo==1.16.2
- pycrypto==2.6.1
- pycups==1.9.73
- pygobject==3.26.1
- pymacaroons==0.13.0
- PyNaCl==1.1.2
- pyparsing==2.4.7
- pyRFC3339==1.0
- python-apt==1.6.5+ubuntu0.3
- python-dateutil==2.8.1
- python-debian==0.1.32
- pytz==2018.3
- pyxdg==0.25
- PyYAML==3.12
- rdflib==5.0.0
- rdflib-jsonld==0.5.0
- regex==2020.11.13
- reportlab==3.4.0
- requests==2.25.0
- requests-unixsocket==0.1.5
- RestrictedPython==5.0
- SecretStorage==2.3.1
- simplejson==3.13.2
- six==1.15.0
- soupsieve==2.0.1
- system-service==0.3
- systemd-python==234
- textblob==0.15.3
- tqdm==4.54.1
- ufw==0.36
- unattended-upgrades==0.1
- urllib3==1.26.2
- usb-creator==0.3.3
- validators==0.18.1
- wadllib==1.3.2
- webencodings==0.5
- Werkzeug==1.0.1
- xkit==0.0.0
- yattag==1.14.0
- zope.interface==4.3.2
