FROM python:3.12

WORKDIR /DB_Presenze

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5200

CMD ["python", "app.py"]
