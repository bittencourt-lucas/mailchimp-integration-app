# MailChimp Integration (FastAPI)

This repository has a FastAPI implementation of a MailChimp Integration.

This project was developed by Lucas Bittencourt.

## Create the .env file before anything else

The project provides a .env.example to follow good practices, but to make anything work, it's necessary to create a .env file with the following environment variables

> MOCKAPI_BASE_URL=https://challenge.trio.dev/api/v1
>
> MAILCHIMP_API_KEY=7cda141bb55b4455c292b50c80dda1b2-us18
>
> MAILCHIMP_SERVER_PREFIX=us18
>
> MAILCHIMP_API_BASE_URL=https://${MAILCHIMP_SERVER_PREFIX}.api.mailchimp.com/3.0

## Instructions to run the app using Docker (recommended)

### Build the Docker image

`docker build -t mailchimp-integration-app.`

### Run the Docker container

`docker run -d -p 3000:3000 mailchimp-integration-app`

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

Run the tests with coverage report: `pytest -vv --cov=src --cov-report=term-missing .\tests\`

### Coverage reports

```
---------- coverage: platform win32, python 3.12.1-final-0 -----------
Name                                                                    Stmts   Miss  Cover
-------------------------------------------------------------------------------------------
src\__init__.py                                                             0      0   100%
src\application\__init__.py                                                 0      0   100%
src\application\models\__init__.py                                          0      0   100%
src\application\models\contact.py                                           5      0   100%
src\application\models\mailchimp_contact.py                                 5      0   100%
src\application\models\mailchimp_list.py                                    4      0   100%
src\application\models\mockapi_contact.py                                   8      0   100%
src\application\models\sync_contacts_response.py                            5      0   100%
src\application\models\sync_output.py                                       6      0   100%
src\application\services\__init__.py                                        0      0   100%
src\application\services\integration\__init__.py                            0      0   100%
src\application\services\integration\sync_mockapi_contacts_service.py      33      3    91%
src\application\services\mailchimp\__init__.py                              0      0   100%
src\application\services\mailchimp\add_members_to_list_service.py          21      0   100%
src\application\services\mailchimp\get_lists_service.py                    16      0   100%
src\application\services\mockapi\__init__.py                                0      0   100%
src\application\services\mockapi\get_contacts_service.py                   16      4    75%
src\infrastructure\__init__.py                                              0      0   100%
src\infrastructure\clients\__init__.py                                      0      0   100%
src\infrastructure\clients\http_client.py                                  26      0   100%
src\infrastructure\externals\__init__.py                                    0      0   100%
src\infrastructure\externals\mailchimp_api_client.py                       33      0   100%
src\infrastructure\externals\mockapi_client.py                             27      3    89%
src\routers\__init__.py                                                     0      0   100%
src\routers\router.py                                                      14      3    79%
-------------------------------------------------------------------------------------------
TOTAL                                                                     219     13    94%
```
