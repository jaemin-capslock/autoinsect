'''
Saves the images into an array. Then shuffles the images randomly, and creates directories & copies the images.
'''

import os
import random
import shutil

core = r"E:/insect_dataset/"


def create_directory(source, dir_name: str):
    train_directory = ''
    validation_directory = ''
    test_directory = ''

    train_directory: str = source + r"_train/" + dir_name
    validation_directory: str = source + r"_validation/" + dir_name
    test_directory: str = source + r"_test/" + dir_name
    try:
        os.mkdir(train_directory)
        os.mkdir(validation_directory)
        os.mkdir(test_directory)
    except OSError:
        print("path" + core + dir_name + r"/" + "already exists")
    print (train_directory)
    return train_directory, validation_directory, test_directory


def load_images(source, img_folder_name : str):
    img_dir = source + img_folder_name + r"/"
    count = 0
    image_list = []
    for i in os.listdir(img_dir):
        image = img_dir + i
        if os.path.getsize(image) > 0:
            count += 1
            image_list.append(i)
            if count % 100 == 0:
                print(str(count) + " th image processing.")
        else:
            print("image file size is 0, not valid!")
    return image_list


def sort_images(source: str, folder_name: str, val_size, test_size):
    train_dir, val_dir, test_dir = create_directory(source, folder_name)
    list_of_sorted_images = load_images(source, folder_name)
    image_dir = source + folder_name + r"/"

    train_length = int(len(list_of_sorted_images) * (1 - (val_size + test_size)))
    val_length = int(len(list_of_sorted_images) * val_size)
    test_length = int(len(list_of_sorted_images) * test_size)
    shuffled_dataset = random.sample(list_of_sorted_images, len(list_of_sorted_images))
    train_dataset = shuffled_dataset[0:train_length]
    validation_dataset = shuffled_dataset[train_length:(train_length + val_length)]
    test_dataset = shuffled_dataset[:test_length]

    print("The length of the total image set of " + folder_name + " is " + str(len(list_of_sorted_images)) + ".")
    print("sorting files at training folder . . . . .")
    for filename in train_dataset:
        file = image_dir + filename
        destination = os.path.join(train_dir, filename)
        shutil.copyfile(file, destination)
    print("sorting files at validation folder . . . . .")
    for filename in validation_dataset:
        file = image_dir + filename
        destination = os.path.join(val_dir, filename)
        shutil.copyfile(file, destination)
    print("sorting files at test folder . . . . .")
    for filename in test_dataset:
        file = image_dir + filename
        destination = os.path.join(test_dir, filename)
        shutil.copyfile(file, destination)

def get_subdirectories(source):
    return [name for name in os.listdir(source)
            if os.path.isdir(os.path.join(source, name))]

names_list = get_subdirectories(core)
if r"urls" in names_list:
    names_list.remove(r"urls")
try:
    os.mkdir(core + r"_train/")
    os.mkdir(core + r"_validation/")
    os.mkdir(core + r"_test/")
except OSError:
    print("folder(s) already exists.")
    pass

target_val_size = .1
target_test_size = .1
for name in names_list:
    sort_images(core, name, target_val_size, target_test_size)