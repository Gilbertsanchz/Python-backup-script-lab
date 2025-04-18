import os
import shutil
from datetime import datetime

# Define source and destination
SOURCE_DIR = os.path.join(os.path.dirname(__file__), "../to_backup")
BACKUP_DIR = os.path.join(os.path.dirname(__file__), "../backups")

# Ensure destination exists
os.makedirs(BACKUP_DIR, exist_ok=True)

# Create backup filename with timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
backup_filename = f"backup_{timestamp}.zip"
backup_path = os.path.join(BACKUP_DIR, backup_filename)

# Perform backup
shutil.make_archive(backup_path.replace(".zip", ""), 'zip', SOURCE_DIR)

print(f"✅ Backup completed: {backup_filename}")

