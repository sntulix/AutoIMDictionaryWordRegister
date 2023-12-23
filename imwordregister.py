"""
Auto IM Dictionary Word Register
checked: Mac Sonoma 14.2
License: GNU General Public License v3.0 
"""

import pyautogui
import pyperclip
import time


def hotkey(hold, key):
    with pyautogui.hold([hold]):
        time.sleep(1)
        pyautogui.press(key)

def pastewrite(word):
    pyperclip.copy(word)
    hotkey('command', 'v')


def open_system_preferences():
    hotkey('command', 'space')
    time.sleep(1)
    pyperclip.copy('ユーザ辞書')
    hotkey('command', 'v')
    pyautogui.keyDown('enter')

def open_user_dictionary():
    pyautogui.press('tab')

def add_word(word, reading):
    pyautogui.press('space')
    pastewrite(reading)
    pyautogui.press('tab')
    pastewrite(word)
    pyautogui.press('enter')


# メインプロセス
open_system_preferences()
time.sleep(2)  # システム環境設定が開くのを待つ

open_user_dictionary()
time.sleep(1)

add_word('漢字', 'かんじ')
add_word('英語', 'えいご')
