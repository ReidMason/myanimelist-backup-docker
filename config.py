import os

# Setup environment variables
NUM_BACKUPS = os.environ['NUM_BACKUPS']
USERNAMES = [x.strip() for x in os.environ['USERNAME'].split()]
# NUM_BACKUPS = 5
# USERNAMES = ['SkippyTheSnake']

BACKUP_PATH = 'data'
