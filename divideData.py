import os
import shutil
import json
from collections import defaultdict
from shutil import copyfile


with open('iwildcam2020_train_annotations.json') as json_file:
    data = json.load(json_file)['annotations']
    print(">>> reading", len(data), "images")

pathMapping = defaultdict(list)

for ele in data:
    # print(ele["category_id"])
    pathMapping[ele['category_id']].append(ele['image_id'])


current_directory = os.path.join(os.getcwd(), "trainDivided")
if not os.path.exists(current_directory):
    os.makedirs(current_directory)

for ele in pathMapping:
    final_directory = os.path.join(current_directory, str(ele))
    if not os.path.exists(final_directory):
        os.makedirs(final_directory)

length = 0
for key, val in pathMapping.items():
    length += len(val)

train_directory = os.path.join(os.getcwd(), "train")

for key, val in pathMapping.items():
    for image in val:
        dst = os.path.join(current_directory, str(key), image + ".jpg")
        src = os.path.join(train_directory, image + ".jpg")
        copyfile(src, dst)