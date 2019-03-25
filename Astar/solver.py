import sys
from PIL import Image
from astar import *

# Author: Miguel Sancho

img = Image.open(sys.argv[1])
image_pixels = img.load()
im_arr = list(img.getdata(0))
width = img.size[0]
height = img.size[1]

# Start row
for x in range(1, width - 1):
    if im_arr[x] > 0:
        startp = x
        break

# End row
offset = (height - 1) * width
for x in range(1, width - 1):
    if im_arr[offset + x] > 0:
        endp = x
        break

# end row
start = (startp, 0)
goal = (endp, height - 1)

astar = astar(width, height, image_pixels)
path = astar.calculatePath(start, goal)

if not path:
   print("path not found")
else:
    print("Path found!")
    print("Length:{}".format(len(path)))
    img = img.convert('RGB')
    path_pixels = img.load()

    for position in path:
        x,y = position
        path_pixels[x,y] = (0,0,255)

    img.save(sys.argv[2])