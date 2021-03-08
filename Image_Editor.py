from PIL import Image, ImageOps
from PIL.ImageFilter import (EMBOSS, GaussianBlur, FIND_EDGES)
from Shift15.Restart_Function import confirm_restart


class ImageEditorClass:
    def __init__(self, inputted_img_param):
        self.inputted_img_param = inputted_img_param
        self.main_img = Image.open(inputted_img_param, mode="r")
        self.imgWidth, self.imgHeight = self.main_img.size
        self.load_imgpixels = self.main_img.load()

    def pixels_check(self, previousimg_param):
        open_previousimg = Image.open(previousimg_param, mode="r")
        previousimgwidth, previousimgheight = open_previousimg.size
        while True:
            if previousimgwidth == self.imgWidth and previousimgheight == self.imgHeight:
                pass
            else:
                return False

            for x in range(self.imgWidth):
                for y in range(self.imgHeight):
                    currentImg_pixelcheck = self.main_img.getpixel((x, y))
                    previousimgcheck = open_previousimg.getpixel((x, y))
                    if currentImg_pixelcheck == previousimgcheck:
                        continue
                    else:
                        return False
            return True

    def grayscale(self):
        self.main_img = ImageOps.grayscale(self.main_img)
        return self.main_img

    def sepia(self):
        for i in range(self.imgWidth):
            for t in range(self.imgHeight):
                single_pixel_rgb = self.main_img.getpixel((i, t))
                red = single_pixel_rgb[0]
                green = single_pixel_rgb[1]
                blue = single_pixel_rgb[2]
                sepiaR = int(0.393 * red + 0.769 * green + 0.189 * blue)
                sepiaG = int(0.349 * red + 0.686 * green + 0.168 * blue)
                sepiaB = int(0.272 * red + 0.534 * green + 0.131 * blue)
                if sepiaR > 255:
                    sepiaR = 255
                if sepiaG > 255:
                    sepiaG = 255
                if sepiaB > 255:
                    sepiaB = 255
                self.load_imgpixels[i, t] = (sepiaR, sepiaG, sepiaB)
        return self.main_img

    def invert(self):
        return ImageOps.invert(self.main_img)

    def emboss(self):
        return self.main_img.filter(EMBOSS)

    def blur(self):
        return self.main_img.filter(GaussianBlur)

    def warm(self):
        while True:
            value_given = int(input("Please enter a number from 1 to 20 for the adjustment level: "))
            if value_given not in range(1, 21):
                print("Enter a number from 1 to 20.")
            else:
                for i in range(self.imgWidth):
                    for t in range(self.imgHeight):
                        single_pixel_rgb = self.main_img.getpixel((i, t))
                        red = single_pixel_rgb[0]
                        green = single_pixel_rgb[1]
                        blue = single_pixel_rgb[2]
                        warmred = red + value_given
                        if warmred > 255:
                            warmred = 255
                        warmblue = blue - value_given
                        if warmblue < 0:
                            warmblue = 0
                        self.load_imgpixels[i, t] = (warmred, green, warmblue)
                return self.main_img

    def cold(self):
        while True:
            value_given = int(input("Please enter a number from 1 to 20 for the adjustment level: "))
            if value_given not in range(1, 21):
                print("Enter a number from 1 to 20.")
            else:
                for i in range(self.imgWidth):
                    for t in range(self.imgHeight):
                        single_pixel_rgb = self.main_img.getpixel((i, t))
                        red = single_pixel_rgb[0]
                        green = single_pixel_rgb[1]
                        blue = single_pixel_rgb[2]
                        coldred = red - value_given
                        if coldred < 0:
                            coldred = 0
                        coldblue = blue + value_given
                        if coldblue > 255:
                            coldblue = 255
                        self.load_imgpixels[i, t] = (coldred, green, coldblue)
                return self.main_img

    def transparent(self):
        self.main_img.putalpha(128)
        return self.main_img

    def pixelate(self):
        main_img_pixelated = self.main_img.resize((32, 32), resample=Image.BILINEAR)
        main_img_pixelated_fit = main_img_pixelated.resize(self.main_img.size, Image.NEAREST)
        return main_img_pixelated_fit

    def find_edges(self):
        return self.main_img.filter(FIND_EDGES)


def process_func(mainimg):
    edit_process = ImageEditorClass(mainimg)
    img_edit_dict = {"grayscale": edit_process.grayscale, "sepia": edit_process.sepia, "invert": edit_process.invert,
                     "emboss": edit_process.emboss, "blur": edit_process.blur, "warm": edit_process.warm,
                     "cold": edit_process.cold, "transparent": edit_process.transparent,
                     "pixelate": edit_process.pixelate, "find_edges": edit_process.find_edges}

    while True:
        user_choice = input("Please enter an image edit option:")
        if user_choice.strip().lower() not in img_edit_dict:
            print("Invalid input. Please try again.")
        else:
            img_edit_dict.get(user_choice.strip().lower())().show()
            break

    while True:
        ask_to_save = input("Would you like to save the image?: ")
        if ask_to_save.strip().lower() == "yes":
            new_file_name = input("Enter a name for the file (with .png): ")
            return img_edit_dict.get(user_choice.strip().lower())().save(new_file_name)
        elif ask_to_save.strip().lower() == "no":
            return "You decided to not save the image."
        else:
            print("Please type yes or no.")


same_img = False
user_img = ""
previous_img = ""
count = 1

while True:
    while True:
        if same_img is False:
            user_img = input("Please type the full path of your image's file location: ")
            if count >= 2:
                try:
                    check_img_same = ImageEditorClass(user_img)
                    if check_img_same.pixels_check(previous_img) is True:
                        print("Same image but ok...")
                except FileNotFoundError or AttributeError:
                    pass
        try:
            process_func(user_img)
            break
        except FileNotFoundError or AttributeError:
            print("Your file was not found. Please enter the absolute/full path of the image file.")

    if confirm_restart() == "yes":
        while True:
            user_confirm_sameimg = input("Would you like to use the same image? ")

            if user_confirm_sameimg.lower().strip() in "yes":
                same_img = True
                break
            elif user_confirm_sameimg.lower().strip() in "no":
                same_img = False
                previous_img = user_img
                count += 1
                break
            else:
                print("Type yes or no.")
                continue
    else:
        break
