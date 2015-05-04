import glob

testfile = open("./testdata.txt",'w')

test_images =  glob.glob("./testdata/*")

testtext = ""

for image in test_images:
    if "cactus" in image:
        testtext += image.split("/")[-1] + " 0\n"
    else:
        testtext += image.split("/")[-1] + " 1\n"

testfile.write(testtext)
testfile.close()

trainfile = open("./traindata.txt",'w')

train_images =  glob.glob("./traindata/*")

traintext = ""

for image in train_images:
    if "cactus" in image:
        traintext += image.split("/")[-1] + " 0\n"
    else:
        traintext += image.split("/")[-1] + " 1\n"

trainfile.write(traintext)
trainfile.close()
