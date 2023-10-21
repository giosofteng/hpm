FROM python:3.12.0

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY src /app/src
COPY tests /app/tests

CMD ["python", "-m", "unittest", "discover", "tests"]

ENTRYPOINT ["python", "src/main.py"]
