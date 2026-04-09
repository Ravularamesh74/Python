import os

def get_file_size(path):
    size = os.path.getsize(path)
    return round(size / 1024, 2)  # KB