import os
import zipfile
from datetime import datetime

def create_backup(source_folder, backup_folder="backups"):
    if not os.path.exists(source_folder):
        print("[!] Source folder does not exist.")
        return

    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    zip_filename = f"backup_{timestamp}.zip"
    zip_path = os.path.join(backup_folder, zip_filename)

    print(f"[+] Backing up: {source_folder}")
    print(f"[+] Saving to: {zip_path}")

    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as backup_zip:
        for foldername, subfolders, filenames in os.walk(source_folder):
            for filename in filenames:
                file_path = os.path.join(foldername, filename)
                arcname = os.path.relpath(file_path, source_folder)
                backup_zip.write(file_path, arcname)

    print("[✓] Backup completed successfully!")

if __name__ == "__main__":
    source = input("Enter folder to backup: ").strip()
    create_backup(source)