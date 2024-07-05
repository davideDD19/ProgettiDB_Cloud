FROM python:3.12

WORKDIR /src

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY app.py /src/app.py

COPY templates /src/templates

RUN pip install -r requirements.txt

#Comando per esecuzione applicazione
CMD [ "python", "app.py" ]

