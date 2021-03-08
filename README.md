# ImageFilter - Image_Editor.py is the main file.

Restart_Function.py is a custom module that has commented instructions in the file and you just have to put both files somewhere and run the main file.

The main file program asks the user for the absolute/full path of the image file. The program asks for the image editing method and then shows the result. The user is asked if he or she wants to save the file; if they choose yes, then the file is saved under a name that is given to the program afterwards and if no, then the program doesn't save and prints out a message seen in the program. 

The program asks if the user wants to continue the program (if they want to loop it or not) and if they do, then the program continues and they are asked if they want to use the same image. If not, then it doesn't ask for a new image and proceeds as usual. However, if the user is asked for the same image and they say "yes" and add the same image, then the program tells the user they already used that image but still continues as usual with the program. Back to the first sentence, if the user types no for continuing the program, the program will just stop. 

Furthermore, both ".py" files in this repository have while loops that allow them to loop back if the user gives a bad input to give the user another chance to repeat themselves for the correct input.

The current dictionary of functions: {"grayscale": edit_process.grayscale, "sepia": edit_process.sepia, "invert": edit_process.invert,
                     "emboss": edit_process.emboss, "blur": edit_process.blur, "warm": edit_process.warm,
                     "cold": edit_process.cold, "transparent": edit_process.transparent,
                     "pixelate": edit_process.pixelate, "find_edges": edit_process.find_edges}
      
1. Grayscale just turns the image into a grayed version.
2. Sepia turns the image into a sepia version.
3. Invert creates a contrasted image by inverting the RGB values.
4. Emboss creates a sort of snowy image; you can search it up as "Emboss pil" to find out more.
5. Blur makes the image blurry.
6. Warm asks the user for another input to adjust the warmth of the image by a certain integer (increases red and decreases blue).
7. Cold does the same thing but makes the image adjusts the cold values (increases blue and decreases red).
8. Transparent makes the image somewhat transparent.
9. Pixelate creates a 32 x 32 version of the image to pixelate it.
10. Find_edges turns it into an image that is akin to white color pencil on a black sheet of paper; you can search it up as "find edges pil" to find out more.
