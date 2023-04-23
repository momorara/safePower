
#!/usr/bin/python

"""
###########################################################################
# sw1 により電源を投入し、sw2　によりシャットダウンの後、電源を切る。

#Filename      :safePower.py

2021/11/19  作成
2021/11/23  safePower基板がないと GPIOが常に0なので、とてふが押されたと判断して
            起動後速攻でシャットダウンしてしまう。
            1→0を検知して動作するようにする。

scp -r LongLife/safePower pi@192.168.68.107:/home/pi/safePower
############################################################################
"""

import RPi.GPIO as GPIO
import time
import subprocess
import configparser

import datetime
import getpass

# ユーザー名を取得
dt_now = datetime.datetime.now()
print(dt_now)
user_name = getpass.getuser()
print('user_name',user_name)
path = '/home/' + user_name + '/safePower/' # cronで起動する際には絶対パスが必要
print(path)

# config,iniから値取得
# --------------------------------------------------
# configparserの宣言とiniファイルの読み込み
config_ini = configparser.ConfigParser()
config_ini.read(path + 'config.ini', encoding='utf-8')
# --------------------------------------------------
# config,iniから値取得
Ry_off = int(config_ini.get('DEFAULT', 'Ry_off'))
POW_off_SW = int(config_ini.get('DEFAULT', 'POW_off_SW'))

def event_callback(POW_off_SW):
    if (GPIO.input(POW_off_SW)):
        print ("GPIO[ %d ] の on が発生しました" % POW_off_SW)
        print('on')
    else:
        print ("GPIO[ %d ] の off が発生しました" % POW_off_SW)

        print('POW_off_SW が押されました。')
        GPIO.output(Ry_off,GPIO.HIGH)
        print('約30秒後に電源を切るカウントを始めます。')
        time.sleep(2)
        print('シャットダウンします。')
        subprocess.run('sudo shutdown now',shell=True)

#main function
def main():
    GPIO.setwarnings(False)
    #set the gpio modes to BCM numbering
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(POW_off_SW,GPIO.IN)
    GPIO.setup(Ry_off,GPIO.OUT,initial=GPIO.LOW)

    # 立ち下がり検出
    GPIO.add_event_detect(POW_off_SW, GPIO.FALLING, callback=event_callback, bouncetime=1000)

    while True:
        time.sleep(0.5)
    

#define a destroy function for clean up everything after the script finished
def destroy():
    #release resource
    GPIO.cleanup()
#
# if run this script directly ,do:
if __name__ == '__main__':
    try:
        main()
    #when 'Ctrl+C' is pressed,child program destroy() will be executed.
    except KeyboardInterrupt:
        destroy()

   
