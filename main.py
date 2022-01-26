import frida
import sys
import Utils as ut

def init():
    ut.colorama.init()

    # logo printing
    ut.cprint(ut.LOGO, 'yellow')

    # select devices
    #device = ut.printListPrompt('DEVICES', 'Select device :', ut.getDevice())

    # auto select device
    device = ut.getDevice()

    # select target APP
    targetName = ut.printListPrompt('APP', 'Select target APP :', )

def main():
    
    

    targetName = ut.printListPrompt

    try:
        # search iPhone device
        device = ut.getDevice()

        # spawn and attach target APP
        targetPid = device.spawn(ut.targetName)
        session = device.attach(targetPid)

        # hook script load
        script = session.create_script(ut.jail_script)
        script.load()

        # target APP resume
        device.resume(targetPid)

        sys.stdin.read()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    init()
    main()