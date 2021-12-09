import os
os.system("ls -la to-be-patched")
for root, dirs, files in os.walk(os.path.abspath("./to-be-patched/")):
    for file in files:
        print(file)
        filee = (os.path.join(root, file))
        print(filee)
        filles = f'"{filee}"'
        print(filles)
        file = f'"{file}"'
        print(file)
        commannd = "fontforge -lang py -script ligaturize.py " + \
            filles + " --output-dir = ../final - -output-name=" + file
        # os.system(commannd)
