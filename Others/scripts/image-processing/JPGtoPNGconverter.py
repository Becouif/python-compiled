import sys
import os

from PIL import Image

# steps
# grab first and second argument
# check if folder in second arg exists, if not create it
# loop through the folder given in first argument
# convert the jpg images to png
# save it to the new folder in second argument


n = len(sys.argv)
first_folder = sys.argv[1]
second_folder = sys.argv[2]

# print(f'this is first argument {first_folder}')
# print(f'this is second argument {second_folder}')

# check if dir exist
# print(os.path.isdir(second_folder))
# print(os.path.isdir(first_folder))

if not (os.path.isdir(second_folder)):
    os.mkdir(second_folder)

# my_dir = os.fsencode(first_folder)

for filename in os.listdir(first_folder):
    # open file name from the folder
    img = Image.open(f'{first_folder}/{filename}')
    # get d name without extention
    clean_name = os.path.splitext(filename)
    # print(clean_name)
    img.save(f'{second_folder}/{clean_name}', 'png')

print('All done, Thank you!!!')





