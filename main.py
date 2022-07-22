from configs.config_data import BACKGROUND_PATH, BG_IMG, DATA_PATH,\
    FONT_PATH, FONT_NAME, IMAGE_PATH, MEME_PATH, ROOT_DIR, TEXT_PATH
from meme_generator.meme_generator import MemeGenerator
from image_text_extractor.image_text_extractor import TextExtractorFromImage
from make_dirs_if_not_exist import make_dirs


def main(bg_img, image_path, meme_path, text_path):
    make_dirs()
    meme_generator = MemeGenerator(bg_img, font_file, image_path, meme_path, text_path)
    meme_generator.generate_memes()
    text_extractor = TextExtractorFromImage(meme_path, text_path)
    text_extractor.extract_text_from_image()


if __name__ == '__main__':
    bg_img = f"{ROOT_DIR}/{DATA_PATH}/{BACKGROUND_PATH}/{BG_IMG}"
    font_file = f"{ROOT_DIR}/{DATA_PATH}/{FONT_PATH}/{FONT_NAME}"
    image_path = f"{ROOT_DIR}/{DATA_PATH}/{IMAGE_PATH}"
    meme_path = f"{ROOT_DIR}/{DATA_PATH}/{MEME_PATH}"
    text_path = f"{ROOT_DIR}/{DATA_PATH}/{TEXT_PATH}"
    main(bg_img, image_path, meme_path, text_path)