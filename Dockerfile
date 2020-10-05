# coding=utf8
FROM python:3.8.5
ENV LC_ALL=C.UTF-8
WORKDIR /app

# Exposing default port for streamlit
#EXPOSE 8501 #expose is not supported by heroku

# Install requirements
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Copy necessary files

COPY . /app

# Launch app when container is run
CMD streamlit run concrete.py
