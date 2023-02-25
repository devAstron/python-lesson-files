# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 00:09:20 2023

@author: Bahodir
"""
'''
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] 
for car in cars:
    if car != 'gm':
        print(car.title())
    else:
        print(car.upper())
'''
'''
ism = input('Loginingizni kiriting: ')
ism.lower()

if ism == 'admin':
    print('Xush kelibsiz Admin; Foydalanuvchilar ro\'yxatini ko\'rasizmi?')
else:
    print(f'Xush kelibsiz {ism.title()}')
'''
'''
a = int(input('Ikki son kiriting: \n>>>'))
b = int(input('>>>'))
if a == b:
    print('Bu ikki son teng ekan')
'''
'''
k = int(input('Son kiriting\n>>>'))
if k<0:
    print('Son manfiy ekan')
else:
    print('Son musbat ekan')
'''
k = int(input('Son kiriting \n>>>'))
if k > 0:
    print(f'Sonning musbat uning ildizi: {k**0.5} ga teng')
else:
        print("Musbat son kiriting")
        