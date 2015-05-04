import sqlite3
import urllib
from PIL import Image
import glob, os, sys

SIZE = 256, 256

sql = sqlite3.connect('cactus.db')
cur = sql.cursor()

cur.execute('DELETE FROM posts WHERE url IS NULL OR url NOT LIKE \"%.jpg\"')
cur.execute('SELECT url FROM posts')
all_urls = [item[0] for item in cur.fetchall()]

num_cactuss = 0


for url_num in range(len(all_urls)):
        try:
                urllib.urlretrieve(all_urls[url_num],"./bad_cactus/cactus{}.jpg".format(url_num)) 
        except IOError:
                print("Couldn't get cactus{}".format(url_num))

cactus = glob.glob("./bad_cactus/*.jpg")

for cactus_num in range(len(cactus)):
        try:
                im = Image.open(cactus[cactus_num])
                im.thumbnail(SIZE)
                im.save("./good_cactus/cactus{}.jpg".format(cactus_num))
        except IOError as e:
                print("Thumbnail failed for cactus {}".format(cactus_num))
