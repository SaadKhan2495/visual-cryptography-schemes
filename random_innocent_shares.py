from PIL import Image
import random
import os
import argparse
import shutil

parser = argparse.ArgumentParser()
parser.add_argument("no_of_shares", help="Total number of random shares that the script will create.")
parser.add_argument("cover_image", help="Path to the cover images.")
arguments = parser.parse_args()

no_of_shares=int(arguments.no_of_shares)
cover_image_path=arguments.cover_image

if not os.path.isfile(cover_image_path):
    print("Error: Cover image does not exist")
    exit(1)

if not os.path.exists('output'):
    os.makedirs('output')

if not os.path.exists('output/random_innocent_shares'):
    os.makedirs('output/random_innocent_shares')

for share_number in range(no_of_shares):
    input_image_width = 278
    input_image_height = 278

    cover_image = Image.open(cover_image_path).convert('L')
    #input_image = Image.open('a.png').convert('L')
    cover_image_pixels = cover_image.load()
    cover_image_width = cover_image.size[0]
    cover_image_height = cover_image.size[1]

    if (input_image_width != cover_image_width) or (input_image_height != cover_image_height):
        print("Error: Cover image dimensions are not equal to secret image dimensions.")

    #---------------Share Images---------------
    share_image = Image.new("L",(input_image_width,input_image_height))
    share_image_pixels = share_image.load()

    for each_row_pixel in range(input_image_height):
        for each_column_pixel in range(input_image_width):
            prob=random.uniform(0,1)
            alpha=random.choice((0,1))
            if alpha==0: #Secret Image
                if prob>=0.5:
                    share_image_pixels[each_column_pixel,each_row_pixel]=255
                else:
                    share_image_pixels[each_column_pixel,each_row_pixel]=0
                    
            else: #Cover Image
                if cover_image_pixels[each_column_pixel,each_row_pixel]==0:
                    share_image_pixels[each_column_pixel,each_row_pixel]=0
                else:
                    share_image_pixels[each_column_pixel,each_row_pixel]=255

    share_image.save('output/random_innocent_shares/random_share_'+str(share_number)+'.png')
    print("Random share number %d created"%share_number)

print("Total random shares created: %d"%no_of_shares)

