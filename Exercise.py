
from PIL import ImageChops 
from pyscreenshot import grab 

im = grab()
while True:
    diff = ImageChops.difference(grab(), im)
    bbox = diff.getbbox()
    if bbox is not None: 
        break

print("bounding box of non-zero difference: %s" % (bbox,))



ImageChops.screen(ImageChops.invert(im.crop(bbox)), diff.crop(bbox)).show()
input("Press Enter to exit")  