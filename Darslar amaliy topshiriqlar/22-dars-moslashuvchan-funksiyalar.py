# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 22:24:00 2023

@author: Bahodir
"""

# def kh(*nums):
#     rst = 1
#     for num in nums:
#         rst *= num
#     return rst
# print(kh(1,4,5,3,5,0))
# Talabalar haqidagi ma'lumotlarini lug'at
#  ko'rinishida qaytaruvchi funkisya yozing. Talabaning 
#  ismi va familiyasi majburiy argument, qolgan ma'lumotlar esa 
#  ixtiyoriy ko'rinishda istalgancha berilishi mumkin bo'lsin.
def std(name, surname, **other_data):
    other_data['name'] = name
    other_data['surname'] = surname
    return other_data
print(std('Sherali', 'Usmonov', kurs = 1, facility = 'TMI'))
    