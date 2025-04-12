import cv2
import mss
import numpy as np


class Window:
    def __init__(self, window_name, width=640, height=480):
        self.window_name = window_name
        self.width = width
        self.height = height
        # 創建窗口
        cv2.namedWindow(self.window_name, cv2.WINDOW_NORMAL)
        cv2.resizeWindow(self.window_name, self.width, self.height)

    def show(self, image):
        cv2.imshow(self.window_name, image)

    def close(self):
        cv2.destroyWindow(self.window_name)

    def wait_for_key(self):
        return cv2.waitKey(1)

    @staticmethod
    def create_monitor(left, top, width, height):
        return locals()

    @staticmethod
    def capture_screen(mss_obj, monitor: dict):
        return cv2.cvtColor(np.array(mss_obj.grab(monitor)), cv2.COLOR_BGRA2BGR)

if __name__ == "__main__":
    def test(width, height):
        import time

        _ESC_ASCII_CODE = 27
        _FPS = 240
        _mss = mss.mss()
        _window = Window("Test", width, height)
        monitor = Window.create_monitor(*(0, 0, width, height))

        # press ESC to exit
        while True:
            img = Window.capture_screen(_mss, monitor)
            _window.show(img)
            if _window.wait_for_key() & 0xFF == _ESC_ASCII_CODE:
                _window.close()
                break
            time.sleep(1 / _FPS)
    test(1920, 1080)
