import os
import pandas as pd
from PIL import Image, ImageFont, ImageDraw
from functions import get_size, copy_item_to_new_folder, resize_img, sort_alphanum, combine_columns, convert_string_to_list
from configs.config_data import BG_IMG, TEXT_PER_LINE


class MemeGenerator:
    def __init__(self, bg_img, font_file, image_path, meme_path, text_path):
        self.bg_img = bg_img
        self.font_file = font_file
        self.image_path = image_path
        self.meme_path = meme_path
        self.text_path = text_path

    def make_meme_template(self):
        images = os.listdir(self.image_path)
        i = len(os.listdir(self.meme_path)) + 1
        for image in images:
            meme_name = f"meme{i}.jpg"
            copy_item_to_new_folder(BG_IMG,meme_name,self.bg_img,self.meme_path)
            background = Image.open(f"{self.meme_path}/{meme_name}")
            img = Image.open(f"{self.image_path}/{image}")
            background, img, area = get_size(background, img)
            background.paste(img, area)
            background = resize_img(background)
            background.save(f"{self.meme_path}/{meme_name}")
            i=i+1

    def add_text_on_image(self):
        meme_data = pd.read_csv(self.text_file)
        memes = os.listdir(self.meme_path)
        memes = pd.Series(sort_alphanum(memes))
        meme_data = combine_columns(meme_data, memes, "meme")
        self.draw_text_on_image(meme_data)


    def draw_text_on_image(self, meme_df):
        for idx in meme_df.index:
            meme = meme_df["meme"][idx]
            text = meme_df["text"][idx]
            img = Image.open(f"{self.meme_path}/{meme}")
            text_list = convert_string_to_list(text)
            text_font = ImageFont.truetype(f"{self.font_file}", 30) #font size
            img_edit = ImageDraw.Draw(img)
            total_text = len(text_list)
            text_width = 20
            text_height = 20
            for i in range(0, total_text, TEXT_PER_LINE):
                text_line = text_list[i:i+TEXT_PER_LINE]
                text_line = ' '.join(map(str, text_line))
                line_distance = 35
                img_edit.text((text_width, text_height), text_line, (0, 0, 0), font=text_font) #font color
                text_height = text_height + line_distance
            img.save(f"{self.meme_path}/{meme}")


    def generate_memes(self):
        self.make_meme_template()
        self.add_text_on_image()