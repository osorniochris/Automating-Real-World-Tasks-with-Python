from PIL import ImageGrab
import keyboard

name = ""
route = ""

while True:
    try:
        if keyboard.is_pressed('p'):
           image = ImageGrab.grab()
           name = input("Image name: ")

           if name.find("COMP_") != -1:
              route = "Compiladores\\"
           elif name.find("CRYP_") != -1:
              route = "Cryptography\\"
           elif name.find("DIST_") != -1:
              route = "Distribuidos\\"
           elif name.find("IS_") != -1:
              route = "IngenieriaSoftware\\"
           elif name.find("MICRO_") != -1:
              route = "Microcontroladores\\"

           image.save(route + name + ".png")
           print(name + " saved!")
           pass
        else:
            pass
    except:
        break