FROM rapidfort/flaskapp

WORKDIR /app

COPY ./requirements.txt ./root/requirements.txt

RUN pip install -Ur ./root/requirements.txt

COPY . .

ENV FLASK_RUN_PORT=8080

EXPOSE 8080

WORKDIR /app/app

CMD ["flask", "run"]