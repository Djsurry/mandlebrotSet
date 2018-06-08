import pygame, random


WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
rainbow = [(148, 0, 211), (75, 0, 130), (0, 0, 245), (0, 245, 0), (245, 245, 0), (245, 127, 0), (245, 0, 0)]

displayWidth = 800
displayHieght = 800

gameDisplay = pygame.display.set_mode((displayWidth,displayHieght))

pygame.display.set_caption('Madlebrot Set')
points = []
gameDisplay.fill(BLACK)

def remap(oldValue, oldMax, oldMin, newMax, newMin):
	return (((oldValue - oldMin) * (newMax - newMin)) / (oldMax - oldMin)) + newMin

for x in range(displayWidth):
	for y in range(displayHieght):
		a = remap(x, displayWidth, 0, 2, -2)
		b = remap(y, displayHieght, 0, 2, -2)
		oa = a

		ob = b
		maxI = 50
		n = 0
		while n != maxI:
			aa = a*a-b*b
			bb = 2*a*b
			a =aa + oa
			b = bb+ ob
			if abs(a + b) > 16:
				break
			n+=1
		

		#gameDisplay.set_at((x, y), (remap(n, 50, 0, 0, 155), remap(n, 50, 0, 0, 123), remap(n, 50, 0, 0, 50)))
		if n > 45 and n < 50:
			gameDisplay.set_at((x, y), rainbow[0])
		elif n > 40 and n < 45:
			gameDisplay.set_at((x, y), rainbow[1])
		elif n > 35 and n < 40:
			gameDisplay.set_at((x, y), rainbow[2])
		elif n > 30 and n < 45:
			gameDisplay.set_at((x, y), rainbow[3])
		elif n > 25 and n < 30:
			gameDisplay.set_at((x, y), rainbow[4])
		elif n > 20 and n < 25:
			gameDisplay.set_at((x, y), rainbow[5])
		elif n > 0 and n < 20:
			gameDisplay.set_at((x, y), rainbow[6])
		else:
			gameDisplay.set_at((x, y), (0,0,0))
pygame.display.update()
while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
