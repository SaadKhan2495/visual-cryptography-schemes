from PIL import Image
import os
import argparse
import shutil

parser = argparse.ArgumentParser()
parser.add_argument("images_path", help="Path to the directory containing input images.")
arguments = parser.parse_args()

dir_path=arguments.images_path

if not os.path.exists('jpg_files'):
    os.makedirs('jpg_files')
else:
    shutil.rmtree('jpg_files', ignore_errors=True)
    os.makedirs('jpg_files')

for image in os.listdir(dir_path):
    if image.endswith(".png"):
        input_image = Image.open(dir_path+'/'+image)
        pixels= input_image.load()
        input_image_width, input_image_height= input_image.size
        jpg_image = Image.new("L",(input_image_width ,input_image_height))
        jpg_image_pixels=jpg_image.load()
        for x in range(input_image_width):
            for y in range(input_image_height):
                jpg_image_pixels[x,y]=255-pixels[x,y][3]
        jpg_image.save('jpg_files/'+image.split('.')[0]+'.jpg')

print("All input png images converted to jpg format")
