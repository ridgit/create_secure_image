FROM python:alpine3.6

COPY application.py /
RUN pip install flask==0.10.1

ENTRYPOINT ["python"]
CMD ["-u", "application.py"]
