import pyautogui
import time


while(1):
    secs = time.time()
    tm = time.localtime(secs)
    setting_th = tm.tm_hour
    setting_tm = tm.tm_min + 2
    setting_ts = tm.tm_sec

    setting_time = "{}:{}:{}".format(setting_th,setting_tm,setting_ts)

    pyautogui.moveTo(223,313) #(x좌표, y좌표, 시간)
    pyautogui.click(clicks=1) 
    time.sleep(1)

    pyautogui.typewrite(setting_time)
    pyautogui.press('enter')

    time.sleep(125) #안에 현재 입력한 시간으로부터 알람이 울리기까지의 시간만큼이 들어가야함..현재 시간 +2니까 실행시간 생각해서 125초 설정. 

    pyautogui.moveTo(269,322)
    pyautogui.click(clicks=1) 
    time.sleep(3)

    if():   #언제까지 메트로 돌릴건지 안에 조건 달아주기. 
        break
