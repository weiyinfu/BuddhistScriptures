import os
from os.path import *

files = []
for i in os.listdir('src'):
    if not i.endswith('.txt'):
        continue
    filepath = f"src/{i}"
    ba = basename(filepath)
    b, ext = splitext(ba)
    os.rename(filepath, f"src/{b}.md")
