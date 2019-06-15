import os

# Setup environment variables
NUM_BACKUPS = int(os.environ['NUM_BACKUPS'])
USERNAMES = [x.strip() for x in os.environ['USERNAMES'].split()]
# NUM_BACKUPS = 5
# USERNAMES = ['SkippyTheSnake']

BACKUP_PATH = 'backups'
