from os import listdir, rename, mkdir
from os.path import isfile, join

PATH_TO_FILES = r'C:\Users\USERNAME\Downloads'
TYPE_OF_FILES = {
    'jpg': 'images', 'png': 'images', 'jpeg': 'images', 'gif': 'images', 'bmp': 'images',
    'mp4': 'videos', 'avi': 'videos', 'mkv': 'videos', 'flv': 'videos', 'wmv': 'videos', 'mov': 'videos',
    'mp3': 'audio', 'wav': 'audio', 'aac': 'audio', 'ogg': 'audio', 'flac': 'audio',
    'txt': 'text', 'doc': 'text', 'docx': 'text', 'pdf': 'text',
    'zip': 'compressed', 'rar': 'compressed', '7z': 'compressed', 'tar': 'compressed', 'gz': 'compressed',
    'json': 'data', 'csv': 'data',
    'xls': 'spreadsheet', 'xlsx': 'spreadsheet', 'ods': 'spreadsheet',
    'ppt': 'presentation', 'pptx': 'presentation', 'odp': 'presentation'
}

all_files = [f for f in listdir(PATH_TO_FILES) if isfile(join(PATH_TO_FILES, f)) if not f.endswith(".ini")]
for file in all_files:
    file_extension = file.split('.')[-1]
    if file_extension in TYPE_OF_FILES:
        destination_folder = join(PATH_TO_FILES, TYPE_OF_FILES[file_extension])
        try:
            mkdir(destination_folder)
        except FileExistsError:
            pass
        rename(join(PATH_TO_FILES, file), join(destination_folder, file))
    else:
        print(f'{file} is not in the list of types')
        
