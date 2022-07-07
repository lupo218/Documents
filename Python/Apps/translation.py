from googletrans import Translator
translator = Translator()
#respund =(translator.translate('אני רוצה לבדוק ',dest = 'en'))
#print(respund.text)

with open('f:\\Temp\\test.txt' , mode='r') as my_file:
    for i in my_file.readlines():
        #print(i)
        respund = (translator.translate(i, dest='he'))
        print(respund.text)