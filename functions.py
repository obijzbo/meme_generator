import os
import shutil
from PIL import Image
import re


def make_version(file_path):
    try:
        existing_versions = os.listdir(file_path)
        versions = [int(v) for v in existing_versions]
        if versions:
            last_version = max(versions)
            new_version = last_version + 1
        else:
            new_version = 1
    except FileNotFoundError as e:
        print(e)
        new_version = 1
    print(f'Version : {new_version}')
    return new_version

def get_latest_version(file_path):
    try:
        existing_versions = os.listdir(file_path)
        versions = [int(v) for v in existing_versions]
        latest_version = max(versions)
        return latest_version
    except FileNotFoundError as e:
        print(e)

def make_dir(dir_name):
    try:
        os.mkdir(dir_name)
        print("Directory ", dir_name, " created.")
    except FileExistsError:
        print("Directory ", dir_name, " already exist.")

def remove_file_if_exists(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f'{file_path} file successfully removed!')
    else:
        print(f'{file_path} path not exists!')

def shuffle_folder_items(dir):
    items = os.listdir(dir)
    return items


# def make_train_test_val(shuffled_items, category):
#         category_len = len(shuffled_items)
#         train_end = int(category_len*0.7)
#         val_end = int(category_len*0.2)
#         test_end = int(category_len*0.1)
#         train_list = shuffled_items[:(train_end-1)]
#         val_list = shuffled_items[train_end:(train_end+val_end)-1]
#         test_list = shuffled_items[val_end:(val_end+test_end)-1]
#         copy_item_to_new_folder(train_list, f"{CURRENT_DATA_SET}/{category}", f"{ROOT_DIR}/{DATA_PATH}/{TRAIN_DATA_PATH}/{category}")
#         copy_item_to_new_folder(val_list, f"{CURRENT_DATA_SET}/{category}", f"{ROOT_DIR}/{DATA_PATH}/{VALIDATION_DATA_PATH}/{category}")
#         copy_item_to_new_folder(test_list, f"{CURRENT_DATA_SET}/{category}", f"{ROOT_DIR}/{DATA_PATH}/{TEST_DATA_PATH}/{category}")



def copy_item_to_new_folder(item_name, new_name, from_dir, to_dir):
        try:
            shutil.copy(f"{from_dir}",f"{to_dir}/{new_name}")
            print(f"{item_name} copied successfully as {new_name}")
        except shutil.SameFileError:
            print("Source and destination represents the same file")

def get_size(background, img):
    text_area = calculate_text_area(img)
    width, height = img.size
    background = background.resize((width, height+text_area))
    area = (0, text_area)
    return(background, img, area)

def calculate_text_area(img):
    width, height = img.size
    area = (height*40)/100
    return int(area)

def resize_img(img):
    height = 460
    img_w = img.size[0]
    img_h = img.size[1]
    h_percentage = (height / float(img_h))
    w_size = int((float(img_w) * float(h_percentage)))
    img = img.resize((height, w_size), Image.ANTIALIAS)
    return img

def sort_alphanum(value):
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(value, key=alphanum_key)

def combine_columns(df, col, name):
    if len(df.columns) < len(col):
        col = col[:int(len(df))]
    df[name] = col
    return df

def convert_string_to_list(text):
    text_list = list(text.split(" "))
    return text_list