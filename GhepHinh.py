import pygame
import random
pygame.init()
rong, hang,cot=600,4,5
tab=40
cach =rong// hang-tab//2
dai=cach*cot
screen=pygame.display.set_mode((rong,dai))
luoi=[0]*hang*cot
img=[]
trong=4
l=[5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
random.shuffle(l)
a1=l[0]
a2=l[1]
a3=l[2]
a4=l[3]
a5=l[4]
a6=l[5]
a7=l[6]
a8=l[7]
a9=l[8]
a10=l[9]
a11=l[10]
a12=l[11]
a13=l[12]
a14=l[13]
a15=l[14]
c=0
keo=pygame.mixer.Sound("Data/GhepHinh/keo.mp3")
nen=pygame.mixer.music.load("Data/GhepHinh/nen.mp3")
win=pygame.mixer.Sound("Data/GhepHinh/win.mp3")
mau=pygame.transform.scale(pygame.image.load("Data/GhepHinh/mau.png"),(cach*3-70,cach*3-70))
bg=pygame.transform.scale(pygame.image.load("Data/GhepHinh/0.png"),(720,1280))
for i in range(16):
	img.append(pygame.transform.scale(pygame.image.load("Data/GhepHinh/"+f"{i}.png"),(cach,cach)))
font=pygame.font.SysFont('san',200)
font2=pygame.font.SysFont('san',50)
pygame.mixer.music.play(-1)
game=0
while game==0:
	screen.fill("White")
	pygame.draw.rect(screen,"Green",(400,700,80,80))
	welcome=font2.render("Welcome to Puzzle Games",True,"black")
	welcome2=font2.render("Tap screen to play",True,"black")
	screen.blit(welcome,(50,200))
	screen.blit(welcome2,(100,300))
	for event in pygame.event.get():
		if event.type==pygame.MOUSEBUTTONDOWN:
			pygame.mixer.music.stop()
			game=1
		if event.type==pygame.QUIT:
			game = -1
	pygame.display.flip()
while game==1:
	screen.blit(bg,(0,0))
	screen.blit(mau,((rong-(cach*3-70))/2,cach*5+tab))
	pygame.draw.rect(screen,"Blue",(0,cach-tab,cach*4+tab,cach*4+tab*2))
	pygame.draw.rect(screen,"green",(trong% hang*cach+tab,trong//hang*cach,cach,cach),20)
#	pygame.draw.rect(screen,"green",(0,720,720,20))
	lop=pygame.Surface((200,100),pygame.SRCALPHA)
	lop1=pygame.Surface((100,200),pygame.SRCALPHA)
	lop.fill((0,0,0,0))
	lop1.fill((0,0,0,0))
	pos=px,py=pygame.mouse.get_pos()
	imgtr=screen.blit(lop1,(trong% hang*cach+cach/4+tab,trong//hang*cach-10))
	imtr=screen.blit(lop,(trong% hang*cach-10+tab,trong//hang*cach+cach/4))
	chu=font.render("YOU WIN",True,"pink")
	chu1=font.render(str(l),True,"pink")
	b1=screen.blit(img[1],(a1% hang*cach+tab,a1//hang*cach))
	b2=screen.blit(img[2],(a2% hang*cach+tab,a2//hang*cach))
	b3=screen.blit(img[3],(a3% hang*cach+tab,a3//hang*cach))
	b4=screen.blit(img[4],(a4% hang*cach+tab,a4//hang*cach))
	b5=screen.blit(img[5],(a5% hang*cach+tab,a5//hang*cach))
	b6=screen.blit(img[6],(a6% hang*cach+tab,a6//hang*cach))
	b7=screen.blit(img[7],(a7% hang*cach+tab,a7//hang*cach))
	b8=screen.blit(img[8],(a8% hang*cach+tab,a8//hang*cach))
	b9=screen.blit(img[9],(a9% hang*cach+tab,a9//hang*cach))
	b10=screen.blit(img[10],(a10% hang*cach+tab,a10//hang*cach))
	b11=screen.blit(img[11],(a11% hang*cach+tab,a11//hang*cach))
	b12=screen.blit(img[12],(a12% hang*cach+tab,a12//hang*cach))
	b13=screen.blit(img[13],(a13% hang*cach+tab,a13//hang*cach))
	b14=screen.blit(img[14],(a14% hang*cach+tab,a14//hang*cach))
	b15=screen.blit(img[15],(a15% hang*cach+tab,a15//hang*cach))
	
	#screen.blit(chu1,(0,740))
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			game=-1
		if event.type==pygame.MOUSEBUTTONDOWN:		
			if imgtr.colliderect(b1) or imtr.colliderect(b1):
				if b1.collidepoint(pos):
					pygame.mixer.Sound.play(keo)
					c=a1
					a1=trong
					trong=c
#2
			if b2.colliderect(imgtr)or imtr.colliderect(b2):
				if b2.collidepoint(pos):
					pygame.mixer.Sound.play(keo)
					c=a2
					a2=trong
					trong=c
#3
			if b3.colliderect(imgtr)or imtr.colliderect(b3):
				if b3.collidepoint(pos):
					pygame.mixer.Sound.play(keo)
					c=a3
					a3=trong
					trong=c
#4
			if b4.colliderect(imgtr)or imtr.colliderect(b4):
				if b4.collidepoint(pos):
					pygame.mixer.Sound.play(keo)
					c=a4
					a4=trong
					trong=c
#5
			if imgtr.colliderect(b5) or imtr.colliderect(b5):
				if b5.collidepoint(pos):
					pygame.mixer.Sound.play(keo)
					c=a5
					a5=trong
					trong=c
#6
			if b6.colliderect(imgtr)or imtr.colliderect(b6):
				if b6.collidepoint(pos):
					pygame.mixer.Sound.play(keo)
					c=a6
					a6=trong
					trong=c
#7
			if b7.colliderect(imgtr)or imtr.colliderect(b7):
				if b7.collidepoint(pos):
					pygame.mixer.Sound.play(keo)
					c=a7
					a7=trong
					trong=c
#8
			if b8.colliderect(imgtr)or imtr.colliderect(b8):
				if b8.collidepoint(pos):
					pygame.mixer.Sound.play(keo)
					c=a8
					a8=trong
					trong=c
#9
			if imgtr.colliderect(b9) or imtr.colliderect(b9):
				if b9.collidepoint(pos):
					pygame.mixer.Sound.play(keo)
					c=a9
					a9=trong
					trong=c
#10
			if b10.colliderect(imgtr)or imtr.colliderect(b10):
				if b10.collidepoint(pos):
					pygame.mixer.Sound.play(keo)
					c=a10
					a10=trong
					trong=c
#11
			if b11.colliderect(imgtr)or imtr.colliderect(b11):
				if b11.collidepoint(pos):
					pygame.mixer.Sound.play(keo)
					c=a11
					a11=trong
					trong=c
#12
			if b12.colliderect(imgtr)or imtr.colliderect(b12):
				if b12.collidepoint(pos):
					pygame.mixer.Sound.play(keo)
					c=a12
					a12=trong
					trong=c
#5
			if imgtr.colliderect(b13) or imtr.colliderect(b13):
				if b13.collidepoint(pos):
					pygame.mixer.Sound.play(keo)
					c=a13
					a13=trong
					trong=c
#6
			if b14.colliderect(imgtr)or imtr.colliderect(b14):
				if b14.collidepoint(pos):
					pygame.mixer.Sound.play(keo)
					c=a14
					a14=trong
					trong=c
#7
			if b15.colliderect(imgtr)or imtr.colliderect(b15):
				if b15.collidepoint(pos):
					pygame.mixer.Sound.play(keo)
					c=a15
					a15=trong
					trong=c
	if a1==1 and a2==2 and a3==3 and a4==4 and a5==5 and a6==6 and a7==7 and a8==8 and a9==9 and a11==11 and a12==12 and a13==13 and a14==14 and a10==10 and a15==15:
			screen.blit(chu,(50,500))
			pygame.mixer.Sound.play(win)
			
	pygame.display.flip()
pygame.quit()