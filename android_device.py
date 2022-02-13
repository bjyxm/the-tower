import subprocess as sp
from ppadb.client import Client as AdbClient
from PIL import Image
import io

sp.run(['adb', 'kill-server'], stdout=sp.PIPE)
sp.run(['adb', 'devices'], stdout=sp.PIPE)


class AndroidDevice:
    def __init__(self, device_id):
        adb = AdbClient()
        self.device = adb.device(device_id)

    def capture(self):
        screen = self.device.screencap()
        im_bytes = io.BytesIO(screen)
        im = Image.open(im_bytes)
        return im

    def tap_xy(self, x, y):
        self.device.input_tap(x, y)

    def tap_point(self, point):
        self.device.input_tap(point[0], point[1])

    def swipe_xy(self, x1, y1, x2, y2, duration):
        self.device.input_swipe(x1, y1, x2, y2, duration)

    def swipe_point(self, p1, p2, duration):
        self.device.input_swipe(p1[0], p1[1], p2[0], p2[1], duration)

    def back(self):
        self.device.input_keyevent(4)

    def get_top_activity_package(self):
        return self.device.get_top_activity().package
