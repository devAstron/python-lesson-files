# def toliq_ism(ism, familiya):
#     """Foydalanuvchi ism va familiyasini jamlab chiqaruvchi funksiya"""
#     print(f"Foydalanuvchi ismi: {ism.title()}\n"
#           f"Foydalanuvchi familiyasi: {familiya.title()}")
# toliq_ism('bahodir', 'siddiqov')
# def yosh_hisobla(ism, tugilgan_yil):
#     """Foydalanuvchi yoshini hisoblaydigan dastur"""
#     print(f"{ism.title()} {2023-tugilgan_yil} yoshda")
# yosh_hisobla('bahodir', 2004)
# def yosh_hisobla(tugilgan_yil, joriy_yil=2023): # joriy yil uchun st.qiymat 2020
#     """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
# yosh_hisobla(2004,2023)
# def yosh_hisobla(ism, joriy_yil=2023):
#     """Foydalanuvchi yoshidan uning tug`ilgan yilini hisoblaydi"""
#     print(f" {name.title()} siz {joriy_yil-tyil} yilda tug`ilgansiz")
# name = input('Ismingiz nima?  ') 
# tyil = int(input("Yoshingiz nechida "))
# yosh_hisobla(tyil)
# def aniqlovchi(son):
#     """Foydalanuvchidan son olib uni toq yoki juftligini konsolega chiqaradi"""
#     if son%2 == 0:
#         print(f"Siz kiritgan {son} soni juft ekan")
#     else: 
#         print(f"Siz kiritgan {son} soni toq ekan")
# son = int(input('Ixtiyoriy son kiriting: '))
# aniqlovchi(son)
# def chiqaruvchi(son1, son2):
#     if son1 > son2:
#         print(f" {son1} soni {son2} ga qaraganda kattaroq shekilli")
#     elif son1 == son2:
#         print(f"{son1} soni {son2} ga tenga o`xshaydi")
#     else:
#         print(f" {son2} soni {son1} dan kattaroq ekan")
# son1 = int(input('1-sonni kiriting '))
# son2 = int(input('2-sonni kiriting '))
# chiqaruvchi(son1, son2)

# def chiqaruvchi(x , y = 2):
#     print(f"{x} \n{y}")
# x = (input("x ni kirit "))

# chiqaruvchi(x)
def kaktus(son):
    numbers = list(range(2,11))
    for number in numbers:
        if son % number == 0:
            print(f"{son} soni {number} ga qoldiqisiz bo`linadi")
        else: 
            print(f"{son} ni {number} ga bo`lganda", son % number, "qoldiq qoladi")
son = int(input("Son kiriting: "))
kaktus(son)










