import os
path = r'.'
list_of_files = []

for root, dirs, files in os.walk(path):
    for file in files:
        list_of_files.append(os.path.join(root, file))
for name in list_of_files:
    print(name)
    commandd = "fontforge -script ../nerd-fonts-master/font-patcher  " + name
    print(commandd)
    os.system(commandd)
