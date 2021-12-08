import os
for root, dirs, files in os.walk(os.path.abspath("../fonts/")):
    for file in files:
        files = (os.path.join(root, file))
        commannd = "cp -f " + files + " ../Ligaturizer/fonts"
        os.system(commannd)
