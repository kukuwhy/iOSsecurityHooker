import re
import frida

LOGO = """


"""

targetName = "com.highaltitudehacks.DVIAswiftv2"
jail_script = open('./script/jaildetect.js', 'r').read()

def getDevice():
    return frida.get_usb_device(1)
