from PIL import Image
import random

input_image = Image.open('a.png').convert('L')
pixels = input_image.load()
input_image_width = input_image.size[0]
input_image_height = input_image.size[1]

print("Image Stats")
print("Width: %d" % input_image_width)
print("Height: %d" % input_image_height)

print("\nPrinting pixel values of original image\n")
for each_row_pixel in range(input_image_height):
    for each_column_pixel in range(input_image_width):
        print("%3d " % pixels[each_column_pixel,each_row_pixel], end="")
    print("")

#---------------Black and White Image---------------
b_and_w_image = Image.new("L",(input_image_width,input_image_height))
b_and_w_image_pixels = b_and_w_image.load()

for each_row_pixel in range(input_image_height):
    for each_column_pixel in range(input_image_width):
        if pixels[each_column_pixel,each_row_pixel] > 127.5:
            b_and_w_image_pixels[each_column_pixel,each_row_pixel] = 255
        else:
            b_and_w_image_pixels[each_column_pixel,each_row_pixel] = 0
    print("")

print("\nPrint Black and White image\n")
for each_row_pixel in range(input_image_height):
    for each_column_pixel in range(input_image_width):
        print("%3d " % b_and_w_image_pixels[each_column_pixel,each_row_pixel], end="")
    print("")
b_and_w_image.save('a_black_and_white.png')


#---------------Share Images---------------
share_image_width=input_image_width * 2
share_image_height=input_image_height*2
share_1_image = Image.new("L",(share_image_width,share_image_height))
share_1_image_pixels = share_1_image.load()
share_2_image = Image.new("L",(share_image_width,share_image_height))
share_2_image_pixels = share_2_image.load()
share_3_image = Image.new("L",(share_image_width,share_image_height))
share_3_image_pixels = share_3_image.load()

share_1_image_row_pixel = 0
share_2_image_row_pixel = 0
share_3_image_row_pixel = 0
for each_row_pixel in range(input_image_height):
    share_1_image_column_pixel = 0
    share_2_image_column_pixel = 0
    share_3_image_column_pixel = 0

    share_1_image_row_pixel = each_row_pixel
    share_1_image_row_pixel=share_1_image_row_pixel*2
    share_2_image_row_pixel = each_row_pixel
    share_2_image_row_pixel=share_2_image_row_pixel*2
    share_3_image_row_pixel = each_row_pixel
    share_3_image_row_pixel=share_3_image_row_pixel*2
    
    for each_column_pixel in range(input_image_width):
        prob=random.uniform(0,1)
        if pixels[each_column_pixel,each_row_pixel] > 127.5: # Pixel is White
            if prob>=0 and prob<=0.0415:
                #----------01----------
                #-----0011-----
                share_1_image_column_pixel=each_column_pixel
                share_1_image_column_pixel=share_1_image_column_pixel*2
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel-=1
                share_1_image_row_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_row_pixel-=1

                #-----0101-----
                share_2_image_column_pixel=each_column_pixel
                share_2_image_column_pixel=share_2_image_column_pixel*2
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel-=1
                share_2_image_row_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_row_pixel-=1

                #-----0110-----
                share_3_image_column_pixel=each_column_pixel
                share_3_image_column_pixel=share_3_image_column_pixel*2
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel-=1
                share_3_image_row_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_row_pixel-=1

            elif prob>0.0415 and prob<=0.083:
                #----------02----------
                #-----0011-----
                share_1_image_column_pixel=each_column_pixel
                share_1_image_column_pixel=share_1_image_column_pixel*2
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel-=1
                share_1_image_row_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_row_pixel-=1

                #-----0110-----
                share_2_image_column_pixel=each_column_pixel
                share_2_image_column_pixel=share_2_image_column_pixel*2
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel-=1
                share_2_image_row_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_row_pixel-=1

                #-----0101-----
                share_3_image_column_pixel=each_column_pixel
                share_3_image_column_pixel=share_3_image_column_pixel*2
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel-=1
                share_3_image_row_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_row_pixel-=1

            elif prob>0.083 and prob<=0.1245:
                #----------03----------
                #-----0101-----
                share_1_image_column_pixel=each_column_pixel
                share_1_image_column_pixel=share_1_image_column_pixel*2
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel-=1
                share_1_image_row_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_row_pixel-=1

                #-----0011-----
                share_2_image_column_pixel=each_column_pixel
                share_2_image_column_pixel=share_2_image_column_pixel*2
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel-=1
                share_2_image_row_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_row_pixel-=1

                #-----0110-----
                share_3_image_column_pixel=each_column_pixel
                share_3_image_column_pixel=share_3_image_column_pixel*2
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel-=1
                share_3_image_row_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_row_pixel-=1

            elif prob>0.1245 and prob<=0.166:
                #----------04----------
                #-----0101-----
                share_1_image_column_pixel=each_column_pixel
                share_1_image_column_pixel=share_1_image_column_pixel*2
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel-=1
                share_1_image_row_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_row_pixel-=1

                #-----0110-----
                share_2_image_column_pixel=each_column_pixel
                share_2_image_column_pixel=share_2_image_column_pixel*2
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel-=1
                share_2_image_row_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_row_pixel-=1

                #-----0011-----
                share_3_image_column_pixel=each_column_pixel
                share_3_image_column_pixel=share_3_image_column_pixel*2
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel-=1
                share_3_image_row_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_row_pixel-=1

            elif prob>0.166 and prob<=0.2075:
                #----------05----------
                #-----0110-----
                share_1_image_column_pixel=each_column_pixel
                share_1_image_column_pixel=share_1_image_column_pixel*2
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel-=1
                share_1_image_row_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_row_pixel-=1

                #-----0011-----
                share_2_image_column_pixel=each_column_pixel
                share_2_image_column_pixel=share_2_image_column_pixel*2
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel-=1
                share_2_image_row_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_row_pixel-=1

                #-----0101-----
                share_3_image_column_pixel=each_column_pixel
                share_3_image_column_pixel=share_3_image_column_pixel*2
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel-=1
                share_3_image_row_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_row_pixel-=1

            elif prob>0.2075 and prob<=0.249:
                #----------06----------
                #-----0110-----
                share_1_image_column_pixel=each_column_pixel
                share_1_image_column_pixel=share_1_image_column_pixel*2
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel-=1
                share_1_image_row_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_row_pixel-=1

                #-----0101-----
                share_2_image_column_pixel=each_column_pixel
                share_2_image_column_pixel=share_2_image_column_pixel*2
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel-=1
                share_2_image_row_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_row_pixel-=1

                #-----0011-----
                share_3_image_column_pixel=each_column_pixel
                share_3_image_column_pixel=share_3_image_column_pixel*2
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel-=1
                share_3_image_row_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_row_pixel-=1

            elif prob>0.249 and prob<=0.2905:
                #----------07----------
                #-----0011-----
                share_1_image_column_pixel=each_column_pixel
                share_1_image_column_pixel=share_1_image_column_pixel*2
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel-=1
                share_1_image_row_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_row_pixel-=1

                #-----1010-----
                share_2_image_column_pixel=each_column_pixel
                share_2_image_column_pixel=share_2_image_column_pixel*2
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel-=1
                share_2_image_row_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_row_pixel-=1

                #-----1001-----
                share_3_image_column_pixel=each_column_pixel
                share_3_image_column_pixel=share_3_image_column_pixel*2
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel-=1
                share_3_image_row_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_row_pixel-=1

            elif prob>0.2905 and prob<=0.332:
                #----------08----------
                #-----0011-----
                share_1_image_column_pixel=each_column_pixel
                share_1_image_column_pixel=share_1_image_column_pixel*2
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel-=1
                share_1_image_row_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_row_pixel-=1

                #-----1001-----
                share_2_image_column_pixel=each_column_pixel
                share_2_image_column_pixel=share_2_image_column_pixel*2
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel-=1
                share_2_image_row_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_row_pixel-=1

                #-----1010-----
                share_3_image_column_pixel=each_column_pixel
                share_3_image_column_pixel=share_3_image_column_pixel*2
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel-=1
                share_3_image_row_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_row_pixel-=1

            elif prob>0.332 and prob<=0.3735:
                #----------09----------
                #-----1010-----
                share_1_image_column_pixel=each_column_pixel
                share_1_image_column_pixel=share_1_image_column_pixel*2
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel-=1
                share_1_image_row_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_row_pixel-=1

                #-----0011-----
                share_2_image_column_pixel=each_column_pixel
                share_2_image_column_pixel=share_2_image_column_pixel*2
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel-=1
                share_2_image_row_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_row_pixel-=1

                #-----1001-----
                share_3_image_column_pixel=each_column_pixel
                share_3_image_column_pixel=share_3_image_column_pixel*2
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel-=1
                share_3_image_row_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_row_pixel-=1

            elif prob>0.3735 and prob<=0.415:
                #----------10----------
                #-----1010-----
                share_1_image_column_pixel=each_column_pixel
                share_1_image_column_pixel=share_1_image_column_pixel*2
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel-=1
                share_1_image_row_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_row_pixel-=1

                #-----1001-----
                share_2_image_column_pixel=each_column_pixel
                share_2_image_column_pixel=share_2_image_column_pixel*2
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel-=1
                share_2_image_row_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_row_pixel-=1

                #-----0011-----
                share_3_image_column_pixel=each_column_pixel
                share_3_image_column_pixel=share_3_image_column_pixel*2
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel-=1
                share_3_image_row_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_row_pixel-=1

            elif prob>0.415 and prob<=0.4565:
                #----------11----------
                #-----1001-----
                share_1_image_column_pixel=each_column_pixel
                share_1_image_column_pixel=share_1_image_column_pixel*2
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel-=1
                share_1_image_row_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_row_pixel-=1

                #-----0011-----
                share_2_image_column_pixel=each_column_pixel
                share_2_image_column_pixel=share_2_image_column_pixel*2
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel-=1
                share_2_image_row_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_row_pixel-=1

                #-----1010-----
                share_3_image_column_pixel=each_column_pixel
                share_3_image_column_pixel=share_3_image_column_pixel*2
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel-=1
                share_3_image_row_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_row_pixel-=1

            elif prob>0.4565 and prob<=0.498:
                #----------12----------
                #-----1001-----
                share_1_image_column_pixel=each_column_pixel
                share_1_image_column_pixel=share_1_image_column_pixel*2
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel-=1
                share_1_image_row_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_row_pixel-=1

                #-----1010-----
                share_2_image_column_pixel=each_column_pixel
                share_2_image_column_pixel=share_2_image_column_pixel*2
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel-=1
                share_2_image_row_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_row_pixel-=1

                #-----0011-----
                share_3_image_column_pixel=each_column_pixel
                share_3_image_column_pixel=share_3_image_column_pixel*2
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel-=1
                share_3_image_row_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_row_pixel-=1

            elif prob>0.498 and prob<=0.5395:
                #----------13----------
                #-----1100-----
                share_1_image_column_pixel=each_column_pixel
                share_1_image_column_pixel=share_1_image_column_pixel*2
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel-=1
                share_1_image_row_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_row_pixel-=1

                #-----0101-----
                share_2_image_column_pixel=each_column_pixel
                share_2_image_column_pixel=share_2_image_column_pixel*2
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel-=1
                share_2_image_row_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_row_pixel-=1

                #-----1001-----
                share_3_image_column_pixel=each_column_pixel
                share_3_image_column_pixel=share_3_image_column_pixel*2
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel-=1
                share_3_image_row_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_row_pixel-=1

            elif prob>0.5395 and prob<=0.581:
                #----------14----------
                #-----1100-----
                share_1_image_column_pixel=each_column_pixel
                share_1_image_column_pixel=share_1_image_column_pixel*2
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel-=1
                share_1_image_row_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_row_pixel-=1

                #-----1001-----
                share_2_image_column_pixel=each_column_pixel
                share_2_image_column_pixel=share_2_image_column_pixel*2
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel-=1
                share_2_image_row_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_row_pixel-=1

                #-----0101-----
                share_3_image_column_pixel=each_column_pixel
                share_3_image_column_pixel=share_3_image_column_pixel*2
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel-=1
                share_3_image_row_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_row_pixel-=1
            
            elif prob>0.581 and prob<=0.6225:
                #----------15----------
                #-----0101-----
                share_1_image_column_pixel=each_column_pixel
                share_1_image_column_pixel=share_1_image_column_pixel*2
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel-=1
                share_1_image_row_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_row_pixel-=1

                #-----1100-----
                share_2_image_column_pixel=each_column_pixel
                share_2_image_column_pixel=share_2_image_column_pixel*2
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel-=1
                share_2_image_row_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_row_pixel-=1

                #-----1001-----
                share_3_image_column_pixel=each_column_pixel
                share_3_image_column_pixel=share_3_image_column_pixel*2
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel-=1
                share_3_image_row_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_row_pixel-=1

            elif prob>0.6225 and prob<=0.664:
                #----------16----------
                #-----0101-----
                share_1_image_column_pixel=each_column_pixel
                share_1_image_column_pixel=share_1_image_column_pixel*2
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel-=1
                share_1_image_row_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_row_pixel-=1

                #-----1001-----
                share_2_image_column_pixel=each_column_pixel
                share_2_image_column_pixel=share_2_image_column_pixel*2
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel-=1
                share_2_image_row_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_row_pixel-=1

                #-----1100-----
                share_3_image_column_pixel=each_column_pixel
                share_3_image_column_pixel=share_3_image_column_pixel*2
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel-=1
                share_3_image_row_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_row_pixel-=1

            elif prob>0.664 and prob<=0.7055:
                #----------17----------
                #-----1001-----
                share_1_image_column_pixel=each_column_pixel
                share_1_image_column_pixel=share_1_image_column_pixel*2
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel-=1
                share_1_image_row_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_row_pixel-=1

                #-----1100-----
                share_2_image_column_pixel=each_column_pixel
                share_2_image_column_pixel=share_2_image_column_pixel*2
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel-=1
                share_2_image_row_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_row_pixel-=1

                #-----0101-----
                share_3_image_column_pixel=each_column_pixel
                share_3_image_column_pixel=share_3_image_column_pixel*2
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel-=1
                share_3_image_row_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_row_pixel-=1

            elif prob>0.7055 and prob<=0.747:
                #----------18----------
                #-----1001-----
                share_1_image_column_pixel=each_column_pixel
                share_1_image_column_pixel=share_1_image_column_pixel*2
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel-=1
                share_1_image_row_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_row_pixel-=1

                #-----0101-----
                share_2_image_column_pixel=each_column_pixel
                share_2_image_column_pixel=share_2_image_column_pixel*2
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel-=1
                share_2_image_row_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_row_pixel-=1

                #-----1100-----
                share_3_image_column_pixel=each_column_pixel
                share_3_image_column_pixel=share_3_image_column_pixel*2
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel-=1
                share_3_image_row_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_row_pixel-=1

            elif prob>0.747 and prob<=0.7885:
                #----------19----------
                #-----1100-----
                share_1_image_column_pixel=each_column_pixel
                share_1_image_column_pixel=share_1_image_column_pixel*2
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel-=1
                share_1_image_row_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_row_pixel-=1

                #-----1010-----
                share_2_image_column_pixel=each_column_pixel
                share_2_image_column_pixel=share_2_image_column_pixel*2
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel-=1
                share_2_image_row_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_row_pixel-=1

                #-----0110-----
                share_3_image_column_pixel=each_column_pixel
                share_3_image_column_pixel=share_3_image_column_pixel*2
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel-=1
                share_3_image_row_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_row_pixel-=1

            elif prob>0.7885 and prob<=0.83:
                #----------20----------
                #-----1100-----
                share_1_image_column_pixel=each_column_pixel
                share_1_image_column_pixel=share_1_image_column_pixel*2
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel-=1
                share_1_image_row_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_row_pixel-=1

                #-----0110-----
                share_2_image_column_pixel=each_column_pixel
                share_2_image_column_pixel=share_2_image_column_pixel*2
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel-=1
                share_2_image_row_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_row_pixel-=1

                #-----1010-----
                share_3_image_column_pixel=each_column_pixel
                share_3_image_column_pixel=share_3_image_column_pixel*2
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel-=1
                share_3_image_row_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_row_pixel-=1

            elif prob>0.83 and prob<=0.8715:
                #----------21----------
                #-----1010-----
                share_1_image_column_pixel=each_column_pixel
                share_1_image_column_pixel=share_1_image_column_pixel*2
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel-=1
                share_1_image_row_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_row_pixel-=1
        
                #-----1100-----
                share_2_image_column_pixel=each_column_pixel
                share_2_image_column_pixel=share_2_image_column_pixel*2
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel-=1
                share_2_image_row_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_row_pixel-=1

                #-----0110-----
                share_3_image_column_pixel=each_column_pixel
                share_3_image_column_pixel=share_3_image_column_pixel*2
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel-=1
                share_3_image_row_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_row_pixel-=1

            elif prob>0.8715 and prob<=0.913:
                #----------22----------
                #-----1010-----
                share_1_image_column_pixel=each_column_pixel
                share_1_image_column_pixel=share_1_image_column_pixel*2
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel-=1
                share_1_image_row_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_row_pixel-=1

                #-----0110-----
                share_2_image_column_pixel=each_column_pixel
                share_2_image_column_pixel=share_2_image_column_pixel*2
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel-=1
                share_2_image_row_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_row_pixel-=1

                #-----1100-----
                share_3_image_column_pixel=each_column_pixel
                share_3_image_column_pixel=share_3_image_column_pixel*2
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel-=1
                share_3_image_row_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_row_pixel-=1

            elif prob>0.913 and prob<=0.9545:
                #----------23----------
                #-----0110-----
                share_1_image_column_pixel=each_column_pixel
                share_1_image_column_pixel=share_1_image_column_pixel*2
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel-=1
                share_1_image_row_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_row_pixel-=1

                #-----1100-----
                share_2_image_column_pixel=each_column_pixel
                share_2_image_column_pixel=share_2_image_column_pixel*2
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel-=1
                share_2_image_row_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_row_pixel-=1

                #-----1010-----
                share_3_image_column_pixel=each_column_pixel
                share_3_image_column_pixel=share_3_image_column_pixel*2
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel-=1
                share_3_image_row_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_row_pixel-=1

            else:
                #----------24----------
                #-----0110-----
                share_1_image_column_pixel=each_column_pixel
                share_1_image_column_pixel=share_1_image_column_pixel*2
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel-=1
                share_1_image_row_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_row_pixel-=1

                #-----1010-----
                share_2_image_column_pixel=each_column_pixel
                share_2_image_column_pixel=share_2_image_column_pixel*2
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel-=1
                share_2_image_row_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_row_pixel-=1

                #-----1100-----
                share_3_image_column_pixel=each_column_pixel
                share_3_image_column_pixel=share_3_image_column_pixel*2
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel-=1
                share_3_image_row_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_row_pixel-=1


        else:  # Pixel is Black
            if prob>=0 and prob<=0.0415:
                #----------01----------
                #-----1100-----
                share_1_image_column_pixel=each_column_pixel
                share_1_image_column_pixel=share_1_image_column_pixel*2
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel-=1
                share_1_image_row_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_row_pixel-=1

                #-----1010-----
                share_2_image_column_pixel=each_column_pixel
                share_2_image_column_pixel=share_2_image_column_pixel*2
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel-=1
                share_2_image_row_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_row_pixel-=1

                #-----1001-----
                share_3_image_column_pixel=each_column_pixel
                share_3_image_column_pixel=share_3_image_column_pixel*2
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel-=1
                share_3_image_row_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_row_pixel-=1

            elif prob>0.0415 and prob<=0.083:
                #----------02----------
                #-----1100-----
                share_1_image_column_pixel=each_column_pixel
                share_1_image_column_pixel=share_1_image_column_pixel*2
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel-=1
                share_1_image_row_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_row_pixel-=1

                #-----1001-----
                share_2_image_column_pixel=each_column_pixel
                share_2_image_column_pixel=share_2_image_column_pixel*2
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel-=1
                share_2_image_row_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_row_pixel-=1

                #-----1010-----
                share_3_image_column_pixel=each_column_pixel
                share_3_image_column_pixel=share_3_image_column_pixel*2
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel-=1
                share_3_image_row_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_row_pixel-=1

            elif prob>0.083 and prob<=0.1245:
                #----------03----------
                #-----1010-----
                share_1_image_column_pixel=each_column_pixel
                share_1_image_column_pixel=share_1_image_column_pixel*2
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel-=1
                share_1_image_row_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_row_pixel-=1

                #-----1100-----
                share_2_image_column_pixel=each_column_pixel
                share_2_image_column_pixel=share_2_image_column_pixel*2
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel-=1
                share_2_image_row_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_row_pixel-=1

                #-----1001-----
                share_3_image_column_pixel=each_column_pixel
                share_3_image_column_pixel=share_3_image_column_pixel*2
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel-=1
                share_3_image_row_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_row_pixel-=1

            elif prob>0.1245 and prob<=0.166:
                #----------04----------
                #-----1010-----
                share_1_image_column_pixel=each_column_pixel
                share_1_image_column_pixel=share_1_image_column_pixel*2
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel-=1
                share_1_image_row_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_row_pixel-=1

                #-----1001-----
                share_2_image_column_pixel=each_column_pixel
                share_2_image_column_pixel=share_2_image_column_pixel*2
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel-=1
                share_2_image_row_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_row_pixel-=1

                #-----1100-----
                share_3_image_column_pixel=each_column_pixel
                share_3_image_column_pixel=share_3_image_column_pixel*2
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel-=1
                share_3_image_row_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_row_pixel-=1

            elif prob>0.166 and prob<=0.2075:
                #----------05----------
                #-----1001-----
                share_1_image_column_pixel=each_column_pixel
                share_1_image_column_pixel=share_1_image_column_pixel*2
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel-=1
                share_1_image_row_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_row_pixel-=1

                #-----1100-----
                share_2_image_column_pixel=each_column_pixel
                share_2_image_column_pixel=share_2_image_column_pixel*2
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel-=1
                share_2_image_row_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_row_pixel-=1

                #-----1010-----
                share_3_image_column_pixel=each_column_pixel
                share_3_image_column_pixel=share_3_image_column_pixel*2
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel-=1
                share_3_image_row_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_row_pixel-=1

            elif prob>0.2075 and prob<=0.249:
                #----------06----------
                #-----1001-----
                share_1_image_column_pixel=each_column_pixel
                share_1_image_column_pixel=share_1_image_column_pixel*2
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel-=1
                share_1_image_row_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_row_pixel-=1

                #-----1010-----
                share_2_image_column_pixel=each_column_pixel
                share_2_image_column_pixel=share_2_image_column_pixel*2
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel-=1
                share_2_image_row_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_row_pixel-=1

                #-----1100-----
                share_3_image_column_pixel=each_column_pixel
                share_3_image_column_pixel=share_3_image_column_pixel*2
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel-=1
                share_3_image_row_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_row_pixel-=1

            elif prob>0.249 and prob<=0.2905:
                #----------07----------
                #-----1100-----
                share_1_image_column_pixel=each_column_pixel
                share_1_image_column_pixel=share_1_image_column_pixel*2
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel-=1
                share_1_image_row_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_row_pixel-=1

                #-----0101-----
                share_2_image_column_pixel=each_column_pixel
                share_2_image_column_pixel=share_2_image_column_pixel*2
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel-=1
                share_2_image_row_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_row_pixel-=1

                #-----0110-----
                share_3_image_column_pixel=each_column_pixel
                share_3_image_column_pixel=share_3_image_column_pixel*2
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel-=1
                share_3_image_row_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_row_pixel-=1

            elif prob>0.2905 and prob<=0.332:
                #----------08----------
                #-----1100-----
                share_1_image_column_pixel=each_column_pixel
                share_1_image_column_pixel=share_1_image_column_pixel*2
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel-=1
                share_1_image_row_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_row_pixel-=1

                #-----0110-----
                share_2_image_column_pixel=each_column_pixel
                share_2_image_column_pixel=share_2_image_column_pixel*2
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel-=1
                share_2_image_row_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_row_pixel-=1

                #-----0101-----
                share_3_image_column_pixel=each_column_pixel
                share_3_image_column_pixel=share_3_image_column_pixel*2
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel-=1
                share_3_image_row_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_row_pixel-=1

            elif prob>0.332 and prob<=0.3735:
                #----------09----------
                #-----0101-----
                share_1_image_column_pixel=each_column_pixel
                share_1_image_column_pixel=share_1_image_column_pixel*2
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel-=1
                share_1_image_row_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_row_pixel-=1

                #-----1100-----
                share_2_image_column_pixel=each_column_pixel
                share_2_image_column_pixel=share_2_image_column_pixel*2
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel-=1
                share_2_image_row_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_row_pixel-=1

                #-----0110-----
                share_3_image_column_pixel=each_column_pixel
                share_3_image_column_pixel=share_3_image_column_pixel*2
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel-=1
                share_3_image_row_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_row_pixel-=1

            elif prob>0.3735 and prob<=0.415:
                #----------10----------
                #-----0101-----
                share_1_image_column_pixel=each_column_pixel
                share_1_image_column_pixel=share_1_image_column_pixel*2
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel-=1
                share_1_image_row_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_row_pixel-=1

                #-----0110-----
                share_2_image_column_pixel=each_column_pixel
                share_2_image_column_pixel=share_2_image_column_pixel*2
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel-=1
                share_2_image_row_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_row_pixel-=1

                #-----1100-----
                share_3_image_column_pixel=each_column_pixel
                share_3_image_column_pixel=share_3_image_column_pixel*2
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel-=1
                share_3_image_row_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_row_pixel-=1

            elif prob>0.415 and prob<=0.4565:
                #----------11----------
                #-----0110-----
                share_1_image_column_pixel=each_column_pixel
                share_1_image_column_pixel=share_1_image_column_pixel*2
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel-=1
                share_1_image_row_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_row_pixel-=1

                #-----1100-----
                share_2_image_column_pixel=each_column_pixel
                share_2_image_column_pixel=share_2_image_column_pixel*2
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel-=1
                share_2_image_row_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_row_pixel-=1

                #-----0101-----
                share_3_image_column_pixel=each_column_pixel
                share_3_image_column_pixel=share_3_image_column_pixel*2
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel-=1
                share_3_image_row_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_row_pixel-=1

            elif prob>0.4565 and prob<=0.498:
                #----------12----------
                #-----0110-----
                share_1_image_column_pixel=each_column_pixel
                share_1_image_column_pixel=share_1_image_column_pixel*2
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel-=1
                share_1_image_row_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_row_pixel-=1

                #-----0101-----
                share_2_image_column_pixel=each_column_pixel
                share_2_image_column_pixel=share_2_image_column_pixel*2
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel-=1
                share_2_image_row_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_row_pixel-=1

                #-----1100-----
                share_3_image_column_pixel=each_column_pixel
                share_3_image_column_pixel=share_3_image_column_pixel*2
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel-=1
                share_3_image_row_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_row_pixel-=1

            elif prob>0.498 and prob<=0.5395:
                #----------13----------
                #-----0011-----
                share_1_image_column_pixel=each_column_pixel
                share_1_image_column_pixel=share_1_image_column_pixel*2
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel-=1
                share_1_image_row_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_row_pixel-=1

                #-----1010-----
                share_2_image_column_pixel=each_column_pixel
                share_2_image_column_pixel=share_2_image_column_pixel*2
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel-=1
                share_2_image_row_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_row_pixel-=1

                #-----0110-----
                share_3_image_column_pixel=each_column_pixel
                share_3_image_column_pixel=share_3_image_column_pixel*2
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel-=1
                share_3_image_row_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_row_pixel-=1

            elif prob>0.5395 and prob<=0.581:
                #----------14----------
                #-----0011-----
                share_1_image_column_pixel=each_column_pixel
                share_1_image_column_pixel=share_1_image_column_pixel*2
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel-=1
                share_1_image_row_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_row_pixel-=1

                #-----0110-----
                share_2_image_column_pixel=each_column_pixel
                share_2_image_column_pixel=share_2_image_column_pixel*2
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel-=1
                share_2_image_row_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_row_pixel-=1

                #-----1010-----
                share_3_image_column_pixel=each_column_pixel
                share_3_image_column_pixel=share_3_image_column_pixel*2
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel-=1
                share_3_image_row_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_row_pixel-=1

            elif prob>0.581 and prob<=0.6225:
                #----------15----------
                #-----1010-----
                share_1_image_column_pixel=each_column_pixel
                share_1_image_column_pixel=share_1_image_column_pixel*2
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel-=1
                share_1_image_row_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_row_pixel-=1

                #-----0011-----
                share_2_image_column_pixel=each_column_pixel
                share_2_image_column_pixel=share_2_image_column_pixel*2
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel-=1
                share_2_image_row_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_row_pixel-=1

                #-----0110-----
                share_3_image_column_pixel=each_column_pixel
                share_3_image_column_pixel=share_3_image_column_pixel*2
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel-=1
                share_3_image_row_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_row_pixel-=1

            elif prob>0.6225 and prob<=0.664:
                #----------16----------
                #-----1010-----
                share_1_image_column_pixel=each_column_pixel
                share_1_image_column_pixel=share_1_image_column_pixel*2
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel-=1
                share_1_image_row_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_row_pixel-=1

                #-----0110-----
                share_2_image_column_pixel=each_column_pixel
                share_2_image_column_pixel=share_2_image_column_pixel*2
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel-=1
                share_2_image_row_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_row_pixel-=1

                #-----0011-----
                share_3_image_column_pixel=each_column_pixel
                share_3_image_column_pixel=share_3_image_column_pixel*2
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel-=1
                share_3_image_row_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_row_pixel-=1

            elif prob>0.664 and prob<=0.7055:
                #----------17----------
                #-----0110-----
                share_1_image_column_pixel=each_column_pixel
                share_1_image_column_pixel=share_1_image_column_pixel*2
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel-=1
                share_1_image_row_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_row_pixel-=1

                #-----0011-----
                share_2_image_column_pixel=each_column_pixel
                share_2_image_column_pixel=share_2_image_column_pixel*2
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel-=1
                share_2_image_row_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_row_pixel-=1

                #-----1010-----
                share_3_image_column_pixel=each_column_pixel
                share_3_image_column_pixel=share_3_image_column_pixel*2
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel-=1
                share_3_image_row_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_row_pixel-=1

            elif prob>0.7055 and prob<=0.747:
                #----------18----------
                #-----0110-----
                share_1_image_column_pixel=each_column_pixel
                share_1_image_column_pixel=share_1_image_column_pixel*2
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel-=1
                share_1_image_row_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_row_pixel-=1

                #-----1010-----
                share_2_image_column_pixel=each_column_pixel
                share_2_image_column_pixel=share_2_image_column_pixel*2
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel-=1
                share_2_image_row_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_row_pixel-=1

                #-----0011-----
                share_3_image_column_pixel=each_column_pixel
                share_3_image_column_pixel=share_3_image_column_pixel*2
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel-=1
                share_3_image_row_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_row_pixel-=1

            elif prob>0.747 and prob<=0.7885:
                #----------19----------
                #-----0011-----
                share_1_image_column_pixel=each_column_pixel
                share_1_image_column_pixel=share_1_image_column_pixel*2
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel-=1
                share_1_image_row_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_row_pixel-=1

                #-----0101-----
                share_2_image_column_pixel=each_column_pixel
                share_2_image_column_pixel=share_2_image_column_pixel*2
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel-=1
                share_2_image_row_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_row_pixel-=1

                #-----1001-----
                share_3_image_column_pixel=each_column_pixel
                share_3_image_column_pixel=share_3_image_column_pixel*2
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel-=1
                share_3_image_row_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_row_pixel-=1

            elif prob>0.7885 and prob<=0.83:
                #----------20----------
                #-----0011-----
                share_1_image_column_pixel=each_column_pixel
                share_1_image_column_pixel=share_1_image_column_pixel*2
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel-=1
                share_1_image_row_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_row_pixel-=1

                #-----1001-----
                share_2_image_column_pixel=each_column_pixel
                share_2_image_column_pixel=share_2_image_column_pixel*2
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel-=1
                share_2_image_row_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_row_pixel-=1

                #-----0101-----
                share_3_image_column_pixel=each_column_pixel
                share_3_image_column_pixel=share_3_image_column_pixel*2
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel-=1
                share_3_image_row_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_row_pixel-=1

            elif prob>0.83 and prob<=0.8715:
                #----------21----------
                #-----0101-----
                share_1_image_column_pixel=each_column_pixel
                share_1_image_column_pixel=share_1_image_column_pixel*2
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel-=1
                share_1_image_row_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_row_pixel-=1

                #-----0011-----
                share_2_image_column_pixel=each_column_pixel
                share_2_image_column_pixel=share_2_image_column_pixel*2
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel-=1
                share_2_image_row_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_row_pixel-=1

                #-----1001-----
                share_3_image_column_pixel=each_column_pixel
                share_3_image_column_pixel=share_3_image_column_pixel*2
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel-=1
                share_3_image_row_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_row_pixel-=1

            elif prob>0.8715 and prob<=0.913:
                #----------22----------
                #-----0101-----
                share_1_image_column_pixel=each_column_pixel
                share_1_image_column_pixel=share_1_image_column_pixel*2
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel-=1
                share_1_image_row_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_row_pixel-=1

                #-----1001-----
                share_2_image_column_pixel=each_column_pixel
                share_2_image_column_pixel=share_2_image_column_pixel*2
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel-=1
                share_2_image_row_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_row_pixel-=1

                #-----0011-----
                share_3_image_column_pixel=each_column_pixel
                share_3_image_column_pixel=share_3_image_column_pixel*2
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel-=1
                share_3_image_row_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_row_pixel-=1

            elif prob>0.913 and prob<=0.9545:
                #----------23----------
                #-----1001-----
                share_1_image_column_pixel=each_column_pixel
                share_1_image_column_pixel=share_1_image_column_pixel*2
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel-=1
                share_1_image_row_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_row_pixel-=1

                #-----0011-----
                share_2_image_column_pixel=each_column_pixel
                share_2_image_column_pixel=share_2_image_column_pixel*2
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel-=1
                share_2_image_row_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_row_pixel-=1

                #-----0101-----
                share_3_image_column_pixel=each_column_pixel
                share_3_image_column_pixel=share_3_image_column_pixel*2
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel-=1
                share_3_image_row_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_row_pixel-=1

            else:
                #----------24----------
                #-----1001-----
                share_1_image_column_pixel=each_column_pixel
                share_1_image_column_pixel=share_1_image_column_pixel*2
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel-=1
                share_1_image_row_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
                share_1_image_row_pixel-=1

                #-----0101-----
                share_2_image_column_pixel=each_column_pixel
                share_2_image_column_pixel=share_2_image_column_pixel*2
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_column_pixel-=1
                share_2_image_row_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=255
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,share_2_image_row_pixel]=0
                share_2_image_row_pixel-=1

                #-----0011-----
                share_3_image_column_pixel=each_column_pixel
                share_3_image_column_pixel=share_3_image_column_pixel*2
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=255
                share_3_image_column_pixel-=1
                share_3_image_row_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_column_pixel+=1
                share_3_image_pixels[share_3_image_column_pixel,share_3_image_row_pixel]=0
                share_3_image_row_pixel-=1
        
        

share_1_image.save('a_share_1.png')
share_2_image.save('a_share_2.png')
share_3_image.save('a_share_3.png')

#---------------Share Images Combined---------------
share_images_combined = Image.new("L",(share_image_width,share_image_height))
share_images_combined_pixels = share_images_combined.load()

for each_row_pixel in range(share_image_height):
    for each_column_pixel in range(share_image_width):
        if (share_1_image_pixels[each_column_pixel,each_row_pixel]+share_2_image_pixels[each_column_pixel,each_row_pixel]+share_3_image_pixels[each_column_pixel,each_row_pixel])==255:
            share_images_combined_pixels[each_column_pixel,each_row_pixel]= 0
        else:
            share_images_combined_pixels[each_column_pixel,each_row_pixel]= share_1_image_pixels[each_column_pixel,each_row_pixel]+share_2_image_pixels[each_column_pixel,each_row_pixel]+share_3_image_pixels[each_column_pixel,each_row_pixel]

share_images_combined.save('a_share_images_combined.png')




#-----0011-----
#share_1_image_column_pixel=each_column_pixel
#share_1_image_column_pixel=share_1_image_column_pixel*2
#share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
#share_1_image_column_pixel+=1
#share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
#share_1_image_column_pixel-=1
#share_1_image_row_pixel+=1
#share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
#share_1_image_column_pixel+=1
#share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
#share_1_image_row_pixel-=1

#-----1100-----
#share_1_image_column_pixel=each_column_pixel
#share_1_image_column_pixel=share_1_image_column_pixel*2
#share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
#share_1_image_column_pixel+=1
#share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
#share_1_image_column_pixel-=1
#share_1_image_row_pixel+=1
#share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
#share_1_image_column_pixel+=1
#share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
#share_1_image_row_pixel-=1

#-----0101-----
#share_1_image_column_pixel=each_column_pixel
#share_1_image_column_pixel=share_1_image_column_pixel*2
#share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
#share_1_image_column_pixel+=1
#share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
#share_1_image_column_pixel-=1
#share_1_image_row_pixel+=1
#share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
#share_1_image_column_pixel+=1
#share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
#share_1_image_row_pixel-=1

#-----1010-----
#share_1_image_column_pixel=each_column_pixel
#share_1_image_column_pixel=share_1_image_column_pixel*2
#share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
#share_1_image_column_pixel+=1
#share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
#share_1_image_column_pixel-=1
#share_1_image_row_pixel+=1
#share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
#share_1_image_column_pixel+=1
#share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
#share_1_image_row_pixel-=1

#-----0110-----
#share_1_image_column_pixel=each_column_pixel
#share_1_image_column_pixel=share_1_image_column_pixel*2
#share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
#share_1_image_column_pixel+=1
#share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
#share_1_image_column_pixel-=1
#share_1_image_row_pixel+=1
#share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
#share_1_image_column_pixel+=1
#share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
#share_1_image_row_pixel-=1

#-----1001-----
#share_1_image_column_pixel=each_column_pixel
#share_1_image_column_pixel=share_1_image_column_pixel*2
#share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
#share_1_image_column_pixel+=1
#share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
#share_1_image_column_pixel-=1
#share_1_image_row_pixel+=1
#share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=255
#share_1_image_column_pixel+=1
#share_1_image_pixels[share_1_image_column_pixel,share_1_image_row_pixel]=0
#share_1_image_row_pixel-=1