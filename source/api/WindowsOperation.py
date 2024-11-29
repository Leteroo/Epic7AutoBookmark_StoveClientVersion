import time
import math
import win32api
import win32con


class Common:
    show_cmd = {
        "normal": win32con.SW_SHOWNORMAL,
        "minimum": win32con.SW_SHOWMINIMIZED,
        "maximum": win32con.SW_SHOWMAXIMIZED,
        "restore": win32con.SW_RESTORE
    }

    ''' 置頂功能，不知道要不要用，先註解掉 '''
    # @classmethod
    # def __set_style(cls, hwnd, new_style, IFTOPMOST):
    #     # 設置視窗新的擴展樣式
    #     win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, new_style)
    #     # 使視窗立即生效
    #     win32gui.SetWindowPos(hwnd, IFTOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
    #
    # @classmethod
    # def topmost(cls, hwnd):
    #     # 獲取當前視窗的擴展樣式
    #     ex_style = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
    #     # 將 WS_EX_TOPMOST 標誌加到當前擴展樣式中
    #     new_ex_style = ex_style | win32con.WS_EX_TOPMOST
    #     cls.__set_style(hwnd, new_ex_style, win32con.HWND_TOPMOST)
    #
    # @classmethod
    # def dis_topmost(cls, hwnd):
    #     # 獲取當前視窗的擴展樣式
    #     ex_style = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
    #     # 將 WS_EX_TOPMOST 標誌加到當前擴展樣式中
    #     new_ex_style = ex_style & ~win32con.WS_EX_TOPMOST
    #     cls.__set_style(hwnd, new_ex_style, win32con.HWND_NOTOPMOST)
    #
    # @staticmethod
    # def check_topmost(hwnd):
    #     fore = win32gui.GetForegroundWindow()
    #     return hwnd == fore

    # *_size = (left, top, right, bottom)

    @staticmethod
    def drag(start, end, duration=1.0, steps=100):
        """
        :param start: 起始座標 (x1, y1)
        :param end: 終點座標 (x2, y2)
        :param duration: 移動持續時間（秒）
        :param steps: 分成多少步完成移動
        """
        x1, y1 = start
        x2, y2 = end

        win32api.SetCursorPos((x1, y1))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x1, y1, 0, 0)
        time.sleep(0.5)
        # 計算每步的時間間隔和位移
        interval = duration / steps
        dx = (x2 - x1) / steps
        dy = (y2 - y1) / steps

        for i in range(steps):
            # 計算每一步的座標
            x = int(x1 + dx * i)
            y = int(y1 + dy * i)

            # 設置游標位置
            win32api.SetCursorPos((x, y))

            # 等待一小段時間
            time.sleep(interval)

        # 確保游標最後精確到終點
        win32api.SetCursorPos((x2, y2))
        time.sleep(0.5)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x2, y2, 0, 0)
        time.sleep(0.5)

    @staticmethod
    def doubleClick(x, y):
        x = int(x)
        y = int(y)
        win32api.SetCursorPos((x, y))
        time.sleep(0.5)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        time.sleep(0.02)  # 按下延遲
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        time.sleep(0.02)  # 按下延遲
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

    @staticmethod
    def get_correct_origin_of_inner_window(outer_size: tuple, inner_size: tuple):
        title_height = win32api.GetSystemMetrics(5)
        frame_height = win32api.GetSystemMetrics(9)
        frame_width = math.ceil((outer_size[2] - outer_size[0] - inner_size[2]) / 2)
        # calc origin
        left = outer_size[0] + frame_width
        top = outer_size[1] + frame_height * 2 - title_height * 2
        tmp = (left, top, 0, 0)
        return tuple(map(lambda x, y: x + y, tmp, inner_size))


