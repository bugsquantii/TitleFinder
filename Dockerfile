#Python
FROM python:3.11-slim

#Set the working directory
WORKDIR /app

#Copy files to app folder
COPY ./app /app

#Install dependencies
RUN pip install -r requirements.txt

#Expose port 8000
EXPOSE 8000

#Start the server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]