import json

from colorama import Style, Back, Fore, init
import utils
from utils import log
from config import USERNAMES, NUM_BACKUPS


def run_backup():
  # Initialise colorama
  init()
  log('----- MyAnimeList backup started  -----', Back.CYAN, Fore.BLACK)

  for i, username in enumerate(USERNAMES):
    # Get anime list data from MyAnimeList
    log(f'[{i + 1}/{len(USERNAMES)}] Getting list data for {username}', Fore.BLACK, Back.CYAN)
    anime_list_data = utils.get_anime_list_data(username)
    log('List data obtained', Fore.GREEN)

    # Check if backup is required
    log(f'Checking if backup is required for {username}', Fore.CYAN)
    if utils.get_previous_backup(username) != anime_list_data:
      utils.backup_anime_list(anime_list_data, username)
    log(f'Done {username}')

  log('Finished backups', Back.GREEN)
