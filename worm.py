import os.path as path
import  os
import shutil
def worm ():
    for s, p, d in os.walk("E:/"):
        if path.isdir(s):
            try:
                shutil.copy("D:/mesh worm ana.txt", s)
            except:
                continue
def anti_worm ():
    for s, p, d in os.walk("E:/"):
        if path.isdir(s):
            if path.exists(path.join(s,"mesh worm ana.txt")):
                try:
                    os.remove(path.join(s,"mesh worm ana.txt"))
                except:
                    continue
anti_worm()