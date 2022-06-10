
     __      __                  __    __                        _________   __    __ 
    /  \    /  \  ____  _____  _/  |_ |  |__    ____ _______     \_   ___ \ |  |  |__|
    \   \/\/   /_/ __ \ \__  \ \   __\|  |  \ _/ __ \\_  __ \    /    \  \/ |  |  |  |
    \        /  \  ___/  / __ \_|  |  |   Y  \\  ___/ |  | \/    \     \____|  |__|  |
    \__/\  /    \___   >(____  /|__|  |___|  / \___  >|__|        \______  /|____/|__|
         \/         \/       \/            \/      \/                    \/


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

### Alternatively with docker

- clone repository
- Setup docker
  - `cd weather-cli/app`
  - `source script.sh`
- Build and run the application
  - `run_db`
  - `build_app`
  - `run_app`

  - > Note at this point if the mongodb is newly created or recreated
    - In a separate terminal  `cd PATH_TO/weather-cli/app`
    - `source script.sh`
    - `setup_db`
    - inside docker container shell `python setup.py`
  - In the `run_app` executed terminal the app will be waiting for user input

> Checkout [report.md](https://github.com/pavan-n-654/weather-cli/blob/main/report.md)
