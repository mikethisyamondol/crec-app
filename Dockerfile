FROM python:3.9
EXPOSE 8501
WORKDIR /app
RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*
COPY . .
RUN python -m pip install --upgrade pip
RUN  pip3 install -r requirements.txt

ENTRYPOINT ["streamlit", "run", "1_Homepage.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.enableCORS=false", "--server.enableXsrfProtection=false"]