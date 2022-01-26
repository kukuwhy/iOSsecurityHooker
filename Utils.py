import re
import frida
from PyInquirer import prompt, style_from_dict, Token

LOGO = """


"""

style = style_from_dict({
    Token.Separator: '#cc5454',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#cc5454',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#f44336 bold',
    Token.Question: '',
})

targetName = "com.highaltitudehacks.DVIAswiftv2"
jail_script = open('./script/jaildetect.js', 'r').read()
anti_script = open('./script/antiDebugging.js', 'r').read()
ssl_script = open('./script/sslPinning.js', 'r').read()

def getDevice():
    return frida.get_usb_device(1)
