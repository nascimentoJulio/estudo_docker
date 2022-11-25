FROM python:3

RUN apt-get update  
RUN apt-get install -y python3-pip python-dev  

WORKDIR /app

RUN pip install Flask
RUN pip install requests
RUN pip install Flask psycopg2-binary

COPY . .

EXPOSE 5000

CMD ["python", "./app.py"]