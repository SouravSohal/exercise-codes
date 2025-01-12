import os
def clearclutter(foldername):
    os.chdir(foldername)
    counter=1
    for item in os.listdir(foldername):
        if item.endswith('.png'):
            os.replace(item, f"{counter}.png")
            print(f"Renamed: {item} -> {counter}.png")
            counter+=1
foldername="path/to/folder"
clearclutter(foldername)