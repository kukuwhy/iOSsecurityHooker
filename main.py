import frida
import sys
import Utils as ut

targetName = ut.getPackageName()
def init():
    ut.colorama.init()

    # logo printing
    ut.cprint(ut.LOGO, 'yellow')

    # select devices
    #device = ut.printListPrompt('DEVICES', 'Select device :', ut.getDevice())

    # select target APP
    

def main():
    try:
        # search iPhone device
        device = ut.getDevice()

        # spawn and attach target APP
        targetPid = device.spawn(targetName)
        session = device.attach(targetPid)

        opt = ut.getOptionList()
        for option in opt['options']:
            if option == "JailBreak Bypass" :
                script = session.create_script(ut.jail_script)
                script.load()
            elif option == "Anti Debug Bypass" :
                script = session.create_script(ut.anti_script)
                script.load()
            elif option == "SSL pinning Bypass" :
                script = session.create_script(ut.ssl_script)
                script.load()

        # target APP resume
        device.resume(targetPid)

        sys.stdin.read()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    init()
    main()