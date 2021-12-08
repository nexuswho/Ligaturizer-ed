import os
print("Nerdfont patching")
for i, j, y in os.walk('.'):
    if i != ".":
        print(i)
        command = "fontforge --script nerdfont-patcher.py " + i + " " + i
        # os.system(command)
        command2 = "cp -rf " + i + " ../Ligaturizer/fonts"
        print(command2)
