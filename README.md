# Python Backup Automation Script

## 📌 Overview

This project is a Python-based automation tool that creates compressed backups of a specified folder.
Each backup is stored as a timestamped ZIP file, making it easy to manage and track versions over time.

---

## ⚙️ Features

* 📂 Automatically backs up any folder
* 🕒 Generates timestamped ZIP files
* 📦 Uses compression to save storage space
* 🛠 Creates backup directory if it doesn’t exist
* ⚡ Simple and lightweight (no external libraries required)

---

## 🧠 How It Works

The script:

1. Takes a folder path as input
2. Creates a timestamp (YYYY-MM-DD_HH-MM-SS)
3. Compresses all files into a ZIP archive
4. Stores it in a `backups/` directory

---

## ▶️ Usage

Run the script:

```bash
python backup.py
```

Enter the folder path when prompted:

```
Enter folder to backup: C:\Users\YourName\Documents
```

---

## 📁 Project Structure

```
backup-automation/
│── backup.py
│── backups/
│── .gitignore
```

---

## 🛡️ Future Improvements

* Add scheduled backups (Task Scheduler / Cron)
* Add logging functionality
* Add encryption for secure backups
* Add cloud upload (AWS S3 / Google Drive)

---

## 👨‍💻 Author

Daniel Nwachukwu
