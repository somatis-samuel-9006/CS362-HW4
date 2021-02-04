def cube_volume(length, width, height):
    try:
        vol = (length * width * height)
        return vol
    except TypeError:
        return "TypeError, non numbers were entered"


