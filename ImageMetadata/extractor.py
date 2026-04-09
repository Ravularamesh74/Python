from PIL import Image
from PIL.ExifTags import TAGS
import os
from utils import get_file_size

def extract_metadata(image_path):
    try:
        img = Image.open(image_path)

        metadata = {
            "filename": os.path.basename(image_path),
            "format": img.format,
            "size": f"{img.width}x{img.height}",
            "file_size_kb": get_file_size(image_path),
            "camera": "N/A",
            "date": "N/A"
        }

        exif_data = img._getexif()

        if exif_data:
            for tag, value in exif_data.items():
                tag_name = TAGS.get(tag, tag)

                if tag_name == "Model":
                    metadata["camera"] = value
                elif tag_name == "DateTime":
                    metadata["date"] = value

        return metadata

    except Exception as e:
        return {"error": str(e)}