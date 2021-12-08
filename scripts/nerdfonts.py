import os
print("Nerdfont patching")
for i, j, y in os.walk('.'):
    if i != ".":
        print(i)
        command = "python3 ../nerdfont-patcher/nerdfont-patcher.py " + i + " ../build"
        os.system(command)
