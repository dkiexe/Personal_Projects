import os
import time
import pathlib
from PIL import Image, ImageFilter
import concurrent.futures

main_path = os.path.abspath(os.path.join(pathlib.Path(__file__).parent, 'Photos'))
size = (1200, 1200)

def process_img(img_name):
    img = Image.open(os.path.join(main_path, img_name))
    img = img.filter(ImageFilter.GaussianBlur(15))
    img.thumbnail(size)
    img.save(os.path.join(main_path, "processed", img_name))

def main():
    start = time.perf_counter()
    image_list = [x for x in os.listdir(main_path) if x != 'processed']
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(process_img, image_list)
    stop = time.perf_counter()
    print(f'finished script in {round(stop-start, 2)}')

if __name__ == '__main__':
    main()