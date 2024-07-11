FROM python:3.12

WORKDIR /nominativi

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY app.py /nominativi/app.py

COPY templates /nominativi/templates

RUN pip install -r requirements.txt

#Comando per esecuzione applicazione
CMD [ "python", "app.py" ]

