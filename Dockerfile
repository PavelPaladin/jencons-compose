FROM python:3.7-slim-stretch

WORKDIR /app
COPY sample_web_pyconsul.py /app

# Install needed stuff
RUN pip install --no-cache-dir flask requests
ENV FLASK_APP=sample_web_pyconsul.py
EXPOSE 5000
CMD ["flask", "run", "--host", "0.0.0.0"]
