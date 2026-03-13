"""
Takes stand-a-lone Roblox/custom classic faces and imports it into Blender (oversimplification).
Faces must be 128x128 to work.

The program takes the face of the diff image accompanying the rig's OBJ file, which is from 895x127 to 1022x0 to modify its color to the desired skin tone. Then, the desired face will be added on. Finally, the diff must be located to its intended place, i.e. next to its Wavefront file and renamed accordingly.
"""

import sys

# import tkinter as tk
from PIL import Image

# root = tk.Tk()
# root.mainloop()

BOTTOM_LEFT_CORNER_OF_DIFF_FACE = (895, 127)
TOP_RIGHT_CORNER_OF_DIFF_FACE = (1022, 0)

FACE_INSERTION_PIXEL = (895, 0)

SKIN_COLOR = (234, 184, 146)

face_diff = input("FACE_DIFF PATH: ")
# face_diff = r"Longstraighthair1_diff.png"

# classic_face_path = r"ZOMG.png"
classic_face_path = input("CLASSIC FACE: ")

try:
    face = Image.open(face_diff)
except Exception:
    print("INVALID FACE_DIFF FILE PATH")
    sys.exit(1)

try:
    classic_face = Image.open(classic_face_path)
except Exception:
    print("INVALID CLASSIC FACE PATH")
    sys.exit(1)

face_diff_pixels = face.load()

face_pixels = []

for x in range(895, 1022 + 1):
    for y in range(0, 127 + 1):
        face_pixels.append((x, 127 - y))

for pixel in face_pixels:
    face.putpixel(pixel, SKIN_COLOR)

facediff_copy = face.copy()
facediff_copy.paste(classic_face, FACE_INSERTION_PIXEL, classic_face)

new_diff_name = input("NEW DIFF NAME: ")

if not isinstance(new_diff_name, str):
    print("INVALID NEW DIFF NAME.")
    sys.exit(1)

facediff_copy.save(new_diff_name, format="PNG")
facediff_copy.show()
