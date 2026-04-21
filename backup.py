import os
import zipfile
import logging
import argparse
import smtplib
from email.message import EmailMessage
from datetime import datetime

# -------------------------------
# Logging Configuration
# -------------------------------
logging.basicConfig(
    filename="backup.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

# -------------------------------
# Email Alert Function
# -------------------------------
def send_alert(subject, body):
    sender = "your_email@gmail.com"
    password = "your_app_password"  # Use Gmail App Password
    receiver = "your_email@gmail.com"

    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = receiver

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(sender, password)
            smtp.send_message(msg)
    except Exception as e:
        logging.error(f"Failed to send email alert: {str(e)}")

# -------------------------------
# Backup Function
# -------------------------------
def create_backup(source_folder, backup_folder="backups"):
    if not os.path.exists(source_folder):
        logging.error("Source folder does not exist.")
        print("[!] Source folder does not exist.")
        return

    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    zip_filename = f"backup_{timestamp}.zip"
    zip_path = os.path.join(backup_folder, zip_filename)

    print(f"[+] Backing up: {source_folder}")
    print(f"[+] Saving to: {zip_path}")

    logging.info(f"Starting backup of {source_folder}")
    logging.info(f"Saving backup to {zip_path}")

    try:
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as backup_zip:
            for foldername, subfolders, filenames in os.walk(source_folder):
                for filename in filenames:
                    file_path = os.path.join(foldername, filename)
                    arcname = os.path.relpath(file_path, source_folder)
                    backup_zip.write(file_path, arcname)

        print("[✓] Backup completed successfully!")
        logging.info("Backup completed successfully.")

    except Exception as e:
        error_msg = f"Backup failed: {str(e)}"
        logging.error(error_msg)
        print("[!] Backup failed. Check logs.")
        send_alert("Backup Failed", error_msg)

# -------------------------------
# CLI Entry Point
# -------------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Backup a folder into a timestamped ZIP file"
    )

    parser.add_argument(
        "--source",
        required=True,
        help="Folder to backup"
    )

    parser.add_argument(
        "--dest",
        default="backups",
        help="Backup destination folder (default: backups)"
    )

    args = parser.parse_args()

    create_backup(args.source, args.dest)