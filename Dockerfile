FROM python:3.7

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

# EXPOSE 8080

# ENTRYPOINT ["python3"]

CMD ["python3", "app.py"]
