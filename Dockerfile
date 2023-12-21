FROM python:3.8.2
LABEL description="text to sql conversion service"
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app/
EXPOSE 8000
CMD ["uvicorn",  "server:app", "--port", "8000", "--reload" ]  