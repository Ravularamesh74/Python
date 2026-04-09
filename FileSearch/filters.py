def match_name(file, keyword):
    return keyword.lower() in file["name"].lower()

def match_extension(file, ext):
    return file["name"].lower().endswith(ext.lower())

def match_size(file, min_size, max_size):
    return min_size <= file["size_kb"] <= max_size