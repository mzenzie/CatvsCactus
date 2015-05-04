from PIL import Image
import glob, os, sys

SIZE = 256, 256

pics = glob.glob("./bad_pics/*.jpg")

for pic_num in range(len(pics)):
        try:
                im = Image.open(pics[pic_num])
                im.thumbnail(SIZE)
                im.save("./good_pics/pic{}.jpg".format(pic_num))
        except IOError as e:
                print("Thumbnail failed for pic {}".format(pic_num))
