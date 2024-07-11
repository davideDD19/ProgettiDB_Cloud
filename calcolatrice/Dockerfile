FROM python:3.12

WORKDIR /calcolatrice

COPY requirements.txt /calcolatrice

RUN pip install -r requirements.txt

COPY app.py /calcolatrice

COPY templates /calcolatrice/templates

EXPOSE 5400

CMD ["python","app.py"]