FROM python:alpine3.6

COPY application.py /
RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["-u", "application.py"]
