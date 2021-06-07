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

if not os.path.exists('output/random_3_out_of_3'):
    os.makedirs('output/random_3_out_of_3')

for share_number in range(no_of_shares):
    #---------------Share Images---------------
    share_image_width=image_width * 2
    share_image_height=image_height*2
    share_image = Image.new("L",(share_image_width,share_image_height))
    share_image_pixels = share_image.load()
    

    share_1_image_row_pixel = 0
    for each_row_pixel in range(image_height):
        share_1_image_column_pixel = 0

        share_1_image_row_pixel = each_row_pixel
        share_1_image_row_pixel=share_1_image_row_pixel*2
    
        for each_column_pixel in range(image_width):
            pixel_prob=random.uniform(0,1)
            share_prob=random.uniform(0,1)
            if pixel_prob >= 0.5:
                if share_prob>=0 and share_prob<=0.0415:
                    #----------01----------
                    #-----0011-----
                    share_1_image_column_pixel=each_column_pixel
                    share_1_image_column_pixel=share_1_image_column_pixel*2
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel-=1
                    share_1_image_row_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_row_pixel-=1

                elif share_prob>0.0415 and share_prob<=0.083:
                    #----------02----------
                    #-----0011-----
                    share_1_image_column_pixel=each_column_pixel
                    share_1_image_column_pixel=share_1_image_column_pixel*2
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel-=1
                    share_1_image_row_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_row_pixel-=1

                elif share_prob>0.083 and share_prob<=0.1245:
                    #----------03----------
                    #-----0101-----
                    share_1_image_column_pixel=each_column_pixel
                    share_1_image_column_pixel=share_1_image_column_pixel*2
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel-=1
                    share_1_image_row_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_row_pixel-=1

                elif share_prob>0.1245 and share_prob<=0.166:
                    #----------04----------
                    #-----0101-----
                    share_1_image_column_pixel=each_column_pixel
                    share_1_image_column_pixel=share_1_image_column_pixel*2
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel-=1
                    share_1_image_row_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_row_pixel-=1

                elif share_prob>0.166 and share_prob<=0.2075:
                    #----------05----------
                    #-----0110-----
                    share_1_image_column_pixel=each_column_pixel
                    share_1_image_column_pixel=share_1_image_column_pixel*2
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel-=1
                    share_1_image_row_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_row_pixel-=1

                elif share_prob>0.2075 and share_prob<=0.249:
                    #----------06----------
                    #-----0110-----
                    share_1_image_column_pixel=each_column_pixel
                    share_1_image_column_pixel=share_1_image_column_pixel*2
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel-=1
                    share_1_image_row_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_row_pixel-=1

                elif share_prob>0.249 and share_prob<=0.2905:
                    #----------07----------
                    #-----0011-----
                    share_1_image_column_pixel=each_column_pixel
                    share_1_image_column_pixel=share_1_image_column_pixel*2
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel-=1
                    share_1_image_row_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_row_pixel-=1

                elif share_prob>0.2905 and share_prob<=0.332:
                    #----------08----------
                    #-----0011-----
                    share_1_image_column_pixel=each_column_pixel
                    share_1_image_column_pixel=share_1_image_column_pixel*2
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel-=1
                    share_1_image_row_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_row_pixel-=1

                elif share_prob>0.332 and share_prob<=0.3735:
                    #----------09----------
                    #-----1010-----
                    share_1_image_column_pixel=each_column_pixel
                    share_1_image_column_pixel=share_1_image_column_pixel*2
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel-=1
                    share_1_image_row_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_row_pixel-=1

                elif share_prob>0.3735 and share_prob<=0.415:
                    #----------10----------
                    #-----1010-----
                    share_1_image_column_pixel=each_column_pixel
                    share_1_image_column_pixel=share_1_image_column_pixel*2
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel-=1
                    share_1_image_row_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_row_pixel-=1

                elif share_prob>0.415 and share_prob<=0.4565:
                    #----------11----------
                    #-----1001-----
                    share_1_image_column_pixel=each_column_pixel
                    share_1_image_column_pixel=share_1_image_column_pixel*2
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel-=1
                    share_1_image_row_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_row_pixel-=1

                elif share_prob>0.4565 and share_prob<=0.498:
                    #----------12----------
                    #-----1001-----
                    share_1_image_column_pixel=each_column_pixel
                    share_1_image_column_pixel=share_1_image_column_pixel*2
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel-=1
                    share_1_image_row_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_row_pixel-=1

                elif share_prob>0.498 and share_prob<=0.5395:
                    #----------13----------
                    #-----1100-----
                    share_1_image_column_pixel=each_column_pixel
                    share_1_image_column_pixel=share_1_image_column_pixel*2
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel-=1
                    share_1_image_row_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_row_pixel-=1

                elif share_prob>0.5395 and share_prob<=0.581:
                    #----------14----------
                    #-----1100-----
                    share_1_image_column_pixel=each_column_pixel
                    share_1_image_column_pixel=share_1_image_column_pixel*2
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel-=1
                    share_1_image_row_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_row_pixel-=1
            
                elif share_prob>0.581 and share_prob<=0.6225:
                    #----------15----------
                    #-----0101-----
                    share_1_image_column_pixel=each_column_pixel
                    share_1_image_column_pixel=share_1_image_column_pixel*2
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel-=1
                    share_1_image_row_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_row_pixel-=1

                elif share_prob>0.6225 and share_prob<=0.664:
                    #----------16----------
                    #-----0101-----
                    share_1_image_column_pixel=each_column_pixel
                    share_1_image_column_pixel=share_1_image_column_pixel*2
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel-=1
                    share_1_image_row_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_row_pixel-=1

                elif share_prob>0.664 and share_prob<=0.7055:
                    #----------17----------
                    #-----1001-----
                    share_1_image_column_pixel=each_column_pixel
                    share_1_image_column_pixel=share_1_image_column_pixel*2
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel-=1
                    share_1_image_row_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_row_pixel-=1

                elif share_prob>0.7055 and share_prob<=0.747:
                    #----------18----------
                    #-----1001-----
                    share_1_image_column_pixel=each_column_pixel
                    share_1_image_column_pixel=share_1_image_column_pixel*2
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel-=1
                    share_1_image_row_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_row_pixel-=1

                elif share_prob>0.747 and share_prob<=0.7885:
                    #----------19----------
                    #-----1100-----
                    share_1_image_column_pixel=each_column_pixel
                    share_1_image_column_pixel=share_1_image_column_pixel*2
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel-=1
                    share_1_image_row_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_row_pixel-=1

                elif share_prob>0.7885 and share_prob<=0.83:
                    #----------20----------
                    #-----1100-----
                    share_1_image_column_pixel=each_column_pixel
                    share_1_image_column_pixel=share_1_image_column_pixel*2
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel-=1
                    share_1_image_row_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_row_pixel-=1

                elif share_prob>0.83 and share_prob<=0.8715:
                    #----------21----------
                    #-----1010-----
                    share_1_image_column_pixel=each_column_pixel
                    share_1_image_column_pixel=share_1_image_column_pixel*2
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel-=1
                    share_1_image_row_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_row_pixel-=1

                elif share_prob>0.8715 and share_prob<=0.913:
                    #----------22----------
                    #-----1010-----
                    share_1_image_column_pixel=each_column_pixel
                    share_1_image_column_pixel=share_1_image_column_pixel*2
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel-=1
                    share_1_image_row_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_row_pixel-=1

                elif share_prob>0.913 and share_prob<=0.9545:
                    #----------23----------
                    #-----0110-----
                    share_1_image_column_pixel=each_column_pixel
                    share_1_image_column_pixel=share_1_image_column_pixel*2
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel-=1
                    share_1_image_row_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_row_pixel-=1

                else:
                    #----------24----------
                    #-----0110-----
                    share_1_image_column_pixel=each_column_pixel
                    share_1_image_column_pixel=share_1_image_column_pixel*2
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel-=1
                    share_1_image_row_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_row_pixel-=1

            else:  # Pixel is Black
                if share_prob>=0 and share_prob<=0.0415:
                    #----------01----------
                    #-----1100-----
                    share_1_image_column_pixel=each_column_pixel
                    share_1_image_column_pixel=share_1_image_column_pixel*2
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel-=1
                    share_1_image_row_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_row_pixel-=1

                elif share_prob>0.0415 and share_prob<=0.083:
                    #----------02----------
                    #-----1100-----
                    share_1_image_column_pixel=each_column_pixel
                    share_1_image_column_pixel=share_1_image_column_pixel*2
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel-=1
                    share_1_image_row_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_row_pixel-=1

                elif share_prob>0.083 and share_prob<=0.1245:
                    #----------03----------
                    #-----1010-----
                    share_1_image_column_pixel=each_column_pixel
                    share_1_image_column_pixel=share_1_image_column_pixel*2
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel-=1
                    share_1_image_row_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_row_pixel-=1

                elif share_prob>0.1245 and share_prob<=0.166:
                    #----------04----------
                    #-----1010-----
                    share_1_image_column_pixel=each_column_pixel
                    share_1_image_column_pixel=share_1_image_column_pixel*2
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel-=1
                    share_1_image_row_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_row_pixel-=1

                elif share_prob>0.166 and share_prob<=0.2075:
                    #----------05----------
                    #-----1001-----
                    share_1_image_column_pixel=each_column_pixel
                    share_1_image_column_pixel=share_1_image_column_pixel*2
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel-=1
                    share_1_image_row_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_row_pixel-=1

                elif share_prob>0.2075 and share_prob<=0.249:
                    #----------06----------
                    #-----1001-----
                    share_1_image_column_pixel=each_column_pixel
                    share_1_image_column_pixel=share_1_image_column_pixel*2
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel-=1
                    share_1_image_row_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_row_pixel-=1

                elif share_prob>0.249 and share_prob<=0.2905:
                    #----------07----------
                    #-----1100-----
                    share_1_image_column_pixel=each_column_pixel
                    share_1_image_column_pixel=share_1_image_column_pixel*2
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel-=1
                    share_1_image_row_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_row_pixel-=1

                elif share_prob>0.2905 and share_prob<=0.332:
                    #----------08----------
                    #-----1100-----
                    share_1_image_column_pixel=each_column_pixel
                    share_1_image_column_pixel=share_1_image_column_pixel*2
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel-=1
                    share_1_image_row_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_row_pixel-=1

                elif share_prob>0.332 and share_prob<=0.3735:
                    #----------09----------
                    #-----0101-----
                    share_1_image_column_pixel=each_column_pixel
                    share_1_image_column_pixel=share_1_image_column_pixel*2
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel-=1
                    share_1_image_row_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_row_pixel-=1

                elif share_prob>0.3735 and share_prob<=0.415:
                    #----------10----------
                    #-----0101-----
                    share_1_image_column_pixel=each_column_pixel
                    share_1_image_column_pixel=share_1_image_column_pixel*2
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel-=1
                    share_1_image_row_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_row_pixel-=1

                elif share_prob>0.415 and share_prob<=0.4565:
                    #----------11----------
                    #-----0110-----
                    share_1_image_column_pixel=each_column_pixel
                    share_1_image_column_pixel=share_1_image_column_pixel*2
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel-=1
                    share_1_image_row_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_row_pixel-=1

                elif share_prob>0.4565 and share_prob<=0.498:
                    #----------12----------
                    #-----0110-----
                    share_1_image_column_pixel=each_column_pixel
                    share_1_image_column_pixel=share_1_image_column_pixel*2
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel-=1
                    share_1_image_row_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_row_pixel-=1

                elif share_prob>0.498 and share_prob<=0.5395:
                    #----------13----------
                    #-----0011-----
                    share_1_image_column_pixel=each_column_pixel
                    share_1_image_column_pixel=share_1_image_column_pixel*2
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel-=1
                    share_1_image_row_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_row_pixel-=1

                elif share_prob>0.5395 and share_prob<=0.581:
                    #----------14----------
                    #-----0011-----
                    share_1_image_column_pixel=each_column_pixel
                    share_1_image_column_pixel=share_1_image_column_pixel*2
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel-=1
                    share_1_image_row_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_row_pixel-=1

                elif share_prob>0.581 and share_prob<=0.6225:
                    #----------15----------
                    #-----1010-----
                    share_1_image_column_pixel=each_column_pixel
                    share_1_image_column_pixel=share_1_image_column_pixel*2
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel-=1
                    share_1_image_row_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_row_pixel-=1

                elif share_prob>0.6225 and share_prob<=0.664:
                    #----------16----------
                    #-----1010-----
                    share_1_image_column_pixel=each_column_pixel
                    share_1_image_column_pixel=share_1_image_column_pixel*2
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel-=1
                    share_1_image_row_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_row_pixel-=1

                elif share_prob>0.664 and share_prob<=0.7055:
                    #----------17----------
                    #-----0110-----
                    share_1_image_column_pixel=each_column_pixel
                    share_1_image_column_pixel=share_1_image_column_pixel*2
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel-=1
                    share_1_image_row_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_row_pixel-=1

                elif share_prob>0.7055 and share_prob<=0.747:
                    #----------18----------
                    #-----0110-----
                    share_1_image_column_pixel=each_column_pixel
                    share_1_image_column_pixel=share_1_image_column_pixel*2
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel-=1
                    share_1_image_row_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_row_pixel-=1

                elif share_prob>0.747 and share_prob<=0.7885:
                    #----------19----------
                    #-----0011-----
                    share_1_image_column_pixel=each_column_pixel
                    share_1_image_column_pixel=share_1_image_column_pixel*2
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel-=1
                    share_1_image_row_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_row_pixel-=1

                elif share_prob>0.7885 and share_prob<=0.83:
                    #----------20----------
                    #-----0011-----
                    share_1_image_column_pixel=each_column_pixel
                    share_1_image_column_pixel=share_1_image_column_pixel*2
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel-=1
                    share_1_image_row_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_row_pixel-=1

                elif share_prob>0.83 and share_prob<=0.8715:
                    #----------21----------
                    #-----0101-----
                    share_1_image_column_pixel=each_column_pixel
                    share_1_image_column_pixel=share_1_image_column_pixel*2
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel-=1
                    share_1_image_row_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_row_pixel-=1

                elif share_prob>0.8715 and share_prob<=0.913:
                    #----------22----------
                    #-----0101-----
                    share_1_image_column_pixel=each_column_pixel
                    share_1_image_column_pixel=share_1_image_column_pixel*2
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel-=1
                    share_1_image_row_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_row_pixel-=1

                elif share_prob>0.913 and share_prob<=0.9545:
                    #----------23----------
                    #-----1001-----
                    share_1_image_column_pixel=each_column_pixel
                    share_1_image_column_pixel=share_1_image_column_pixel*2
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel-=1
                    share_1_image_row_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_row_pixel-=1

                else:
                    #----------24----------
                    #-----1001-----
                    share_1_image_column_pixel=each_column_pixel
                    share_1_image_column_pixel=share_1_image_column_pixel*2
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel-=1
                    share_1_image_row_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                    share_1_image_column_pixel+=1
                    share_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                    share_1_image_row_pixel-=1
        
    share_image.save('output/random_3_out_of_3/random_share_'+str(share_number)+'.png')
    print("Random share number %d created"%share_number)

print("Total random shares created: %d"%no_of_shares)