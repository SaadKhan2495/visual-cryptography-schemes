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
share_1_image = Image.new("L",(input_image_width * 2,input_image_height))
share_1_image_pixels = share_1_image.load()
share_2_image = Image.new("L",(input_image_width * 2,input_image_height))
share_2_image_pixels = share_2_image.load()
share_3_image = Image.new("L",(input_image_width * 2,input_image_height))
share_3_image_pixels = share_3_image.load()

for each_row_pixel in range(input_image_height):
    share_1_image_column_pixel = -1
    share_2_image_column_pixel = -1
    for each_column_pixel in range(input_image_width):
        prob=random.uniform(0,1)
        if pixels[each_column_pixel,each_row_pixel] > 127.5:
            if prob>=0.5:
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,each_row_pixel]=255
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,each_row_pixel]=0
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,each_row_pixel]=255
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,each_row_pixel]=0
            else:
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,each_row_pixel]=0
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,each_row_pixel]=255
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,each_row_pixel]=0
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,each_row_pixel]=255
        else:
            if prob>=0.5:
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,each_row_pixel]=255
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,each_row_pixel]=0
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,each_row_pixel]=0
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,each_row_pixel]=255
            else:
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,each_row_pixel]=0
                share_1_image_column_pixel+=1
                share_1_image_pixels[share_1_image_column_pixel,each_row_pixel]=255
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,each_row_pixel]=255
                share_2_image_column_pixel+=1
                share_2_image_pixels[share_2_image_column_pixel,each_row_pixel]=0

share_1_image.save('a_share_1.png')
share_2_image.save('a_share_2.png')

#---------------Share Images Combined---------------
share_images_combined = Image.new("L",(input_image_width * 2,input_image_height))
share_images_combined_pixels = share_images_combined.load()

for each_row_pixel in range(input_image_height):
    for each_column_pixel in range(input_image_width*2):
        if (share_1_image_pixels[each_column_pixel,each_row_pixel]+share_2_image_pixels[each_column_pixel,each_row_pixel])==255:
            share_images_combined_pixels[each_column_pixel,each_row_pixel]= 0
        else:
            share_images_combined_pixels[each_column_pixel,each_row_pixel]= share_1_image_pixels[each_column_pixel,each_row_pixel]+share_2_image_pixels[each_column_pixel,each_row_pixel]

share_images_combined.save('a_share_images_combined.png')