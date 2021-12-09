import os
os.system("ls -la to-be-patched")
for root, dirs, files in os.walk(os.path.abspath("./to-be-patched/")):
    for file in files:
        filee = (os.path.join(root, file))
        fille = f'"{filee}"'
        file = f'"{file}"'
        commannd = "fontforge -lang py -script ligaturize.py " + \
            filee + " --output-dir = ../final - -output-name=" + file
        print(filee)
        os.system(commannd)
