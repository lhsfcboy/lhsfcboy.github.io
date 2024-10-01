import os

def recursive_listdir(path):
    files = os.listdir(path)
    for file in files:
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
            print(file)
        elif os.path.isdir(file_path):
            print(file_path)
            recursive_listdir(file_path)
recursive_listdir('/tmp')

def recursive_duplicate_dir(source_path, target_base_path):
    files = os.listdir(source_path)
    for file in files:
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
            print(file)
        elif os.path.isdir(file_path):
            print(file_path)
            recursive_listdir(file_path)
