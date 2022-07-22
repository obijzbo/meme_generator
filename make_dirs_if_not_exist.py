from functions import make_dir
from configs.config_data import BACKGROUND_PATH, DATA_PATH, FONT_PATH, IMAGE_PATH, MEME_PATH, ROOT_DIR, TEXT_PATH

bg_path = f"{ROOT_DIR}/{DATA_PATH}/{BACKGROUND_PATH}"
font_path = f"{ROOT_DIR}/{DATA_PATH}/{FONT_PATH}"
image_path = f"{ROOT_DIR}/{DATA_PATH}/{IMAGE_PATH}"
meme_path = f"{ROOT_DIR}/{DATA_PATH}/{MEME_PATH}"
text_path = f"{ROOT_DIR}/{DATA_PATH}/{TEXT_PATH}"
data_path = f"{ROOT_DIR}/{DATA_PATH}"

path_list = [data_path, bg_path, font_path, image_path, meme_path, text_path]

def make_dirs():
    for path in path_list:
        make_dir(path)