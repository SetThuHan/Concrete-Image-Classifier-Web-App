# The Dockerfile defines the image's environment
# Import Python runtime and set up working directory
FROM python:3.8.5-alpine
WORKDIR /app
ADD . /app

# Install any necessary dependencies
RUN pip install -r requirements.txt

# Open port 80 for serving the webpage
EXPOSE 80

# Run concrete.py when the container launches
CMD streamlit run concrete.py
