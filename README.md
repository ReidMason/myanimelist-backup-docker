# MyAnimeList backup
A program to backup users anime lists from MyAnimeLists locally.\
This is designed to run in a docker container on unraid but can be run as a python app if the config file is edited to remove the use of environment variables.

## Installation to unraid
This is the easiest and recommended way to install.\
Simply add this repo to the templates list and create the container using the new template.

## Alternate installation
Clone the repo and edit `config.py` replacing the environment variable references.

Hard coded example:
```
NUM_BACKUPS = 5
USERNAMES = ['username1', 'username2']
```
You could also use commandline arguments.

Then just run the following commands.
```
$ pip install -r requirements.txt
$ python main.py
```