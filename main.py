# trained model is located here https://github.com/danielgatis/rembg

from rembg import remove
from PIL import Image
from pathlib import Path

def remove_bg():
    list_of_extensions = ['*.png', '*.jpg']
    all_files = []

    for ext in list_of_extensions:
        all_files.extend(Path(r"C:\Users\Nikita\Documents\VSCode\Python\DelBackground\input_imgs").glob(ext))

    for index, item in enumerate(all_files):
        input_path = Path(item)
        file_name = input_path.stem

        output_path = rf"C:\Users\Nikita\Documents\VSCode\Python\DelBackground\ouput_imgs\{file_name}_output.png"

        input_img = Image.open(input_path)
        output_img = remove(input_img)
        output_img.save(output_path)

        print(f"Comleted: {index + 1} / {len(all_files)}")

def main():
    remove_bg()

if __name__ == '__main__':
    main()