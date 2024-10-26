''' This File Organizer is a Python script that automatically organizes files in a specified
directory based on their types, such as images, documents, audio, and video.
 Users can upload various files like .jpg, .pdf, .mp3, and .zip, and the script
 will create corresponding folders to categorize them. This tool enhances file management,
 making it easier to locate and access files efficiently.'''



import os
import shutil

def organize_files(directory):
    # List of file extensions and corresponding folder names
    extensions = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents': ['.pdf', '.docx', '.txt', '.pptx'],
        'Audio': ['.mp3', '.wav', '.ogg'],
        'Videos': ['.mp4', '.mkv', '.avi'],
        'Archives': ['.zip', '.tar', '.rar']
    }

    # Create folders for each file type
    for folder_name in extensions.keys():
        folder_path = os.path.join(directory, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Move files into their respective folders
    for filename in os.listdir(directory):
        file_extension = os.path.splitext(filename)[1].lower()
        for folder_name, ext_list in extensions.items():
            if file_extension in ext_list:
                src_path = os.path.join(directory, filename)
                dst_path = os.path.join(directory, folder_name, filename)
                shutil.move(src_path, dst_path)
                print(f'Moved: {filename} to {folder_name}')
                break

if __name__ == '__main__':
    target_directory = input("Enter the directory to organize: ")
    if os.path.exists(target_directory):
        organize_files(target_directory)
        print("File organization complete!")
    else:
        print("The specified directory does not exist.")
