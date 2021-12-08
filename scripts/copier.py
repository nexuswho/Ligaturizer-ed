import os
os.system("ls -la")
for root, dirs, files in os.walk(os.path.abspath("../fonts/")):
    for file in files:
        filee = (os.path.join(root, file))
        if "Nerd" in files:
            print(files)
            commannd = "cp -vvf " + filee + " fonts"
            os.system(commannd)
