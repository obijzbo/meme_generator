import numpy as np
from easyocr import Reader
import cv2
from PIL import Image, ImageEnhance, ImageFilter
import os
from functions import sort_alphanum
from configs.config_data import ROOT_DIR, DATA_PATH, PROSSED_MEME_PATH


class TextExtractorFromImage:
    def __init__(self, meme_path, text_path):
        self.meme_path = meme_path
        self.text_path = text_path
        self.reader = Reader(['bn'])

    def extract_text_from_image(self):
        memes = os.listdir(self.meme_path)
        images = sort_alphanum(memes)
        for image in images:
            result = self.reader.readtext(f"{self.meme_path}/{image}")
            texts = ''
            for (_, text, _) in result:
                texts = texts + ' ' + text
            print(texts)