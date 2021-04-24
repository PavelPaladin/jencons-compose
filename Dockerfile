FROM python:3.7-slim-stretch

WORKDIR /app
COPY pyconsul_task.py /app

# Install needed stuff
RUN pip install --no-cache-dir python-consul 
EXPOSE 8000
CMD ["python3", "/app/pyconsul_task.py"]
