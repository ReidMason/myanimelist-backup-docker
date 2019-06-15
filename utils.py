import json
import os

import requests
from datetime import datetime
from colorama import Style, Fore
from bs4 import BeautifulSoup
from config import BACKUP_PATH, NUM_BACKUPS


def log(text, *style):
  """ Logs text with a specified style using colorama styles """
  text = ((''.join(style) + text) + Style.RESET_ALL).replace('\r', '').replace('\n', '')
  print(datetime.today().strftime('%d-%m-%Y %H:%M:%S') + ' ' + text)


def get_date():
  return str(datetime.now()).replace(':', '.')


def get_anime_list_data(username):
  url = f'https://myanimelist.net/animelist/{username}'

  r = requests.get(url)
  soup = BeautifulSoup(r.content, 'lxml')

  anime_list_data = soup.find('table', {'class': 'list-table'}).get('data-items')
  return json.loads(anime_list_data)


def get_previous_backup(username):
  path = os.path.join(BACKUP_PATH, username)

  # Check that the backup folder exists
  if not os.path.exists(path):
    log('No backups from this user. Creating folder', Fore.YELLOW)
    os.mkdir(path)
    return None

  backups = os.listdir(os.path.join(path))
  # If there are no backups return None
  if len(backups) < 1:
    return None

  # Get the data from the last backup
  with open(os.path.join(path, backups[-1]), 'r') as f:
    return json.load(f)


def backup_anime_list(data, username):
  path = os.path.join(BACKUP_PATH, username)

  # Create save path
  filename = f"MyAnimeListBackup {get_date()} - {username}.json"
  filepath = os.path.join(path, filename)

  # Save the file
  log(f'Saving backup to {filepath}', Fore.CYAN)
  with open(filepath, 'w') as f:
    json.dump(data, f)

  # Remove old backups
  remove_old_backups(path)


def remove_old_backups(path):
  log(f'Checking for old backups', Fore.CYAN)
  backups = os.listdir(path)
  for i in range(0, len(backups) - NUM_BACKUPS):
    log(f'Removing old backup', Fore.CYAN)
    os.remove(os.path.join(path, backups.pop(0)))
