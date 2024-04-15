# Trio Challenge - MailChimp (FastAPI)

This repository has a FastAPI implementation of the MailChimp Technical Challenge from Trio.

This project was developed by Lucas Bittencourt.

## Create the .env file before anything else

The project provides a .env.example to follow good practices, but to make anything work, it's necessary to create a .env file with the following environment variables

> MOCKAPI_BASE_URL=https://challenge.trio.dev/api/v1

## Instructions to run the app using Docker (recommended)

### Build the Docker image

`docker build -t trio-challenge-mailchimp .`

### Run the Docker container

`docker run -d -p 3000:3000 trio-challenge-mailchimp`

## Instructions to run the app locally

### Create a venv and install the requirements

`python -m venv ./env`

> Use the command to activate the env depending on which OS you are using.
>
> Reference: https://docs.python.org/3/library/venv.html#how-venvs-work

`pip install -r ./requirements.txt`

`pip install -r ./requirements.dev.txt`

### Run the app locally

`uvicorn main:app --host localhost --port 3000`

### Development tools

Run the linter: `flake8`

Run the tests: `pytest`
