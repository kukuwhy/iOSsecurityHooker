import frida
import sys
import Utils as ut


def main():
    try:
        print("hello?")
        targetDevice = ut.getDevice()
        targetPid = targetDevice.spawn(ut.targetName)
        session = targetDevice.attach(targetPid)
        script = session.create_script(ut.jail_script)
        script.load()
        targetDevice.resume(targetPid)
        sys.stdin.read()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()