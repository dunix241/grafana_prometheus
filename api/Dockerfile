FROM python:slim-bullseye

# Set the working directory
WORKDIR /app

# install dependencies
COPY ./src/requirements.txt /app
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# copy the scripts to the folder
COPY ./src/ /app

# create prometheus config folder
RUN mkdir -p ./prometheus

# start the server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9999"]
