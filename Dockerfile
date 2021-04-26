FROM python:3.7-slim-stretch

WORKDIR /app
COPY sample_web_pyconsul.py /app

# Install needed stuff
RUN pip install --no-cache-dir flask requests
EXPOSE 5000
CMD ["python3", "/app/sample_web_pyconsul.py"]
