# start from an official image
FROM python:3.6

# arbitrary location choice: you can change the directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
# we use --system flag because we don't need an extra virtualenv
RUN apt-get update && apt-get install -y netcat

RUN mkdir staticfiles


RUN pip install pipenv 
COPY ./Pipfile /usr/src/app/Pipfile
RUN pipenv install --skip-lock --system --dev

# copy entrypoint.sh
COPY ./entrypoint.sh .

# copy project
COPY . .

# run entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]


