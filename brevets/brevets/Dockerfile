FROM python:3
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /brevets
WORKDIR /brevets
RUN pip install -r requirements.txt
ENTRYPOINT ["python"] 
CMD ["flask_brevets.py"]

