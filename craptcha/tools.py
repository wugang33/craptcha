"""
Generic image manipulation tools.
"""
import functools
import Image
import ImageOps


deborder = functools.partial(ImageOps.crop, border=1)


def getColors(image):
    return set(color for (count, color) in image.getcolors())


def filterColors(image, colors, newColor=(255, 255, 255)):
    """
    Turns a bunch of colors into a new color.
    """
    new = Image.new("RGB", image.size)
    newData = [p if p not in colors else newColor for p in image.getdata()]
    new.putdata(newData)
    return new


def simplify(image, colors=4):
    result = image.convert("P", palette=Image.ADAPTIVE, colors=colors)
    return result.convert("RGB")