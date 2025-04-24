import pygame as pg

## INIT 
pg.init()

  # VARIABLE RUNNING GAME
isRun = True

  # MEMBUAT DISPLAY SURFACE OBJECT
window_panjang = 700
window_lebar = 500
window = pg.display.set_mode((window_panjang, window_lebar))

  # OBJECT GAME
     # POSISI
x = 250
y = 250

     # UKURAN
panjang = 20
lebar = 20

     # KECEPATAN GERAK 
speed = 10

while isRun :
    pg.time.delay(10)


## USER INPUT, DATABASE INPUT
    for event in pg.event.get():
        if event.type == pg.QUIT:
            isRun = False  

  # AMBIL SEMUA KEYBOARD PRESS
    keys = pg.key.get_pressed()
     
     # AMBIL KIRI
    if keys[pg.K_LEFT] and x > 0 :
        x -= speed

     # AMBIL KANAN
    if keys[pg.K_RIGHT] and x < window_panjang - panjang :
        x += speed

     # AMBIL ATAS
    if keys[pg.K_UP] and y > 0 :
        y -= speed

     # AMBIL BAWAH
    if keys[pg.K_DOWN] and y < window_lebar - lebar :
        y += speed


## UPDATE ASSET
    window.fill((255,255,255))
    pg.draw.rect(window,(255,0,0),(x,y,lebar,panjang))


## RENDER KE DISPLAY
    pg.display.update()

pg.quit()
