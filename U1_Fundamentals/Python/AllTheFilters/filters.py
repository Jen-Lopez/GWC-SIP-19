# from the Pillow Library import this Image class
from PIL import Image

# returns the image object with the opened file
def load_img(file_name):
    im = Image.open(file_name)
    return im

# displays the image object using image preview
def show_img(img):
    img.show(title = None, command = None)

# saves a new image with the given file name in the same directory
def save_img(img_obj,new_name):
    img_obj.save(new_name,format = None)

# creates obamicon filter
def obamicon(img):
    pix = img.getdata() # gets all the pixels in the picture
    new_values = list() # holds "replacement"/filter pixels

    darkBlue = (0,51,76)
    red = (217,26,33)
    lightBlue = (112,150,158)
    yellow = (252,227,166)

    for p in pix:
        intensity = p[0] + p[1]+p[2]

        # darkBlue/Low(<182)
        if (182 < intensity < 364):
            new_values.append(darkBlue)
        # red/Medium-Low( >= 182 and <364
        elif (182 <= intensity < 364):
            new_values.append(red)
        # lightBlue/Medium-High(>= 364 and < 546)
        elif (364 <= intensity < 546):
            new_values.append(lightBlue)
        # yellow/ High (>= 546)
        else:
            new_values.append(yellow)
    # return a new image with the filter applied
    new_image = Image.new("RGB",img.size) # make new image object
    new_image.putdata(new_values) # replace rgb values for new image
    return new_image

# gray-scale filter
# set each pixel's rgb values to the average of the rgb values
def gray (img):
    pixels = img.getdata()
    new_pix = list()

    for p in pixels:
        avg = int((p[0] + p[1] + p[2])/3)
        new_rgb = (avg,avg,avg)
        new_pix.append(new_rgb)

    new_image = Image.new("RGB",img.size)
    new_image.putdata (new_pix)
    return new_image

# Invert-colors filter
# flip pixel values. Subtract current RGB value from maximum value (255)

def invert(img):
    pixels = img.getdata()
    new_pix = list()

    for p in pixels:
        red = 255 - p[0]
        green = 255 - p[1]
        blue  = 255 - p[2]

        new_rgb = (red, green, blue)
        new_pix.append(new_rgb)

    new_image = Image.new("RGB",img.size)
    new_image.putdata (new_pix)
    return new_image

# Color Tint - yellowish tint filter
def tint(img):
    pixels = img.getdata()
    new_pix = list()
    color = (10,-100,20)

    for p in pixels:
        red = p[0] + color[0]
        green = p[1] + color[1]
        blue = p[2] + color[2]

        new_rgb = (red,blue,green)
        new_pix.append(new_rgb)

    new_image = Image.new("RGB",img.size)
    new_image.putdata (new_pix)
    return new_image
