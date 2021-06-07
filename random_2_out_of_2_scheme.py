from PIL import Image
import random
import os
import argparse
import shutil

parser = argparse.ArgumentParser()
parser.add_argument("no_of_shares", help="Total number of random shares that the script will create.")
arguments = parser.parse_args()

no_of_shares=int(arguments.no_of_shares)

image_width=278
image_height=278

if not os.path.exists('output'):
    os.makedirs('output')

if not os.path.exists('output/random_2_out_of_2'):
    os.makedirs('output/random_2_out_of_2')

for share_number in range(no_of_shares):
    #---------------Share Images---------------
    share_image = Image.new("L",(image_width*2,image_height))
    share_image_pixels = share_image.load()

    for each_row_pixel in range(image_height):
        share_1_image_column_pixel = -1
        for each_column_pixel in range(image_width):
            pixel_prob=random.uniform(0,1)
            share_prob=random.uniform(0,1)
            if pixel_prob >= 0.5:
                if share_prob>=0.5:
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,each_row_pixel]=255
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,each_row_pixel]=0
                else:
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,each_row_pixel]=0
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,each_row_pixel]=255
            else:
                if share_prob>=0.5:
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,each_row_pixel]=255
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,each_row_pixel]=0
                else:
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,each_row_pixel]=0
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,each_row_pixel]=255

    share_image.save('output/random_2_out_of_2/random_share_'+str(share_number)+'.png')
    print("Random share number %d created"%share_number)

print("Total random shares created: %d"%no_of_shares)
