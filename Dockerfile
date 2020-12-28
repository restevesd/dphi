FROM python:3.8-slim-buster

# install build utilities
RUN apt-get update && \
	apt-get install -y gcc make apt-transport-https ca-certificates build-essential

# Copy all the files from the project’s root to the working directory
COPY . /app
WORKDIR  /app

# Installing python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENTRYPOINT [ "python3" ]
CMD [ "app.py","run","--host","0.0.0.0"]