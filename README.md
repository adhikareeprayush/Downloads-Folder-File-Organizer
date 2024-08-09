# Downloads Folder File Organizer

This Python script automatically organizes files in your Downloads folder based on their file types. It monitors the Downloads folder for changes and moves files into designated subfolders whenever a new file is added or an existing file is modified.

## Features

- **Automatic Organization**: Automatically moves files into subfolders based on their file extension.
- **Customizable Folders**: Predefined folders for various file types (e.g., Documents, Images, Videos) are automatically created.
- **Real-time Monitoring**: Monitors the Downloads folder for changes and organizes files in real-time.

## Folder Structure

The script organizes files into the following folders:

- **Documents**: `.pdf`, `.docx`, `.txt`, `.xlsx`
- **Images**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.svg`, `.webp`
- **Videos**: `.mp4`, `.mkv`, `.avi`
- **Music**: `.mp3`, `.wav`, `.aac`
- **Archives**: `.zip`, `.rar`, `.tar.gz`
- **Programs**: `.exe`, `.msi`, `.dmg`

## Installation

1. **Clone the repository** or download the script file.

2. **Install the required Python package**:

   ```bash
   pip install watchdog
   ```

3. **Update the `downloads_folder` path**:

   - By default, the script is set to monitor the `C:/Users/prayu/Downloads` folder.
   - Update the `downloads_folder` variable in the script if your Downloads folder is located elsewhere.

## Usage

1. **Run the script**:

   ```bash
   python file_organizer.py
   ```

2. **Let it run in the background**:

   - The script will continuously monitor your Downloads folder and automatically organize files as they are added or modified.

3. **Stop the script**:

   - To stop the script, press `Ctrl + C` in the terminal where the script is running.

## Customization

- You can add or remove file extensions and their corresponding folders by modifying the `file_type_folders` dictionary in the script.

## Troubleshooting

- Ensure that the `watchdog` package is installed.
- Verify that the `downloads_folder` path is correct.
- Ensure that the script has permission to move files in the Downloads folder.

## Contributing

Feel free to contribute to this project by submitting issues or pull requests.

