import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

downloads_folder = 'C:/Users/prayu/Downloads'

file_type_folders = {
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.svg', '.webp'],
    'Videos': ['.mp4', '.mkv', '.avi'],
    'Music': ['.mp3', '.wav', '.aac'],
    'Archives': ['.zip', '.rar', '.tar.gz'],
    'Programs': ['.exe', '.msi', '.dmg'],
}

def organize_files(filename):
    file_path = os.path.join(downloads_folder, filename)
    if os.path.isdir(file_path):
        return

    _, file_extension = os.path.splitext(filename)
    for folder, extensions in file_type_folders.items():
        if file_extension.lower() in extensions:
            target_folder = os.path.join(downloads_folder, folder)
            os.makedirs(target_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(target_folder, filename))
            break

class FileOrganizerHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(downloads_folder):
            organize_files(filename)

if __name__ == '__main__':
    event_handler = FileOrganizerHandler()
    observer = Observer()
    observer.schedule(event_handler, path=downloads_folder, recursive=False)
    observer.start()
    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
