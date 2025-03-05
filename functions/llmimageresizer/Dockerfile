#This Dockerfile creates a Docker Image with 'python:3.7-slim' as the base image. It then sets '/app' as working directories and copies 'requirements.txt' and 'app.py' into it. 
#Afterwards, it installs the python dependencies using pip, exposes the port '5000', and finally runs the app.py script.
FROM python:3.7-slim
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev

WORKDIR /app

COPY ./requirements.txt /app
RUN pip install -r requirements.txt

COPY ./app.py /app
EXPOSE 5000

CMD ["python", "app.py"]
