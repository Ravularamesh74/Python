import os
from utils import get_file_info
from filters import match_name, match_extension, match_size

def search_files(directory, name=None, ext=None, min_size=0, max_size=float('inf')):
    results = []

    for root, _, files in os.walk(directory):
        for f in files:
            path = os.path.join(root, f)
            file_info = get_file_info(path)

            if name and not match_name(file_info, name):
                continue
            if ext and not match_extension(file_info, ext):
                continue
            if not match_size(file_info, min_size, max_size):
                continue

            results.append(file_info)

    return results