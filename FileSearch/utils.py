import os

def format_size(size):
    return round(size / 1024, 2)  # KB

def get_file_info(path):
    return {
        "name": os.path.basename(path),
        "path": path,
        "size_kb": format_size(os.path.getsize(path))
    }