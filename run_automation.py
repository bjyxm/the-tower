from android_device import AndroidDevice
from time import sleep
from state import find_state

device = AndroidDevice('emulator-5554')
app_package = 'com.TechTreeGames.TheTower'

while True:
    cap = device.capture()
    if cap is None:
        print('Capture failed')
        sleep(3)
        continue

    package = device.get_top_activity_package()
    if package != app_package:
        print('App is not running')
        continue

    state = find_state(cap)
    if state:
        print('Current State:', state.name())
        state.do_automation(device, cap)
    else:
        print('Unknown State')
    sleep(3)
