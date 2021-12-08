import os

for root, dirs, files in os.walk(os.path.abspath("./fonts/")):
    for file in files:
        files = (os.path.join(root, file))
        print(dirs)
        commannd = "fontforge -lang py -script ligaturize.py" + \
            files + "--output-dir = ../final - -output-name = Liga"
