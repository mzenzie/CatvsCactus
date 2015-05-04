import random, glob, os, sys, shutil

catfiles = "./good_cats/"
cactusfiles = "./good_cactus/"

traindata = "./traindata/"
testdata = "./testdata/"

cats = glob.glob("./good_cats/*.jpg")
cacti = glob.glob("./good_cactus/*.jpg")

for cat in cats:
    if(random.random() > 0.75):
        print("moving to test")
        shutil.copyfile(cat, testdata + cat.split("/")[-1])
    else:
        shutil.copyfile(cat, traindata + cat.split("/")[-1])

for cactus in cacti:
    if(random.random() > 0.75):
        shutil.copyfile(cactus, testdata + cactus.split("/")[-1])
    else:
        shutil.copyfile(cactus, traindata + cactus.split("/")[-1])
                        
