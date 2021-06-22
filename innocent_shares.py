from PIL import Image
import random
import os
import argparse
import shutil

parser = argparse.ArgumentParser()
parser.add_argument("images_path", help="Path to the directory containing input images.")
parser.add_argument("cover_image", help="Path to the cover images.")
arguments = parser.parse_args()

dir_path=arguments.images_path
cover_image_path=arguments.cover_image

if not os.path.isfile(cover_image_path):
    print("Error: Cover image does not exist")
    exit(1)

if not os.path.exists('output'):
    os.makedirs('output')

if not os.path.exists('output/innocent_shares'):
    os.makedirs('output/innocent_shares')

if not os.path.exists('output/innocent_shares/share_1'):
    os.makedirs('output/innocent_shares/share_1')
else:
    shutil.rmtree('output/innocent_shares/share_1', ignore_errors=True)
    os.makedirs('output/innocent_shares/share_1')

if not os.path.exists('output/innocent_shares/share_2'):
    os.makedirs('output/innocent_shares/share_2')
else:
    shutil.rmtree('output/innocent_shares/share_2', ignore_errors=True)
    os.makedirs('output/innocent_shares/share_2')

if not os.path.exists('output/innocent_shares/combined'):
    os.makedirs('output/innocent_shares/combined')
else:
    shutil.rmtree('output/innocent_shares/combined', ignore_errors=True)
    os.makedirs('output/innocent_shares/combined')

for image in os.listdir(dir_path):
    if image.endswith(".jpg"):
        input_image = Image.open(dir_path+'/'+image).convert('L')
        #input_image = Image.open('a.png').convert('L')
        input_image_pixels = input_image.load()
        input_image_width = input_image.size[0]
        input_image_height = input_image.size[1]

        cover_image = Image.open(cover_image_path).convert('L')
        #input_image = Image.open('a.png').convert('L')
        cover_image_pixels = cover_image.load()
        cover_image_width = cover_image.size[0]
        cover_image_height = cover_image.size[1]

        if (input_image_width != cover_image_width) or (input_image_height != cover_image_height):
            print("Error: Cover image dimensions are not equal to secret image dimensions.")

        print("Image Stats: ",image)
        print("Width: %d" % input_image_width)
        print("Height: %d\n" % input_image_height)

        #---------------Share Images---------------
        share_1_image = Image.new("L",(input_image_width,input_image_height))
        share_1_image_pixels = share_1_image.load()
        share_2_image = Image.new("L",(input_image_width,input_image_height))
        share_2_image_pixels = share_2_image.load()

#Algorithm
#- Assign alpha a random value of 0 or 1
#- If alpha==0, create share pixels using secret image pixel value
#    - If pixel value of secret image is 0, choose random column from B0
#    - If pixel value of secret image is 255, choose random column from B1
#- If alpha==1, create share pixels using cover image pixel
#    - If cover image pixel is 0, share pixels should be 0 and 255 or 255 and 0
#    - If cover image pixel is 255, share pixels should be 255
#
#B0=[0, 1; 0, 1]
#B1=[0, 1; 1, 0]

        for each_row_pixel in range(input_image_height):
            for each_column_pixel in range(input_image_width):
                alpha=random.choice((0,1))
                if alpha==0: #Secret Image
                    column_number=random.choice((0,1))
                    if input_image_pixels[each_column_pixel,each_row_pixel]==255:
                        if column_number==0:
                            share_1_image_pixels[each_column_pixel,each_row_pixel]=255
                            share_2_image_pixels[each_column_pixel,each_row_pixel]=255
                        else:
                            share_1_image_pixels[each_column_pixel,each_row_pixel]=0
                            share_2_image_pixels[each_column_pixel,each_row_pixel]=0
                    else:
                        if column_number==0:
                            share_1_image_pixels[each_column_pixel,each_row_pixel]=255
                            share_2_image_pixels[each_column_pixel,each_row_pixel]=0
                        else:
                            share_1_image_pixels[each_column_pixel,each_row_pixel]=0
                            share_2_image_pixels[each_column_pixel,each_row_pixel]=255

                else: #Cover Image
                    column_number=random.choice((0,1))
                    if cover_image_pixels[each_column_pixel,each_row_pixel]==0:
                        share_1_image_pixels[each_column_pixel,each_row_pixel]=0
                        share_2_image_pixels[each_column_pixel,each_row_pixel]=0
                    else:
                        if column_number==0:
                            share_1_image_pixels[each_column_pixel,each_row_pixel]=255
                            share_2_image_pixels[each_column_pixel,each_row_pixel]=0
                        else:
                            share_1_image_pixels[each_column_pixel,each_row_pixel]=0
                            share_2_image_pixels[each_column_pixel,each_row_pixel]=255

        share_1_image.save('output/innocent_shares/share_1/'+image+'_share_1.png')
        share_2_image.save('output/innocent_shares/share_2/'+image+'_share_2.png')

        #---------------Share Images Combined---------------
        share_images_combined = Image.new("L",(input_image_width,input_image_height))
        share_images_combined_pixels = share_images_combined.load()

        for each_row_pixel in range(input_image_height):
            for each_column_pixel in range(input_image_width):
                if (share_1_image_pixels[each_column_pixel,each_row_pixel]+share_2_image_pixels[each_column_pixel,each_row_pixel])==255:
                    share_images_combined_pixels[each_column_pixel,each_row_pixel]= 0
                else:
                    share_images_combined_pixels[each_column_pixel,each_row_pixel]= share_1_image_pixels[each_column_pixel,each_row_pixel]+share_2_image_pixels[each_column_pixel,each_row_pixel]

        share_images_combined.save('output/innocent_shares/combined/'+image+'_share_images_combined.png')

print("Input Images divided into Shares.")
