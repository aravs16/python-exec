import os
import shutil

images_dir = '/Users/program/Desktop/images/'
desktop_dir = '/Users/program/Desktop/'

file_names = os.listdir('/Users/program/Desktop/')

for file_ in file_names:
    split_filename = file_.split('.')
    if len(split_filename) == 2:
        extension = split_filename[1]

        if extension in ['jpeg','png','gif']:
            print(desktop_dir+file_)
            shutil.move(desktop_dir+file_, images_dir)

