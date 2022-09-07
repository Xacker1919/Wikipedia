 #Bu kod @Vaxsh1y_Xacker tomonidan yozildi. Telegram kanalimiz: @Bu_shunchaki_foydali
import wikipedia
while True:
 til = input(' Oʻzinggiz uchun mos tilni tanlang\nMasalan: Uz , Ru , En ')
 
 wikipedia.set_lang(til)

 print('Wikipedia qidiruviga xush kelibsiz\nQidiruv uchun biron-bir soʻz kiriting:\n\n')
 a = input('>>>')
 print('\n')
 
 print(wikipedia.summary(a))