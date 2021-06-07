# visual-cryptography-schemes

This repository contains scripts which can be used to implement the following visual cryptographic schemes:
- 2 out of 2 scheme
- 3 out of 3 scheme

There are currently 5 python scripts:
- ```2_out_of_2_scheme.py``` Generates 2 shares of an input black and white image.
- ```3_out_of_3_scheme.py``` Generates 3 shares of an input black and white image.
- ```random_2_out_of_2_scheme.py``` Generates a specified number of random shares for the 2 out of 2 scheme.
- ```random_3_out_of_3_scheme.py``` Generates a specified number of random shares for the 3 out of 3 scheme.
- ```png_to_jpg.py``` Used to convert png images to jpg format.

## Running the scipts

### 2_out_of_2_scheme.py
This script requires a path to a directory which contains black and white images (whose shares need to be generated) in jpg format.
```console
C:\visual-cryptography-schemes> python3 .\2_out_of_2_scheme.py .\path_to_input_directory\
```

### 3_out_of_3_scheme.py
This script requires a path to a directory which contains black and white images (whose shares need to be generated) in jpg format.
```console
C:\visual-cryptography-schemes> python3 .\3_out_of_3_scheme.py .\path_to_input_directory\
```

### random_2_out_of_2_scheme.py
This script requires a number which will be the total number of random shares generated by the script.
```console
C:\visual-cryptography-schemes> python3 .\random_2_out_of_2_scheme.py 10
```

### random_3_out_of_3_scheme.py
This script requires a number which will be the total number of random shares generated by the script.
```console
C:\visual-cryptography-schemes> python3 .\random_3_out_of_3_scheme.py 10
```

### png_to_jpg.py
This script requires a path to a directory which contains black and white images in png format. It will convert these images and store the result in a directory ```jpg_files```.
```console
C:\visual-cryptography-schemes>  python3 .\png_to_jpg.py .\path_to_input_directory\
```

## Output
An ```output``` directory will be generated when a script is run. The scripts will generate and store their out in the respective directory within this ```output``` directory.
