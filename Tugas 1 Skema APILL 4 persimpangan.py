#setup trafic light in 4 intersection

#Library
from gpiozero import LED  #library untuk GPIO yang akan dimasukki LED
from time import sleep    #library untuk pengaturan waktu mati dan menyala

#setup the LED
red = LED(22)     #simpangan 1 dimasukkan kedalam P22
yellow = LED(27)  #simpangan 1 dimasukkan kedalam P27
green = LED (17)  #simpangan 1 dimasukkan kedalam P17
red1 = LED(21)    #simpangan 2 dimasukkan kedalam P21
yellow1 = LED(20) #simpangan 2 dimasukkan kedalam P20
green1 = LED(16)  #simpangan 2 dimasukkan kedalam P16
red2 = LED(26)    #simpangan 3 dimasukkan kedalam P26
yellow2 = LED(19) #simpangan 3 dimasukkan kedalam P19
green2 = LED (13) #simpangan 3 dimasukkan kedalam P13
red3 = LED(6)     #simpangan 4 dimasukkan kedalam P6
yellow3 = LED(5)  #simpangan 4 dimasukkan kedalam P5
green3 = LED (11) #simpangan 4 dimasukkan kedalam P11

#looping
while True:
    
    green.on()    #lampu hijau persimpangan 1 menyala
    green1.off()  #lampu hijau persimpangan 2 mati
    green2.off()  #lampu hijau persimpangan 3 mati
    green3.off()  #lampu hijau persimpangan 4 mati
    yellow.off()  #lampu kuning persimpangan 1 mati
    yellow1.off() #lampu kuning persimpangan 2 mati
    yellow2.off() #lampu kuning persimpangan 3 mati
    yellow3.off() #lampu kuning persimpangan 4 mati
    red.off()     #lampu merah persimpangan 1 mati
    red1.on()     #lampu merah persimpangan 2 menyala
    red2.on()     #lampu merah persimpangan 3 menyala
    red3.on()     #lampu merah persimpangan 4 menyala
    sleep(3)      #menyala selama 3 detik untuk setiap perpindahannya
    
    green.off()   #lampu hijau persimpangan 1 mati
    green1.off()  #lampu hijau persimpangan 2 mati
    green2.off()  #lampu hijau persimpangan 3 mati
    green3.off()  #lampu hijau persimpangan 4 mati
    yellow.on()   #lampu kuning persimpangan 1 menyala
    yellow1.off() #lampu kuning persimpangan 2 mati
    yellow2.off() #lampu kuning persimpangan 3 mati
    yellow3.off() #lampu kuning persimpangan 4 mati
    red.off()     #lampu merah persimpangan 1 mati
    red1.on()     #lampu merah persimpangan 2 menyala
    red2.on()     #lampu merah persimpangan 3 menyala
    red3.on()     #lampu merah persimpangan 4 menyala
    sleep(3)      #menyala selama 3 detik untuk setiap perpindahannya
    
    green.off()   #lampu hijau persimpangan 1 mati
    green1.off()  #lampu hijau persimpangan 2 mati
    green2.off()  #lampu hijau persimpangan 3 mati
    green3.off()  #lampu hijau persimpangan 4 mati
    yellow.off()  #lampu kuning persimpangan 1 mati
    yellow1.on()  #lampu kuning persimpangan 2 menyala
    yellow2.off() #lampu kuning persimpangan 3 mati
    yellow3.off() #lampu kuning persimpangan 4 mati
    red.on()      #lampu merah persimpangan 1 menyala
    red1.on()     #lampu merah persimpangan 2 menyala
    red2.on()     #lampu merah persimpangan 3 menyala
    red3.on()     #lampu merah persimpangan 4 menyala
    sleep(3)      #menyala selama 3 detik untuk setiap perpindahannya
    
    green.off()   #lampu hijau persimpangan 1 mati
    green1.on()   #lampu hijau persimpangan 2 menyala
    green2.off()  #lampu hijau persimpangan 3 mati
    green3.off()  #lampu hijau persimpangan 4 mati
    yellow.off()  #lampu kuning persimpangan 1 mati
    yellow1.off() #lampu kuning persimpangan 2 mati
    yellow2.off() #lampu kuning persimpangan 3 mati
    yellow3.off() #lampu kuning persimpangan 4 mati
    red.on()      #lampu merah persimpangan 1 menyala
    red1.off()    #lampu merah persimpangan 2 mati
    red2.on()     #lampu merah persimpangan 3 menyala
    red3.on()     #lampu merah persimpangan 4 menyala
    sleep(3)      #menyala selama 3 detik untuk setiap perpindahannya
    
    green.off()   #lampu hijau persimpangan 1 mati
    green1.off()  #lampu hijau persimpangan 2 mati
    green2.off()  #lampu hijau persimpangan 3 mati
    green3.off()  #lampu hijau persimpangan 4 mati
    yellow.off()  #lampu kuning persimpangan 1 mati
    yellow1.on()  #lampu kuning persimpangan 2 menyala
    yellow2.off() #lampu kuning persimpangan 3 mati
    yellow3.off() #lampu kuning persimpangan 4 mati
    red.on()      #lampu merah persimpangan 1 menyala
    red1.off()    #lampu merah persimpangan 2 mati
    red2.on()     #lampu merah persimpangan 3 menyala
    red3.on()     #lampu merah persimpangan 4 menyala
    sleep(3)      #menyala selama 3 detik untuk setiap perpindahannya
    
    green.off()   #lampu hijau persimpangan 1 mati
    green1.off()  #lampu hijau persimpangan 2 mati
    green2.off()  #lampu hijau persimpangan 3 mati
    green3.off()  #lampu hijau persimpangan 4 mati
    yellow.off()  #lampu kuning persimpangan 1 mati
    yellow1.off() #lampu kuning persimpangan 2 mati
    yellow2.on()  #lampu kuning persimpangan 3 mati
    yellow3.off() #lampu kuning persimpangan 4 mati
    red.on()      #lampu merah persimpangan 1 menyala
    red1.on()     #lampu merah persimpangan 2 menyala
    red2.on()     #lampu merah persimpangan 3 menyala
    red3.on()     #lampu merah persimpangan 4 menyala
    sleep(3)      #menyala selama 3 detik untuk setiap perpindahannya
    
    green.off()   #lampu hijau persimpangan 1 mati
    green1.off()  #lampu hijau persimpangan 2 mati
    green2.on()   #lampu hijau persimpangan 3 menyala
    green3.off()  #lampu hijau persimpangan 4 mati
    yellow.off()  #lampu kuning persimpangan 1 mati
    yellow1.off() #lampu kuning persimpangan 2 mati
    yellow2.off() #lampu kuning persimpangan 3 mati
    yellow3.off() #lampu kuning persimpangan 4 mati
    red.on()      #lampu merah persimpangan 1 menyala
    red1.on()     #lampu merah persimpangan 2 menyala
    red2.off()    #lampu merah persimpangan 3 mati
    red3.on()     #lampu merah persimpangan 4 menyala
    sleep(3)      #menyala selama 3 detik untuk setiap perpindahannya
    
    green.off()   #lampu hijau persimpangan 1 mati
    green1.off()  #lampu hijau persimpangan 2 mati
    green2.off()  #lampu hijau persimpangan 3 mati
    green3.off()  #lampu hijau persimpangan 4 mati
    yellow.off()  #lampu kuning persimpangan 1 mati
    yellow1.off() #lampu kuning persimpangan 2 mati
    yellow2.on()  #lampu kuning persimpangan 3 menyala
    yellow3.off() #lampu kuning persimpangan 4 mati
    red.on()      #lampu merah persimpangan 1 menyala
    red1.on()     #lampu merah persimpangan 2 menyala
    red2.off()    #lampu merah persimpangan 3 mati
    red3.on()     #lampu merah persimpangan 4 menyala
    sleep(3)      #menyala selama 3 detik untuk setiap perpindahannya
    
    green.off()   #lampu hijau persimpangan 1 mati
    green1.off()  #lampu hijau persimpangan 2 mati
    green2.off()  #lampu hijau persimpangan 3 mati
    green3.off()  #lampu hijau persimpangan 4 mati
    yellow.off()  #lampu kuning persimpangan 1 mati
    yellow1.off() #lampu kuning persimpangan 2 mati
    yellow2.off() #lampu kuning persimpangan 3 mati
    yellow3.on()  #lampu kuning persimpangan 4 menyala
    red.on()      #lampu merah persimpangan 1 menyala
    red1.on()     #lampu merah persimpangan 2 menyala
    red2.off()    #lampu merah persimpangan 3 mati
    red3.on()     #lampu merah persimpangan 4 menyala
    sleep(3)      #menyala selama 3 detik untuk setiap perpindahannya
    
    green.off()   #lampu hijau persimpangan 1 mati
    green1.off()  #lampu hijau persimpangan 2 mati
    green2.off()  #lampu hijau persimpangan 3 mati
    green3.on()   #lampu hijau persimpangan 4 menyala
    yellow.off()  #lampu kuning persimpangan 1 mati
    yellow1.off() #lampu kuning persimpangan 2 mati
    yellow2.off() #lampu kuning persimpangan 3 mati
    yellow3.off() #lampu kuning persimpangan 4 mati
    red.on()      #lampu merah persimpangan 1 menyala
    red1.on()     #lampu merah persimpangan 2 menyala
    red2.on()     #lampu merah persimpangan 3 menyala
    red3.off()    #lampu merah persimpangan 4 mati
    sleep(3)      #menyala selama 3 detik untuk setiap perpindahannya
    
    green.off()   #lampu hijau persimpangan 1 mati
    green1.off()  #lampu hijau persimpangan 2 mati
    green2.off()  #lampu hijau persimpangan 3 mati
    green3.off()  #lampu hijau persimpangan 4 mati
    yellow.on()   #lampu kuning persimpangan 1 menyala
    yellow1.off() #lampu kuning persimpangan 2 mati
    yellow2.off() #lampu kuning persimpangan 3 mati
    yellow3.on()  #lampu kuning persimpangan 4 menyala
    red.on()      #lampu merah persimpangan 1 menyala
    red1.on()     #lampu merah persimpangan 2 menyala
    red2.on()     #lampu merah persimpangan 3 menyala
    red3.off()    #lampu merah persimpangan 1 mati
    sleep(3)      #menyala selama 3 detik untuk setiap perpindahannya