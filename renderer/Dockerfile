FROM python:3.11.6

WORKDIR /app

COPY requirements.txt /app/

RUN pip3 install -r requirements.txt

COPY src /app/src
COPY tests /app/tests

CMD ["python3", "-m", "unittest", "discover", "tests"]
CMD ["python3", "src/main.py"]

EXPOSE 5000

ENTRYPOINT ["python3", "src/app.py"]
