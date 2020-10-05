FROM python:3.8.5

WORKDIR /app

# Exposing default port for streamlit
EXPOSE 8501

# Install requirements
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Copy necessary files

COPY . /app

ENTRYPOINT [ "python" ]

# Launch app when container is run
CMD streamlit run concrete.py
