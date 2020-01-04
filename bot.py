 #-*-coding:utf-8-*-

#ПО

import random
import requests
import os
import keyboard
import pyautogui
import time
from colorama import init
from colorama import Fore, Back, Style
import sys
import socket
import pyowm
init()


#BOT

exit = '0'
one = '1'
two = '2'
three = '3'
four = '4'
five = '5'
six = '6'
seven = '7'
eith = '8'
nine = '9'


#ANTISKUKA

def antiskuka():
  global exit
  while True:
    try:
      print(colorrandom() + '\n\nВыберите средство от скуки\n\n' + colorrandom() + 
            '1.(Вирус(' + Fore.RED + 'ЗАПУСКАТЬ НА СВОЙ СТРАХ И РИСК' + colorrandom() + '))\n0.(Выйти в меню бота)\n')
      a = int(input())
      if a == 1:
        if keyboard.is_pressed(exit):
          return
        while True:
          pyautogui.hotkey('win','r')
          pyautogui.write('cmd')
          pyautogui.press('enter')
          pyautogui.hotkey('win','r')
          pyautogui.write('msconfig')
          pyautogui.press('enter')
          pyautogui.hotkey('win','r')
          pyautogui.write('regedit')
          pyautogui.press('enter')
          os.system('devmgmt.msc')
          os.system('services.msc')
      elif a == 0:
        return
    except:
      print(colorrandom() + many() + '=================')
      print(Fore.RED + '| Введите цифру |')
      print(colorrandom() + '=================')


#WEATHER

def weather():
  while True:
    try:
      owm = pyowm.OWM('60a644a24f44f9b1d955105766a3cc54', language = 'ru')
      place = input('\n\nВведите город/страну: ')
      observation = owm.weather_at_place(place)
      w = observation.get_weather()
      temp = w.get_temperature('celsius')["temp"]
      print('Сейчас в городе ' + place + ': ' + w.get_detailed_status())
      print('Сейчас в городе ' + place + ' температура: ' + str(temp))
      time.sleep(8)
      return
    except:
      print(colorrandom() + many() + '==================================')
      print(Fore.RED + '| Введите корректно город/страну |')
      print(colorrandom() + '==================================')

#CHANGE_PASS_USER

def change_pass_user():
  colorrandom()
  os.system('net user ' + os.environ['USERNAME'] + ' *')
  time.sleep(3)

#MANYENTERS

def many():
  a = ('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
  return a


#GENERATORPASS

def generatorpass():
  colorrandom()
  while True:
    try:
      print(colorrandom() + 'Выберите режим генерации пароля:\n')
      k = int(input('1.(С заглавными буквами и цифрами)\n2.(С маленькими буквами и цифрами)\n3.(Только цифры)\n'
                   '4.(Только заглавные буквы)\n5.(Только маленькие буквы)\n0.(Выйти в меню бота)\n'))
      if k == 1:  
        while True:
          try:
            colorrandom()
            d = int(input('Введите число в котором количестве вы хотите сгенерировать пароль: '))
            a = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890'
            b = ''
            c = 0
            while c < d:
              b += a[random.randint(0, len(a) -1)]
              c += 1
            print(colorrandom() + '\n\nВаш пароль: ' + b + '\n\n')
            colorrandom()
            a = input('\nНажмите "W" чтобы повторить генерацию\nНажмите "Q" чтобы выйти из генератора паролей\n'
                      'Нажмите "Е" чтобы повторить генерацию на выбранном пункте\n')
            enter = 'w'
            q = 'q'
            e = 'e'
            if a == q:
              many()
              return
            elif a == enter:
              many()
              break
            elif a == e:
              colorrandom() + many()
          except:
            print(colorrandom() + many() + '=================')
            print(Fore.RED + '| Введите цифру |')
            print(colorrandom() + '=================')
      elif k == 2:
        while True:        
          try:
              colorrandom()
              d = int(input('Введите число в котором количестве вы хотите сгенерировать пароль: '))
              a = 'qwertyuiopasdfghjklzxcvbnm1234567890'
              b = ''
              c = 0
              while c < d:
                b += a[random.randint(0, len(a) -1)]
                c += 1
              print(colorrandom() + '\n\nВаш пароль: ' + b + '\n\n')
              colorrandom()
              a = input('\nНажмите "W" чтобы повторить генерацию\nНажмите "Q" чтобы выйти из генератора паролей\n'
                        'Нажмите "Е" чтобы повторить генерацию на выбранном пункте\n')
              enter = 'w'
              q = 'q'
              e = 'e'
              if a == q:
                many()
                return
              elif a == enter:
                many()
                break
              elif a == e:
                colorrandom() + many()
          except:
            print(colorrandom() + many() + '=================')
            print(Fore.RED + '| Введите цифру |')
            print(colorrandom() + '=================')
      elif k == 3:
        while True:
          try:
              colorrandom()
              d = int(input('Введите число в котором количестве вы хотите сгенерировать пароль: '))
              a = '1234567890'
              b = ''
              c = 0
              while c < d:
                b += a[random.randint(0, len(a) -1)]
                c += 1
              print(colorrandom() + '\n\nВаш пароль: ' + b + '\n\n')
              colorrandom()
              a = input('\nНажмите "W" чтобы повторить генерацию\nНажмите "Q" чтобы выйти из генератора паролей\n'
                        'Нажмите "Е" чтобы повторить генерацию на выбранном пункте\n')
              enter = 'w'
              q = 'q'
              e = 'e'
              if a == q:
                many()
                return
              elif a == enter:
                many()
                break
              elif a == e:
                colorrandom() + many()
          except:
            print(colorrandom() + many() + '=================')
            print(Fore.RED + '| Введите цифру |')
            print(colorrandom() + '=================')
      elif k == 4:
        while True:
          try:
              colorrandom()
              d = int(input('Введите число в котором количестве вы хотите сгенерировать пароль: '))
              a = 'QWERTYUIOPASDFGHJKLZXCVBNM'
              b = ''
              c = 0
              while c < d:
                b += a[random.randint(0, len(a) -1)]
                c += 1
              print(colorrandom() + '\n\nВаш пароль: ' + b + '\n\n')
              colorrandom()
              a = input('\nНажмите "W" чтобы повторить генерацию\nНажмите "Q" чтобы выйти из генератора паролей\n'
                        'Нажмите "Е" чтобы повторить генерацию на выбранном пункте\n')
              enter = 'w'
              q = 'q'
              e = 'e'
              if a == q:
                many()
                return
              elif a == enter:
                many()
                break
              elif a == e:
                colorrandom() + many()
          except:
            print(colorrandom() + many() + '=================')
            print(Fore.RED + '| Введите цифру |')
            print(colorrandom() + '=================')
      elif k == 5:
        while True:
          try:
              colorrandom()
              d = int(input('Введите число в котором количестве вы хотите сгенерировать пароль: '))
              a = 'qwertyuiopasdfghjklzxcvbnm'
              b = ''
              c = 0
              while c < d:
                b += a[random.randint(0, len(a) -1)]
                c += 1
              print(colorrandom() + '\n\nВаш пароль: ' + b + '\n\n')
              colorrandom()
              a = input('\nНажмите "W" чтобы повторить генерацию\nНажмите "Q" чтобы выйти из генератора паролей\n'
                        'Нажмите "Е" чтобы повторить генерацию на выбранном пункте\n')
              enter = 'w'
              q = 'q'
              e = 'e'
              if a == q:
                many()
                return
              elif a == enter:
                many()
                break
              elif a == e:
                colorrandom() + many()
          except:
            print(colorrandom() + many() + '=================')
            print(Fore.RED + '| Введите цифру |')
            print(colorrandom() + '=================')
      elif k == 0:
        many()
        return
    except:
      print(colorrandom() + many() + '=================')
      print(Fore.RED + '| Введите цифру |')
      print(colorrandom() + '=================')
  

#COLORRANDOM

def colorrandom():
  a = random.randint(1,6)
  if a == 1:
    return Fore.GREEN
  elif a == 2:
    return Fore.RED
  elif a == 3:
    return Fore.WHITE
  elif a == 4:
    return Fore.YELLOW
  elif a == 5:
    return Fore.CYAN
  elif a == 6:
    return Fore.MAGENTA

#RANDOMIZER

def randomizer():
  while True:
    try:
      a = random.randint(1,100)
      print(colorrandom(), many() ,'=========================')
      print(colorrandom() + ' | 1.(Случайное число)   |')
      print(colorrandom() + ' | 2.(Задать число)      |')
      print(colorrandom() + ' | 3.(Орел или решка)    |')
      print(colorrandom() + ' | 0.(Выйти в меню бота) |')
      print(colorrandom() + ' =========================') 
      b = int(input())
      if b == 1:
        print(colorrandom() + '\n\n===================\nВаше число: ', a ,' |\n===================')
        time.sleep(5)
        return
      elif b == 2:
        s = int(input('От числа: '))
        f = int(input('До числа: '))
        print(colorrandom() + '\n\n===================\nВаше число: ', random.randint(s,f)  ,' |\n===================')
        time.sleep(5)
        return
      elif b == 3:
        vars = ("Орел", "Решка")
        print(colorrandom() + vars[random.randint(0, 1)])
        time.sleep(3)
        return
      elif b == 0:
        return
    except:
      print(colorrandom() + many() + '=================')
      print(Fore.RED + '| Введите цифру |')
      print(colorrandom() + '=================')

#MAIN MENU

def main_menu():
  print(colorrandom() + '==========================================================================================================')
  print(Fore.GREEN + '| ' + os.environ['USERNAME'] + ' | 0.(Выйти в меню выбора разрешения экрана) | (ПИСАТЬ ТОЛЬКО ЦИФРЫ)')
  print(colorrandom() + '==========================================================================================================\n')
  print(colorrandom() + '|===================================================|' + colorrandom() + '|===================================================|')
  print(colorrandom() + '|1.(Выключить ПК)                                   |' + colorrandom() + '|9.(Генератор пароля) | (требуется английский язык) |')
  print(colorrandom() + '|---------------------------------------------------|' + colorrandom() + '|---------------------------------------------------|')
  print(colorrandom() + '|2.(Перезагрузить ПК)                               |' + colorrandom() + '|10.(Поменять пароль на учетной записи)             |')
  print(colorrandom() + '|---------------------------------------------------|' + colorrandom() + '|---------------------------------------------------|')
  print(colorrandom() + '|3.(Браузер)          | (требуется английский язык) |' + colorrandom() + '|11.(Узнать погоду)                                 |')
  print(colorrandom() + '|---------------------------------------------------|' + colorrandom() + '|---------------------------------------------------|')
  print(colorrandom() + '|4.(Система)          | (требуется английский язык) |' + colorrandom() + '|12.(АнтиСкука)       | (требуется английский язык) |')
  print(colorrandom() + '|---------------------------------------------------|' + colorrandom() + '|---------------------------------------------------|')
  print(colorrandom() + '|5.(Автокликер)       | (требуется английский язык) |' + colorrandom() + '|13.(Недоступно)                                    |')
  print(colorrandom() + '|---------------------------------------------------|' + colorrandom() + '|---------------------------------------------------|')
  print(colorrandom() + '|6.(Починка ПК)       | (требуется английский язык) |' + colorrandom() + '|14.(Недоступно)                                    |')
  print(colorrandom() + '|---------------------------------------------------|' + colorrandom() + '|---------------------------------------------------|')
  print(colorrandom() + '|7.(Узнать свой IP адрес)                           |' + colorrandom() + '|15.(Недоступно)                                    |')
  print(colorrandom() + '|---------------------------------------------------|' + colorrandom() + '|---------------------------------------------------|')
  print(colorrandom() + '|8.(Рандомайзер)                                    |' + colorrandom() + '|16.(Недоступно)                                    |')
  print(colorrandom() + '|===================================================|' + colorrandom() + '|===================================================|')

#IP

def ip():
  while True:
    try:
      a = int(input('Узнать внешний или локальный IP-Адрес?\n1.(Внешний)\n2.(Локальный)\n0.(Выйти в меню бота)\n'))
      if a == 1:
        print(colorrandom() + 'Пока что не работает :(')
        time.sleep(6)
        return
      elif a == 2:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("gmail.com",80))
        print(s.getsockname()[0])
        s.close()
        time.sleep(6)
        return
      elif a == 0:
        return
    except:
      print(colorrandom() + many() + '=================')
      print(Fore.RED + '| Введите цифру |')
      print(colorrandom() + '=================')


#BROWSER

def VK_YOUTUBE_YANDEX():
  yandex() #BROWSER
  time.sleep(15)
  pyautogui.hotkey('win','up')
  pyautogui.press('F6') #SEARCH
  pyautogui.write('https://youtube.com')
  pyautogui.press('enter')
  pyautogui.hotkey('ctrl','t') #+
  time.sleep(3)
  pyautogui.press('F6')
  pyautogui.write('https://vk.com')   
  pyautogui.press('enter')

def VK_Y():
  yandex() #BROWSER
  time.sleep(15)
  pyautogui.hotkey('win','up')
  pyautogui.press('F6')
  pyautogui.write('https://vk.com') 
  pyautogui.press('enter')

def Y_Y():
  yandex() #BROWSER
  time.sleep(15)
  pyautogui.hotkey('win','up')
  pyautogui.press('F6') #SEARCH
  pyautogui.write('https://youtube.com')
  pyautogui.press('enter')

def TranslatorY():
  yandex()
  time.sleep(15)
  pyautogui.hotkey('win','up')
  pyautogui.press('F6')
  time.sleep(1)
  pyautogui.write('https://translate.yandex.ru/')
  time.sleep(1)
  pyautogui.press('enter')

def VK_YOUTUBE_GOOGLE():
  google() #BROWSER
  time.sleep(15)
  pyautogui.hotkey('win','up')
  pyautogui.press('F6') #SEARCH
  pyautogui.write('https://youtube.com')
  pyautogui.press('enter')
  pyautogui.hotkey('ctrl','t') #+
  time.sleep(3)
  pyautogui.press('F6')
  pyautogui.write('https://vk.com')   
  pyautogui.press('enter') 

def VK_G():
  google() #BROWSER
  time.sleep(15)
  pyautogui.hotkey('win','up')
  pyautogui.press('F6')
  pyautogui.write('https://vk.com')   
  pyautogui.press('enter')

def Y_G():
  google() #BROWSER
  time.sleep(15)
  pyautogui.hotkey('win','up')
  pyautogui.press('F6') #SEARCH
  pyautogui.write('https://youtube.com')
  pyautogui.press('enter')

def TranslatorG():
  google()
  time.sleep(15)
  pyautogui.hotkey('win','up')
  pyautogui.press('F6')
  time.sleep(1)
  pyautogui.write('https://translate.yandex.ru/')
  time.sleep(1)
  pyautogui.press('enter')

def WinR():
  time.sleep(1)
  pyautogui.hotkey('win','r')
  time.sleep(1)

def vk_ALL():
  WinR()
  time.sleep(1)
  pyautogui.write('https://vk.com')
  pyautogui.press('enter')

def youtube_ALL():
  WinR()
  time.sleep(1)
  pyautogui.write('https://youtube.com')
  pyautogui.press('enter')

def vk_youtube_ALL():
  WinR()
  time.sleep(1)
  pyautogui.write('https://youtube.com')
  pyautogui.press('enter')
  WinR()
  time.sleep(1)
  pyautogui.write('https://vk.com')
  pyautogui.press('enter')

def translator_ALL():
  WinR()
  time.sleep(1)
  pyautogui.write('https://translate.yandex.ru')
  pyautogui.press('enter')

#USING

def browser():
  while True:
    try:
      print(colorrandom(), many() ,'=========================\n'
                            ' | Выберите браузер:     |')
      print(colorrandom() + ' | 1.(Yandex)            |')
      print(colorrandom() + ' | 2.(Google Chrome)     |')
      print(colorrandom() + ' | 3.(Прочее)            |')
      print(colorrandom() + ' | 0.(Выйти в меню бота) |')
      print(colorrandom() + ' =========================')
      BROWSER = int(input())
      if BROWSER == 1: #YANDEX
        while True:
          try:
            init()
            print(colorrandom(), many() ,'            ==========')
            print(colorrandom() + '             | YANDEX |')
            print(colorrandom() + '             ==========')
            print(colorrandom() + '|1.(Вконтакте + Youtube)                          |')
            print(colorrandom() + '|2.(Вконтакте)                                    |')
            print(colorrandom() + '|3.(Youtube)                                      |')
            print(colorrandom() + '|4.(Переводчик)                                   |')
            print(colorrandom() + '|0.(Выйти в главное меню бота)                    |')
            come = int(input())
            if come == 1:
              VK_YOUTUBE_YANDEX()
              print(many()) 
              return
            elif come == 2:
              VK_Y()
              print(many())
              return
            elif come == 3:
              Y_Y()
              print(many())    
              return     
            elif come == 4:
              TranslatorY()
              print(many())
              return
            elif come == 0:
              return
              print(many())
          except:
            print(colorrandom() + many() + '=================')
            print(Fore.RED + '| Введите цифру |')
            print(colorrandom() + '=================')
      elif BROWSER == 2: # GOOGLE
        while True:
          try:
            init()
            print(colorrandom(), many() ,'            ==========')
            print(colorrandom() + '             | GOOGLE |')
            print(colorrandom() + '             ==========')
            print(colorrandom() + '|1.(Вконтакте + Youtube)                          |')
            print(colorrandom() + '|2.(Вконтакте)                                    |')
            print(colorrandom() + '|3.(Youtube)                                      |')
            print(colorrandom() + '|4.(Переводчик)                                   |')
            print(colorrandom() + '|0.(Выйти в главное меню бота)                    |')
            come = int(input())
            if come == 1:
              VK_YOUTUBE_GOOGLE()
              print(many())
              return
            elif come == 2:
              VK_G()
              print(many())
              return
            elif come == 3:
              Y_G()
              print(many())
              return
            elif come == 4:
              TranslatorG()
              print(many())
              return
            elif come == 0:
              return
              print(many())
          except:
            print(colorrandom() + many() + '=================')
            print(Fore.RED + '| Введите цифру |')
            print(colorrandom() + '=================')
      elif BROWSER == 3: #allBrowser
        while True:
          try:
            init()
            print(colorrandom(), many() ,'            ==========')
            print(colorrandom() + '             | Прочее |')
            print(colorrandom() + '             ==========')
            print(colorrandom() + '|1.(Вконтакте + Youtube)                          |')
            print(colorrandom() + '|2.(Вконтакте)                                    |')
            print(colorrandom() + '|3.(Youtube)                                      |')
            print(colorrandom() + '|4.(Переводчик)                                   |')
            print(colorrandom() + '|0.(Выйти в главное меню бота)                    |')
            come = int(input())
            if come == 1:
              vk_youtube_ALL()
              print(many())
              return
            elif come == 2:
              vk_ALL()
              print(many())
              return
            elif come == 3:
              youtube_ALL()
              print(many())
              return
            elif come == 4:
              translator_ALL()
              print(many())
              return
            elif come == 0:
              return
              print(many())
          except:
            print(colorrandom() + many() + '=================')
            print(Fore.RED + '| Введите цифру |')
            print(colorrandom() + '=================')
      elif BROWSER == 0:
        return
    except:
      print(colorrandom() + many() + '=================')
      print(Fore.RED + '| Введите цифру |')
      print(colorrandom() + '=================')

#REBOOT

def reboot():
  while True:
    try:
      init()
      many()
      print(colorrandom() + '|1.(Перезагрузить ПК)                              |')
      print(colorrandom() + '|2.(Перезагрузить ПК через 30 минут) (1800 секунд) |')
      print(colorrandom() + '|3.(Перезагрузить ПК через 1 час)    (3600 секунд) |')
      print(colorrandom() + '|4.(Перезагрузить ПК через 1.5 часа) (5400 секунд) |')
      print(colorrandom() + '|5.(Перезагрузить ПК через 2 часа)   (7200 секунд) |')
      print(colorrandom() + '|6.(Задать время  в секундах)                      |')
      print(colorrandom() + '|0.(Выйти в главное меню бота)                     |')
      SASA = int(input())
      if SASA == 1:
        os.system('shutdown /r /t 0')
      elif SASA == 2:
        time.sleep(1800)  
        os.system('shutdown /r /t 0')
      elif SASA == 3:
        time.sleep(3600)
        os.system('shutdown /r /t 0')
      elif SASA == 4:
        time.sleep(5400)
        os.system('shutdown /r /t 0')
      elif SASA == 5:
        time.sleep(7200)
        os.system('shutdown /r /t 0')
      elif SASA == 6:
        asdzx = int(input(colorrandom() + '\n\n\nВведите число (в секундах): '))
        time.sleep(asdzx)
        os.system('shutdown /r /t 0')
      elif SASA == 0:
        return
        many()
    except:
      print(colorrandom() + many() + '=================')
      print(Fore.RED + '| Введите цифру |')
      print(colorrandom() + '=================')

#SHUTDOWN

def shutdown():
  while True:
    try:
      init()
      many()
      print(colorrandom() + '|1.(Выключить ПК)                                  |')
      print(colorrandom() + '|2.(Выключить ПК через 30 минут)  (1800 секунд)    |')
      print(colorrandom() + '|3.(Выключить ПК через 1 час)     (3600 секунд)    |')
      print(colorrandom() + '|4.(Выключить ПК через 1,5 часа)  (5400 секунд)    |')
      print(colorrandom() + '|5.(Выключить ПК через 2 часа)    (7200 секунд)    |')
      print(colorrandom() + '|6.(Задать время  в секундах)                      |')
      print(colorrandom() + '|0.(Выйти в главное меню бота)                     |')
      BASD = int(input())
      if BASD == 1:
        os.system('shutdown /s /t 0')
      elif BASD == 2:
        time.sleep(1800)
        os.system('shutdown /s /t 0')
      elif BASD == 3:
        time.sleep(3600)
        os.system('shutdown /s /t 0')
      elif BASD == 4:
        time.sleep(5400)
        os.system('shutdown /s /t 0')
      elif BASD == 5:
        time.sleep(7200)
        os.system('shutdown /s /t 0')
      elif BASD == 6:
        asdzxc = int(input(colorrandom() + '\n\n\nВведите число (в секундах): '))
        time.sleep(asdzxc)
        os.system('shutdown /s /t 0')
      elif BASD == 0:
        return
        many()
    except:
      print(colorrandom() + many() + '=================')
      print(Fore.RED + '| Введите цифру |')
      print(colorrandom() + '=================')

#AutoClicker

def AutoClicker():
  global exit
  while True:
    try:
      print(colorrandom(), many() ,'Выбери режим кликов\n' + colorrandom() + '1.(1 клик за раз)\n'
            + colorrandom() + '2.(2 клика за раз)\n' + colorrandom() + '3.(3 клика за раз)\n' + colorrandom() + '0.(Выйти в главное меню бота)\n')
      nbv = int(input())
      if nbv == 1:
        print(colorrandom() + 'чтобы выйти в главное меню автокликера нажмите на клавишу "0"\n')
        print(colorrandom() + 'Нажмите и удерживайте клавишу "F4", чтобы автокликер начал работать\nОпустите, чтобы перестал кликать')
        key = 'F4'
        while 'F4':
            if keyboard.is_pressed(key):
              pyautogui.click()
            elif keyboard.is_pressed(exit):
              return
      elif nbv == 2:
        print(colorrandom() + 'чтобы выйти в главное меню автокликера нажмите на клавишу "0"\n')
        print(colorrandom() + 'Нажмите и удерживайте клавишу "F4", чтобы автокликер начал работать\nОпустите, чтобы перестал кликать')
        keys = 'F4'
        while  'F4':
            if keyboard.is_pressed(keys):
              pyautogui.doubleClick()
            elif keyboard.is_pressed(exit):
              return
      elif nbv == 3:
        print(colorrandom() + 'чтобы выйти в главное меню автокликера нажмите на клавишу "0"\n')
        print(colorrandom() + 'Нажмите и удерживайте клавишу "F4", чтобы автокликер начал работать\nОпустите, чтобы перестал кликать')
        keya = 'F4'
        while 'F4':
            if keyboard.is_pressed(keya):
              pyautogui.tripleClick()
            elif keyboard.is_pressed(exit):
              return
      elif nbv == 0:
        return
    except:
      print(colorrandom() + many() + '=================')
      print(Fore.RED + '| Введите цифру |')
      print(colorrandom() + '=================')

#SYSTEM

def cmd():
  WinR()
  time.sleep(1)
  pyautogui.write('cmd')
  pyautogui.press('enter')
def system():
  while True:
    try:
      init()
      print(colorrandom() + '\n\n\n\n|1.(Командная строка)                             |')
      print(colorrandom() + '|2.(Конфигурация системы)                         |')
      print(colorrandom() + '|3.(Реестр)                                       |')
      print(colorrandom() + '|4.(Службы)                                       |')
      print(colorrandom() + '|5.(appdata)                                      |')
      print(colorrandom() + '|6.(Диспетчер устройств)                          |')
      print(colorrandom() + '|7.(Завершить процесс приложения)                 |')
      print(colorrandom() + '|8.(Узнать характеристики компьютера)             |')
      print(colorrandom() + '|0.(Выйти в главное меню бота)                    |')
      pt = int(input())
      if pt == 1:
        cmd()
      elif pt == 2:
        WinR()
        time.sleep(1)
        pyautogui.write('msconfig')
        pyautogui.press('enter')
      elif pt == 3:
        os.system('regedit')
      elif pt == 4:
        os.system('services.msc')
      elif pt == 5:
        WinR()
        time.sleep(1)
        pyautogui.write('%appdata%')
        pyautogui.press('enter')
      elif pt == 6:
        os.system('devmgmt.msc')
      elif pt == 7:
        print(colorrandom())
        process = input(many() + '(Например: [google, sublime])\nВведите название первой части приложения: ')
        print(Fore.RED + Back.WHITE + '\n\n\n\n\n\n\n\n\n\n\n\nЕСЛИ НЕТ ВТОРОГО НАЗВАНИЯ ОСТАВИТЬ ПОЛЕ ПУСТЫМ\n')
        print(colorrandom() + Back.BLACK)
        process2 = input('(Например: [chrome, text])\nВведите название второй части приложения: ')
        print(colorrandom())
        if process + process2:                                                       # -
          os.system('Taskkill /IM ' '-' + process + process2 + '.exe /F')
        print(colorrandom())
        if process + process2:                                                       #    -
          os.system('Taskkill /IM ' + process + process2 + '-' '.exe /F')
        print(colorrandom())
        if process + process2:                                                       #  -
          os.system('Taskkill /IM ' + process + '-' + process2 + '.exe /F')
        print(colorrandom())
        if process + process2:                                                       # - -
          os.system('Taskkill /IM ' '-' + process + '-' + process2 + '.exe /F')
        print(colorrandom())
        if process + process2:                                                       # -  -
          os.system('Taskkill /IM ' '-' + process + process2 + '-' '.exe /F')
        print(colorrandom())
        if process + process2:                                                       # - - -
          os.system('Taskkill /IM ' '-' + process + '-' + process2 + '-' '.exe /F')
        print(colorrandom())
        if process + process2:                                                       #  _
          os.system('Taskkill /IM ' + process + '_' + process2 + '.exe /F')
        print(colorrandom())
        if process + process2:                                                       # SPACE
          os.system('Taskkill /IM ' + process + '' + process2 + '.exe /F')
        print(colorrandom())
        if process + process2:                                                       # JOIN
          os.system('Taskkill /IM ' + process + process2 + '.exe /F')
        print(colorrandom())
        if process + process2:                                                       # _
          os.system('Taskkill /IM ' '_' + process + process2 + '.exe /F')
        print(colorrandom())
        if process + process2:                                                       #    _
          os.system('Taskkill /IM ' + process + process2 + '_' '.exe /F')
        print(colorrandom())
        if process + process2:                                                       # _ _
          os.system('Taskkill /IM ' '_' + process + '_' + process2 + '.exe /F')
        print(colorrandom())
        if process + process2:                                                       # _  _
          os.system('Taskkill /IM ' '_' + process + process2 + '_' '.exe /F')
        print(colorrandom())
        if process + process2:                                                       # _ _ _
          os.system('Taskkill /IM ' '_' + process + '_' + process2 + '_' '.exe /F')
        print(colorrandom())
        if process + process2:                                                       # - _ _
          os.system('Taskkill /IM ' '-' + process + '_' + process2 + '_' '.exe /F')
        print(colorrandom())
        if process + process2:                                                       # _ - _
          os.system('Taskkill /IM ' '_' + process + '-' + process2 + '_' '.exe /F')
        print(colorrandom())
        if process + process2:                                                       # _ _ -
          os.system('Taskkill /IM ' '_' + process + '_' + process2 + '-' '.exe /F')
        print(colorrandom())
        if process + process2:                                                       # - - _
          os.system('Taskkill /IM ' '-' + process + '-' + process2 + '_' '.exe /F')
        print(colorrandom())
        if process + process2:                                                       # _ - -
          os.system('Taskkill /IM ' '_' + process + '-' + process2 + '-' '.exe /F')
        print(colorrandom())
        if process + process2:                                                       # - _ -
          os.system('Taskkill /IM ' '-' + process + '_' + process2 + '-' '.exe /F')
        print(many())
      elif pt == 8:
        os.system('systeminfo')
      elif pt == 0:
        return
    except:
      print(colorrandom() + many() + '=================')
      print(Fore.RED + '| Введите цифру |')
      print(colorrandom() + '=================')

#FIXING PC

def fix():
  while True:
    try:
      a = int(input(colorrandom() + many() + '1.(Починить звук)\n2.(Проверка целостности и исправление системных файлов)\n'
              '3.(Оптимизация ПК)\n0.(Выйти в меню бота)\n'))
      if a == 1:
        print(colorrandom() + 'Идет перезапуск службы...')
        os.system('net stop audiosrv')
        os.system('net start audiosrv')
        while True:
          try:
            many()
            print(colorrandom() + 'Помогло?')
            s = int(input(colorrandom() + '1.(Да)\n2.(Нет)\n'))
            if s == 2:
              print(colorrandom() + 'Пробуем дальше...\n\n\n')
              time.sleep(2)
              print(colorrandom() + 'Выключаем звук...\n')
              os.system('net stop "Windows Audio"')
              print(colorrandom() + 'Включаем звук...\n')
              os.system('net start "Windows Audio"')
              while True:
                try:
                  many()
                  print(colorrandom() + 'Помогло?')
                  d = int(input(colorrandom() + '1.(Да)\n2.(Нет)\n'))
                  if d == 2:
                    print(colorrandom() + 'Идем дальше...\n\n\n')
                    time.sleep(2)
                    print(colorrandom() + 'Пытаемся поменять тип запуска звука...\n\n\n')
                    time.sleep(2)
                    os.system('sc config Audiosrv start= auto')
                    while True:
                      try:
                        many()
                        print(colorrandom() + 'Помогло?')
                        c = int(input(colorrandom() + '1.(Да)\n2.(Нет)\n'))
                        if c == 1:
                          print(colorrandom() + 'Приятно было помочь вам')
                          time.sleep(3)
                          return
                        elif c == 2:
                          print(colorrandom() + '\nПростите, я больше не знаю как вам помочь\n'
                                'В будущем в меня добавят еще способы исправления проблемы!')
                          time.sleep(7)
                          return
                      except:
                        print(colorrandom() + many() + '=================')
                        print(Fore.RED + '| Введите цифру |')
                        print(colorrandom() + '=================')
                  elif d == 1: 
                    print(colorrandom(), many() ,'Приятно было помочь вам')
                    time.sleep(3) 
                    return
                except:
                  print(colorrandom() + many() + '=================')
                  print(Fore.RED + '| Введите цифру |')
                  print(colorrandom() + '=================')
            elif s == 1:
              print(colorrandom(), many() ,'Приятно было помочь вам')
              time.sleep(3)
              return
          except:
            print(colorrandom() + many() + '=================')
            print(Fore.RED + '| Введите цифру |')
            print(colorrandom() + '=================')
      elif a == 2:
        os.system('dism /Online /Cleanup-Image /RestoreHealth')
        time.sleep(3)
        return
      elif a == 3:
        os.system('sfc /scannow')
        cmd()
        time.sleep(0.3)
        pyautogui.write('del C:\\Users\\' + os.environ['USERNAME'] + '\\AppData\\Local\\Temp')
        time.sleep(0.3)
        pyautogui.press('enter')
        pyautogui.write('y')
        pyautogui.press('enter')
        time.sleep(0.3)
        pyautogui.write('del C:\\Windows\\Temp')
        time.sleep(0.3)
        pyautogui.press('enter')
        pyautogui.write('y')
        pyautogui.press('enter')
        time.sleep(0.3)
        pyautogui.write('%windir%\\system32\\rundll32.exe advapi32.dll,ProcessIdleTasks')
        pyautogui.press('enter')
        time.sleep(0.3)
        pyautogui.write('%windir%\\SysWOW64\\rundll32.exe advapi32.dll,ProcessIdleTasks')
        pyautogui.press('enter')
        time.sleep(0.3)
        pyautogui.write('ipconfig /flushdns')
        pyautogui.press('enter')
        time.sleep(0.3)
        pyautogui.write('Cleanmgr /verylowdisk')
        pyautogui.press('enter')
        pyautogui.write('Cleanmgr /SETUP')
        pyautogui.press('enter')
        os.system('Taskkill /IM cmd.exe /F')
        x = int(input(colorrandom(), many() ,'Делать сканирование и оптимизацию дисков?' + colorrandom() + '\n1.(Да)'
             + colorrandom() + '\n2.(Нет)\n'))
        while True:
          try:
            if x == 1:
              os.system('chkdsk /O')
              cmd()
              time.sleep(0.3)
              pyautogui.write('defrag /C /U /V')
              pyautogui.press('enter')
              WinR()
              time.sleep(0.5)
              pyautogui.write('chkdsk /r /f')
              pyautogui.press('enter')
              time.sleep(9)
              pyautogui.write('y')
              pyautogui.press('enter')
              os.system('Taskkill /IM cmd.exe /F')
              i = int(input(colorrandom(), many() ,'Перезагрузить ПК для завершения оптимизации?\n1.(Да)\n2.(Нет)\n'))
              while True:
                try:
                  if i == 1:
                    print(colorrandom() + 'Перезгрузка ПК через...')
                    time.sleep(1)
                    print('5...')
                    time.sleep(1)
                    print('4...')
                    time.sleep(1)
                    print('3...')
                    time.sleep(1)
                    print('2...')
                    time.sleep(1)
                    print('1...')
                    time.sleep(1)
                    print(colorrandom() + '\n\n\n...Началась перезгрузка ПК...\n\n\n')
                    time.sleep(3)
                    os.system('shutdown /r /t 0')
                  elif i == 2:
                    print(colorrandom(), many() ,'\n\n===================================================\n'
                         + colorrandom() +'| Советуем вам для завершения оптимизации перезгрузить ПК |\n'
                          + colorrandom() + '===================================================\n')
                    time.sleep(4)
                    return
                except:
                  print(colorrandom() + many() + '=================')
                  print(Fore.RED + '| Введите цифру |')
                  print(colorrandom() + '=================')
          except:
            print(colorrandom() + many() + '=================')
            print(Fore.RED + '| Введите цифру |')
            print(colorrandom() + '=================')
      elif a == 0:
        return
    except:
      print(colorrandom() + many() + '=================')
  print(Fore.RED + '| Введите цифру |')
  print(colorrandom() + '=================')


def yandex():
  homefolder = os.path.join("C:\\Users\\" + os.environ['USERNAME'] + "\\AppData\\Local\\Yandex\\YandexBrowser\\Application\\browser.exe")
  os.startfile(homefolder)


def google():
  homefolderr = os.path.join('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe')
  os.startfile(homefolderr)


def Change_Language():
  pyautogui.hotkey('shift','alt')
  os.startfile('bot.exe')
  sys.exit()
  sys.exit()

def start():
  print(Back.BLACK)
  print(colorrandom() + '\n\n\n\n\n\n\n\n\n\n\n''                                      =================================='
                                              '\n                                      |Подождите, идет загрузка бота...|\n'
                                                '                                      ==================================')
  time.sleep(2)
  print(many())

start()

while True:
  try:
    print(Back.BLACK)
    print(Fore.RED + '                          !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n'
                     '                          !!!ВНИМАНИЕ, БОТ РАБОТАЕТ ТОЛЬКО НА АНГЛИЙСКОЙ РАСКЛАДКЕ ЯЗЫКА!!!\n'
                     '                          !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!' '\n\n')
    print(Back.BLACK)
    print(colorrandom() + '                                              (ПИСАТЬ ТОЛЬКО ЦИФРЫ)')
    print(Fore.GREEN + '\n\n\n                                     Поменять раскаладку на английский язык?\n\n\n\n\n'
      '                                     1.(Да)                          2.(Нет)\n')
    azsxcz = int(input('                                                       '))
    if azsxcz == 1:
      Change_Language()
    elif azsxcz == 2:
      break
  except:
    print(colorrandom() + many() + '=================')
    print(Fore.RED + '| Введите цифру |')
    print(colorrandom() + '=================')
print(many())
while True:
  try:
    many()
    print(colorrandom() + '                                ================================================')
    print(Fore.GREEN + '                                |                    ' + os.environ['USERNAME'] + '                      |')
    print(colorrandom() + '                                ================================================')
    print(colorrandom() + '                                |      Выбери свое разрешение экрана:          |' + colorrandom() + 
                          '\n                                |               1.(1280x720)                   |' + colorrandom() + 
                          '\n                                |               2.(1280x800)                   |' + colorrandom() + 
                          '\n                                |               3.(1280x1024)                  |' + colorrandom() + 
                          '\n                                |               4.(1360x768)                   |' + colorrandom() + 
                          '\n                                |               5.(1600x900)                   |' + colorrandom() + 
                          '\n                                |               6.(1680x1050)                  |' + colorrandom() + 
                          '\n                                |               7.(1920x1080)                  |' + colorrandom() + 
                          '\n                                |     8.(1920x1080) (масштабирование 125%)     |\n'
        + colorrandom() + '                                ================================================\n\n\n\n\n')
    menu = int(input('                                                       '))
    if menu == 3:
      while True:
        try:

#1280x1024

          print(Fore.RED + '\n                           =============================================================')
          print(Fore.GREEN + '                           | Данный бот работает только на разрешении экрана 1280х1024 |')
          print(Fore.RED + '                           =============================================================\n')
          main_menu()
          klj = int(input())
      #CHANGE_SCREEN    
          if klj == 0:
            break
      #SHUTDOWN

          if klj == 1:
            shutdown()
          
      #REBOOT

          elif klj == 2:
            reboot()
          
      #BROWSER

          elif klj == 3:
            browser()
      
      #SYSTEM

          elif klj == 4:
            system()

      #AutoClicker

          elif klj == 5:
            AutoClicker()
          
      #Fixing PC

          elif klj == 6:
            fix()
      #IP
          elif klj == 7:
            ip()
      #RANDOMIZER    
          elif klj == 8:
            randomizer()
      #RANDOMPASS
          elif klj == 9:
            generatorpass()
      #CHANGE_PASS_USER    
          elif klj == 10:
            change_pass_user()
      #WEATHER
          elif klj == 11:
            weather()
      #ANTISKUKA
          elif klj == 12:
            antiskuka()
        except:
          print(Fore.RED, many() ,'|-----Пожалуйста-----------|')
          print(Fore.GREEN + ' |----------введите---------|')
          print(Fore.WHITE + ' |----------------цифру-----|')

#1280x720

    elif menu == 1:
      while True:
        try:





          print(Fore.RED + '\n                           =============================================================')
          print(Fore.GREEN  + '                          | Данный бот работает только на разрешении экрана 1280х720 |')
          print(Fore.RED + '                           =============================================================\n')
          main_menu()
          klj = int(input())
      #CHANGE_SCREEN
          if klj == 0:
            break
      #SHUTDOWN

          if klj == 1:
            shutdown()
          
      #REBOOT

          elif klj == 2:
            reboot()
          
      #BROWSER

          elif klj == 3:
            browser()
          
      #SYSTEM

          elif klj == 4:
            system()

      #AutoClicker

          elif klj == 5:
            AutoClicker()
          
      #Fixing PC

          elif klj == 6:
            fix()
      #IP
          elif klj == 7:
            ip()
      #RANDOMIZER    
          elif klj == 8:
            randomizer()
      #RANDOMPASS
          elif klj == 9:
            generatorpass()
      #CHANGE_PASS_USER    
          elif klj == 10:
            change_pass_user()
      #WEATHER
          elif klj == 11:
            weather()
      #ANTISKUKA
          elif klj == 12:
            antiskuka()
        except:
          print(Fore.RED, many() ,'|-----Пожалуйста-----------|')
          print(Fore.GREEN + ' |----------введите---------|')
          print(Fore.WHITE + ' |----------------цифру-----|')

#1280x800

    elif menu == 2:
      while True:
        try:





          print(Fore.RED + '\n                           =============================================================')
          print(Fore.GREEN  + '                          | Данный бот работает только на разрешении экрана 1280х800 |')
          print(Fore.RED + '                           =============================================================\n')
          main_menu()     
          klj = int(input())
      #CHANGE_SCREEN
          if klj == 0:
            break
      #SHUTDOWN

          if klj == 1:
            shutdown()
          
      #REBOOT

          elif klj == 2:
            reboot()
          
      #BROWSER

          elif klj == 3:
            browser()
          
      #SYSTEM

          elif klj == 4:
            system()

      #AutoClicker

          elif klj == 5:
            AutoClicker()
          
      #Fixing PC

          elif klj == 6:
            fix()
      #IP
          elif klj == 7:
            ip()
      #RANDOMIZER    
          elif klj == 8:
            randomizer()
      #RANDOMPASS
          elif klj == 9:
            generatorpass()
      #CHANGE_PASS_USER    
          elif klj == 10:
            change_pass_user()
      #WEATHER
          elif klj == 11:
            weather()
      #ANTISKUKA
          elif klj == 12:
            antiskuka()
        except:
          print(Fore.RED, many() ,'|-----Пожалуйста-----------|')
          print(Fore.GREEN + ' |----------введите---------|')
          print(Fore.WHITE + ' |----------------цифру-----|')
#1360x768

    elif menu == 4:
      while True:
        try:





          print(Fore.RED + '\n                           =============================================================')
          print(Fore.GREEN  + '                          | Данный бот работает только на разрешении экрана 1360х768 |')
          print(Fore.RED + '                           =============================================================\n')
          main_menu()
          klj = int(input())
      #CHANGE_SCREEN
          if klj == 0:
            break
      #SHUTDOWN

          if klj == 1:
            shutdown()
          
      #REBOOT

          elif klj == 2:
            reboot()
          
      #BROWSER

          elif klj == 3:
            browser()
          
      #SYSTEM

          elif klj == 4:
            system()

      #AutoClicker

          elif klj == 5:
            AutoClicker()
          
      #Fixing PC

          elif klj == 6:
            fix()
      #IP
          elif klj == 7:
            ip()
      #RANDOMIZER    
          elif klj == 8:
            randomizer()
      #RANDOMPASS
          elif klj == 9:
            generatorpass()
      #CHANGE_PASS_USER    
          elif klj == 10:
            change_pass_user()
      #WEATHER
          elif klj == 11:
            weather()
      #ANTISKUKA
          elif klj == 12:
            antiskuka()
        except:
          print(Fore.RED, many() ,'|-----Пожалуйста-----------|')
          print(Fore.GREEN + ' |----------введите---------|')
          print(Fore.WHITE + ' |----------------цифру-----|')

#1600x900

    elif menu == 5:
      while True:
        try:





          print(Fore.RED + '\n                           =============================================================')
          print(Fore.GREEN  + '                          | Данный бот работает только на разрешении экрана 1600х900 |')
          print(Fore.RED + '                           =============================================================\n')
          main_menu()
          klj = int(input())
      #CHANGE_SCREEN
          if klj == 0:
            break
      #SHUTDOWN

          if klj == 1:
            shutdown()
          
      #REBOOT

          elif klj == 2:
            reboot()
          
      #BROWSER

          elif klj == 3:
            browser()
          
      #SYSTEM

          elif klj == 4:
            system()

      #AutoClicker

          elif klj == 5:
            AutoClicker()
          
      #Fixing PC

          elif klj == 6:
            fix()
      #IP
          elif klj == 7:
            ip()
      #RANDOMIZER    
          elif klj == 8:
            randomizer()
      #RANDOMPASS
          elif klj == 9:
            generatorpass()
      #CHANGE_PASS_USER    
          elif klj == 10:
            change_pass_user()
      #WEATHER
          elif klj == 11:
            weather()
      #ANTISKUKA
          elif klj == 12:
            antiskuka()
        except:
          print(Fore.RED, many() ,'|-----Пожалуйста-----------|')
          print(Fore.GREEN + ' |----------введите---------|')
          print(Fore.WHITE + ' |----------------цифру-----|')

#1680x1050

    elif menu == 6:
      while True:
        try:





          print(Fore.RED + '\n                           =============================================================')
          print(Fore.GREEN + '                           | Данный бот работает только на разрешении экрана 1680x1050 |')
          print(Fore.RED + '                           =============================================================\n')
          main_menu()
          klj = int(input())
      #CHANGE_SCREEN
          if klj == 0:
            break
      #SHUTDOWN

          if klj == 1:
            shutdown()
          
      #REBOOT

          elif klj == 2:
            reboot()
          
      #BROWSER

          elif klj == 3:
            browser()
          
      #SYSTEM

          elif klj == 4:
            system()

      #AutoClicker

          elif klj == 5:
            AutoClicker()
          
      #Fixing PC

          elif klj == 6:
            fix()
      #IP
          elif klj == 7:
            ip()
      #RANDOMIZER    
          elif klj == 8:
            randomizer()
      #RANDOMPASS
          elif klj == 9:
            generatorpass()
      #CHANGE_PASS_USER    
          elif klj == 10:
            change_pass_user()
      #WEATHER
          elif klj == 11:
            weather()
      #ANTISKUKA
          elif klj == 12:
            antiskuka()
        except:
          print(Fore.RED, many() ,'|-----Пожалуйста-----------|')
          print(Fore.GREEN + ' |----------введите---------|')
          print(Fore.WHITE + ' |----------------цифру-----|')

#1920x1080

    elif menu == 7:
      while True:
        try:





          print(Fore.RED + '\n                           =============================================================')
          print(Fore.GREEN + '                           | Данный бот работает только на разрешении экрана 1920x1080 |')
          print(Fore.RED + '                           =============================================================\n')
          main_menu()
          klj = int(input())
      #CHANGE_SCREEN
          if klj == 0:
            break
      #SHUTDOWN

          if klj == 1:
            shutdown()
          
      #REBOOT

          elif klj == 2:
            reboot()
          
      #BROWSER

          elif klj == 3:
            browser()
          
      #SYSTEM

          elif klj == 4:
            system()

      #AutoClicker

          elif klj == 5:
            AutoClicker()
          
      #Fixing PC

          elif klj == 6:
            fix()
      #IP
          elif klj == 7:
            ip()
      #RANDOMIZER    
          elif klj == 8:
            randomizer()
      #RANDOMPASS
          elif klj == 9:
            generatorpass()
      #CHANGE_PASS_USER    
          elif klj == 10:
            change_pass_user()
      #WEATHER
          elif klj == 11:
            weather()
      #ANTISKUKA
          elif klj == 12:
            antiskuka()
        except:
          print(Fore.RED, many() ,'|-----Пожалуйста-----------|')
          print(Fore.GREEN + ' |----------введите---------|')
          print(Fore.WHITE + ' |----------------цифру-----|')

#1920x1080 X125%

    elif menu == 8:
      while True:
        try:





          print(Fore.RED + '\n                           =============================================================')
          print(Fore.GREEN + '                           | Данный работает только на разрешении экрана 1920x1080(масштабирование 125%) |')
          print(Fore.RED + '                           =============================================================\n')
          main_menu()
          klj = int(input())
      #CHANGE_SCREEN
          if klj == 0:
            break
      #SHUTDOWN

          if klj == 1:
            shutdown()
          
      #REBOOT

          elif klj == 2:
            reboot()
          
      #BROWSER

          elif klj == 3:
            browser()
          
      #SYSTEM

          elif klj == 4:
            system()

      #AutoClicker

          elif klj == 5:
            AutoClicker()
          
      #Fixing PC

          elif klj == 6:
            fix()
      #IP
          elif klj == 7:
            ip()
      #RANDOMIZER    
          elif klj == 8:
            randomizer()
      #RANDOMPASS
          elif klj == 9:
            generatorpass()
      #CHANGE_PASS_USER    
          elif klj == 10:
            change_pass_user()
      #WEATHER
          elif klj == 11:
            weather()
      #ANTISKUKA
          elif klj == 12:
            antiskuka()
        except:
          print(Fore.RED, many() ,'|-----Пожалуйста-----------|')
          print(Fore.GREEN + ' |----------введите---------|')
          print(Fore.WHITE + ' |----------------цифру-----|')
  except:
    print(Fore.RED, many() ,'|-----Пожалуйста-----------|')
    print(Fore.GREEN + ' |----------введите---------|')
    print(Fore.WHITE + ' |----------------цифру-----|\n\n\n\n\n\n')