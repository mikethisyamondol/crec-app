FROM python:3.10-slim-buster
COPY . /
RUN pip3 install --upgrade pip
RUN python3 -m pip install --upgrade setuptools
RUN pip3 install -r /requirements.txt
RUN export PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python
EXPOSE 8501
WORKDIR /app
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health
ENTRYPOINT ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
#CMD streamlit run streamlit_app.py