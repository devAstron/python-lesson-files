# print('dastur kiritilgan sonnni kvadratini hisoblab beradi')
# quession = 'istalgan son kiriting biz uni kvadratini hisoblab beramiz (dasturni to`xtatish uchun "exit" deb yozing)\n>>>'
# value = ''
# while value != 'exit':
#     value = input(quession)
#     if value != 'exit':
#         print(float(value)**2)
# print('Dastur to`xtadi')
# print('dastur kiritilgan sonnni kvadratini hisoblab beradi')
# quession = 'istalgan son kiriting biz uni kvadratini hisoblab beramiz (dasturni to`xtatish uchun "exit" deb yozing)\n>>>'
# target = True
# while target:
#     value = input(quession)
#     if value == 'exit':
#         target = False
#     else: 
#         print(float(value)**2)
        
# print('Dastur tugadi')
# print('Ixitoyriy son kiriting biz sizga uni kvadratini hisoblab beramiz, dasturni to`xtatish uchun "exit" deb yozing')
# Value = ' '
# while Value !='exit':
#         Value = input('>>> ')
#         if Value != 'exit':
#             print(f"{int(Value)**2}")
# print('Dastur to`xtadi')
# print('Ixitoyriy son kiriting biz sizga uni kvadratini hisoblab beramiz, dasturni to`xtatish uchun "exit" deb yozing')
# value = ''
# while True:
#     value = input('>>>')
#     if value == 'exit':
#         break
#     else:
#         print(f"{int(value)**2}")
# print('Dastur tugadi')       
# son = 1 # son ga 1 qiymatini beramiz
# while son<=5: # toki son 5 dan kichik yoki teng ekan...
#     print(son, end=' ') # son ni konsolga chiqaramiz,
#     son = son+1 # songa 1 qo'shamiz.
# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5: # son 5 ga teng bo'lsa tiskl boshiga qaytadi
#         break
#     print(f"{son} ning kvadrati {son**2} ga teng")
#Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang. Foydalanuvchi stop so'zini yozishi bilan dasturni to'xtating
# print('Qayso kitoblarni yaxshi ko`rasi ? ')
# kitob =  ''
# while kitob != 'exit':
#     if kitob!= 'exit':
#         kitob = input('>>>')
 
# print('dastur toxtadi, malumotlar saqlandi')
# Muzeyga chipta narhi foydalanuvchining yoshiga 
# bog'liq: 7 dan yoshlarga - 2000 so'm, 7-18 gacha 3000 so'm, 
# 18-65 gacha 10000 so'm, 65 dan kattalarga bepul. Shunday while
#  tsikl yozingki, dastur foydalanuvchi yoshini so'rasin va chipta 
#  narhini chiqarsin. Foydalanuvchi exit yoki quit deb yozganda dastur 
#  to'xtasin (ikkita shartni ham tekshiring).
# print('Assalomu alaykum, yoshingiz nechida ( dasturni to`xtatish uchun exit yoki quit deb yozing ) ')
# yosh = ' '
# while True:
#     yosh = input()
#     if yosh== 'exit' or yosh=='quit':
#         break
#     if int(yosh) < 7:
#         print("Kirish narxi- 2000 so`m")
#     elif int(yosh) >= 7 and int(yosh) < 18:
#         print('Kirish narxi - 3000 so`m')
#     elif int(yosh) >= 18 and int(yosh) < 65:
#         print('Kirish narxi - 10000 so`m')
#     elif int(yosh) > 65:
#         print('Kirish tekin')
# print('Dastur to`xtadi')
savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if int(qiymat)<0:
        break
    elif qiymat=='Exit':
        break
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")            
print(f" {qiymat} ning ildizi yo`q!")













