FROM python:3
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn

COPY app/. .

# CMD ["python", "-m", "uvicorn", "main:app"]
CMD ["gunicorn", "-k" , "uvicorn.workers.UvicornWorker", "main:app", "--bind", "0.0.0.0"]
EXPOSE 8000