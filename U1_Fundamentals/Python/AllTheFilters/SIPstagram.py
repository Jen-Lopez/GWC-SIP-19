import filters

def intro ():
    intro = """
    To make a filtered image, enter a valid file name
    or path to open and modify.
    """
    print(intro)

# validates the path put in by user
def validPath():
    while True:
        fileName = input ("Enter a file name: ")
        try:
            pic = filters.load_img(fileName)
            print ("Success!\n")
            return pic
        except FileNotFoundError:
            print ("Unable to open the file. Try Again.\n")

# asks and validates user response to saving new image file
def shouldSave():
    while True:
        res = input ("Do you want to save? ")
        try:
            res = res.lower()
            if res == "y":
                return True
            elif res == "n":
                return False
            else:
                print ("'y' for save, 'n' to not save\n")
        except:
            print ("Invalid Input.\n")

# asks and validates a user's file name for the new image
def newName (img):
    while True:
        try:
            new_name = input ("Enter a name for your file (include extension): ")
            filters.save_img(img, new_name)
            break
        except:
            print ("Invalid name. Remember to add an extension (e.g. .jpg, .png, etc)\n")

# asks user what filter they want to apply to image object
def ask (picture):
    print ("What filter do you want to apply?")
    while True:
        res = input("\nObamicon[o], Gray[g], Inverted[i], Yellow-Tinted[y], Quit[q] ")

        try:
            res = res.lower()
        except:
            print("Wrong Input. Please try again.\n")
            continue

        if res == 'o':
            print("...generating obamicon...")
            obamicon_pic = filters.obamicon(picture)
            curr_pic = obamicon_pic
            filters.show_img(obamicon_pic)

        elif res == 'g':
            print("...generating grayscale...")
            gray_pic = filters.gray(picture)
            curr_pic = gray_pic
            filters.show_img(gray_pic)

        elif res == 'i':
            print("...generating inverted...")
            inverted = filters.invert(picture)
            curr_pic = inverted
            filters.show_img(inverted)

        elif res == 'y':
            print("...generating yellow-tinted...")
            tinted_pic = filters.tint(picture)
            curr_pic = tinted_pic
            filters.show_img(tinted_pic)

        elif res == 'q':
            print ("...quitting...\n")
            break

        else:
            print("Invalid response. Please Try Again.\n")
            continue

        print("success!\n")

        if (shouldSave()):
            newName(curr_pic)
            print ("All Saved!\n")

# MAIN FUNCTION
def main ():
    intro()
    pic_obj = validPath()
    ask(pic_obj)

#---------- MAIN PROGRAM ----------
if __name__ == "__main__":
    main ()
