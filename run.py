import time
import schedule
from backup import run_backup

run_backup()

schedule.every().day.at("19:05").do(run_backup)

while True:
  schedule.run_pending()
  time.sleep(60)  # wait one minute
