# Weather-Cli

> Command line application to view real time weather.

## Requirements

- python 3.x
- mongodb
- optional
  - docker, docker-compose

## Usage

- clone repository
  - `git clone git@github.com:pavan-n-654/weather-cli.git`
- Setup virtual environment
  - `cd weather-cli/app`
  - `python/3/3.x -m venv .venv`
  - `source .venv/bin/activate`
  - `pip install -r requirements.txt`
- Setup environment variables
  - `cp env_sample .env`
  - make appropriate changes in .env
- Make sure mongodb is up and running on port 27017
  - `python setup.py`
- Run the application
  - `python app.py`
