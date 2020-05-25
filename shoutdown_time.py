""" Testing Windows shutdown events """

import win32con
import win32api
import win32gui
import sys
import time
import datetime
now = datetime.datetime.now()

# запись в файл времени
def log_info(msg):
    print (msg)
    f = open("h:\\test.log", "a")
    f.write(msg + "\n")
    f.close()

# процедура отлова завершения работы 
def wndproc(hwnd, msg, wparam, lparam):
    log_info("Working hours : %s" % (datetime.datetime.now() - now))

# основная функция 
if __name__ == "__main__":
    timee = 0
    log_info("*** STARTING {}***".format(now))
    # Возвращает дескриптор уже загруженной библиотеки DLL.
    hinst = win32api.GetModuleHandle(None)
    # Обычно вы создаете объект PyWNDCLASS и устанавливаете его свойства. 
    # Затем объект может быть передан любой функции, которая принимает объект WNDCLASS
    wndclass = win32gui.WNDCLASS()
    # Дескриптор копии приложения
    wndclass.hInstance = hinst
    wndclass.lpszClassName = "testWindowClass"
    messageMap = { 
    win32con.WM_ENDSESSION : wndproc,
                   win32con.WM_QUIT : wndproc,
                   win32con.WM_DESTROY : wndproc,
                   win32con.WM_CLOSE : wndproc
                    }
    # Функции окна 
    wndclass.lpfnWndProc = messageMap
    try:
        # Регистрация класса в windows 
        myWindowClass = win32gui.RegisterClass(wndclass)
        # Создание окна с расширенным стилем
        hwnd = win32gui.CreateWindowEx(win32con.WS_EX_LEFT,
                                     myWindowClass, 
                                     "testMsgWindow", 
                                     0, 
                                     0, 
                                     0, 
                                     win32con.CW_USEDEFAULT, 
                                     win32con.CW_USEDEFAULT, 
                                     0, 
                                     0, 
                                     hinst, 
                                     None)
    except (Exception):
        log_info("Exception: %s" % str(Exception))   

    # Постоянная проверка на предмет завершения работы каждую секунду 
    while True:
        win32gui.PumpWaitingMessages()
        time.sleep(1)