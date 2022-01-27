from email.mime import application
import frida
import string
import random
import socket
from PyInquirer import prompt, style_from_dict, Token, Separator
import colorama
from termcolor import *
import platform
import re

LOGO = """


"""

targetName = "com.highaltitudehacks.DVIAswiftv2"

# open hook script
jail_script = open('./script/jailBreak.js', 'r').read()
anti_script = open('./script/antiDebugging.js', 'r').read()
ssl_script = open('./script/sslPinning.js', 'r').read()


style = style_from_dict({
    Token.Separator: '#cc5454',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#cc5454',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#f44336 bold',
    Token.Question: '',
})

def printInputPrompt(name, message):
    questions = [
        {
            'type': 'input',
            'name': name,
            'message': message,
        }
    ]
    pmt = prompt(questions, style=style, qmark='[?]')[name]
    return pmt

def printListPrompt(name, message, list):
    questions = [
        {
            'type': 'list',
            'name': name,
            'message': message,
            'choices' : list
        }
    ]
    pmt = prompt(questions, style=style, qmark='[?]')[name]
    return pmt
def getOptionList():
    questions = [
        {
            'type': 'checkbox',
            'message' : 'Select Option',
            'name' : 'options',
            'choices' : [
                Separator('== Bypass =='),
                {
                    'name': 'JailBreak Bypass'
                },
                {
                    'name': 'Anti Debug Bypass'
                },
                {
                    'name': 'SSL pinning Bypass'
                }
            ],
        }
    ]
    return prompt(questions, style=style, qmark='[?]')

def getDevice():
    return frida.get_usb_device(1)

def getPackageName():
    device = getDevice()
    apps = device.enumerate_applications()
    appList = []
    packageList = []
    for app in apps :
        appList.append(app.name)
        packageList.append(app.identifier)

    targetName = printListPrompt('package', 'Choose the paacad :', appList)
    index = appList.index(targetName)
    return packageList[index]





# if __name__ == "__main__":
