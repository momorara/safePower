
#!/usr/bin/python

"""
###########################################################################
# sw1 により電源を投入し、sw2によりシャットダウンの後、電源を切る。

#Filename      :safePower.py

2021/11/19  作成
2021/11/23  safePower基板がないと GPIOが常に0なので、swが押されたと判断して
            起動後速攻でシャットダウンしてしまう。
            1→0を検知して動作するようにする。
2023/10/07  POW_off_SWをソフトプルアップとした
2025/01/03  gpiozero使用に改造
############################################################################
"""
from gpiozero import Button, LED
import time
import subprocess
import configparser
import datetime
import getpass

# ユーザー名を取得
dt_now = datetime.datetime.now()
print(dt_now)
user_name = getpass.getuser()
print('user_name', user_name)
path = f'/home/{user_name}/safePower/'  # cronで起動する際には絶対パスが必要
print(path)

# config.iniから値取得
# --------------------------------------------------
config_ini = configparser.ConfigParser()
config_ini.read(path + 'config.ini', encoding='utf-8')
# --------------------------------------------------
Ry_off_pin = int(config_ini.get('DEFAULT', 'Ry_off'))
POW_off_SW_pin = int(config_ini.get('DEFAULT', 'POW_off_SW'))

# GPIOピン設定
relay = LED(Ry_off_pin)  # リレーをLEDとして制御
power_button = Button(POW_off_SW_pin, pull_up=True)

# イベントコールバック関数
def power_off():
    print(f"GPIO[{POW_off_SW_pin}] の off が発生しました")
    print('POW_off_SW が押されました。')

    print('約30秒後に電源を切るカウントを始めます。')
    relay.on()  # リレーをONにする

    print('シャットダウンします。')
    subprocess.run('sudo shutdown now', shell=True)

    time.sleep(30)  # 30秒待機  これは無くても既にシャットダウンシーケンス実行中


# ボタン押下時のイベント設定
power_button.when_released = power_off

# メインループ
def main():
    try:
        print("安全な電源管理スクリプトが実行中です。終了するにはCtrl+Cを押してください。")
        while True:
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("プログラムを終了します。")

# スクリプトを直接実行する場合
if __name__ == '__main__':
    main()
