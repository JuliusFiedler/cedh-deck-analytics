import os
from datetime import datetime

def create_timestamped_dir(url):
    t = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    path = os.path.join("temp", "folder__" + t)
    os.makedirs(path, exist_ok=True)
    return path

def get_latest_output_dir():
    folders = os.listdir("temp")
    folders.sort()
    return os.path.join("temp", folders[-1])