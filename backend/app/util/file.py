from fastapi import FastAPI, HTTPException
import base64
import binascii
from io import BytesIO
from PIL import Image
from pathlib import Path
import time
from app.core.exception import *

class File:
    ROOT_DIR = 'public'
    ALLOWED_FORMAT = {"PNG", "JPEG"}
    DEFAULT_PREFIX = "i"

    @staticmethod
    def save_image_from_b64(b64:str,disk:str,prefix:str=None, ) -> str:
        try:
            UPLOAD_DIR = Path(f"{File.ROOT_DIR}/{disk}") if disk else Path(f"{File.ROOT_DIR}")
            UPLOAD_DIR.mkdir(exist_ok=True, parents=True)

            if ',' in b64:
                b64 = b64.split(',')[1]
            
            image_bytes = base64.b64decode(b64)
            image = Image.open(BytesIO(image_bytes))

            img_format = image.format.upper() if image.format else ""

            if img_format not in File.ALLOWED_FORMAT:
                raise

            ext = "png" if img_format == "PNG" else "jpg"

            filename = f"{prefix if prefix else File.DEFAULT_PREFIX}_{int(time.time())}.{ext}"
            file_path = UPLOAD_DIR/filename
            image.save(file_path)
            return f"{disk}/{filename}" if disk else f"{filename}"
        except binascii.Error:
            raise 
        except Exception as e:
            raise