import sqlite3
import urllib
from PIL import Image
import glob, os, sys

SIZE = 256, 256

sql = sqlite3.connect('cats.db')
cur = sql.cursor()

cur.execute('DELETE FROM posts WHERE url IS NULL OR url NOT LIKE \"%.jpg\"')
cur.execute('SELECT url FROM posts')
all_urls = [item[0] for item in cur.fetchall()]

num_cats = 0


for url_num in range(len(all_urls)):
        try:
                urllib.urlretrieve(all_urls[url_num],"./bad_cats/cat{}.jpg".format(url_num)) 
        except IOError:
                print("Couldn't get cat{}".format(url_num))

cats = glob.glob("./bad_cats/*.jpg")

for cat_num in range(len(cats)):
        try:
                im = Image.open(cats[cat_num])
                im.thumbnail(SIZE)
                im.save("./good_cats/cat{}.jpg".format(cat_num))
        except IOError as e:
                print("Thumbnail failed for cat {}".format(cat_num))
