FROM python

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . /usr/src/app/
RUN pip3 install setuptools
RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install --upgrade lxml

CMD [ "python3", "python-task.py" ]
