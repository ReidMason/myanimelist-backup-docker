from utils import log
import utils
from colorama import Back
from config import USERNAMES


def run_backup():
    log('MyAnimeList backup started', Back.CYAN)
    for username in USERNAMES:
        log(f'Processing {username}', Back.CYAN)
        # Get current list data for user
        try:
            new_list_data = utils.get_anime_list_data(username)

        except AttributeError:
            # Failed to obtain list data continue to next user
            log("Error: Unable to obtain anime list data", Back.RED)
            continue

        # Get most recent backup
        recent_backup = utils.get_recent_backup(username)

        # Check if the recent backup needs updating
        if new_list_data == recent_backup:
            continue

        # Save the new anime data
        utils.backup_anime_list(new_list_data, username)
        log(f"Backup for {username} complete", Back.GREEN)
