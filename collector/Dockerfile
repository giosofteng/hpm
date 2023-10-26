FROM python:3.11.6

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt

CMD ["python3", "-m", "unittest", "discover", "tests"]

ENTRYPOINT ["python3", "src/main.py"]
