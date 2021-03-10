import pygame
import sys





class Room(object):

	def room_1(self,mainWindow):

	# Setting Screen Size
		pygame.init()
		screen = pygame.display.set_mode((1920,1000))
		clock = pygame.time.Clock()
		DISPLAYSURF = pygame.display.set_mode((0, 0),pygame.RESIZABLE)
		bg = pygame.image.load("Chair_bg.jpg")

		room_map = pygame.Surface((250,250))
		room_map.fill((128,128,128))
		room_border = pygame.Rect(1495,95,260,260)


		size = 20


		puzzle_rect = pygame.Rect(1735,335,15,15)

		x_pos = 1515																				# Starting Position
		y_pos =	115 



		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:														# Code for exiting the game
					pygame.quit()
					sys.exit()

				if event.type == pygame.KEYDOWN:													# Code for Movement
					if event.key == pygame.K_LEFT or event.key == ord("a"):
						if x_pos <= 1515:
							print("Cannot move further in this direction") 
						else:
							x_pos -= 15
							print("left")
					if event.key == pygame.K_RIGHT or event.key == ord("d"):
						if x_pos >= 1735:
							print("Cannot move further in this direction") 
						else:
							x_pos += 15
							print("right")
					if event.key == pygame.K_UP or event.key == ord("w"):
						if y_pos <= 115:
							print("Cannot move further in this direction") 
						else:
							y_pos -= 15
							print("forward")
					if event.key == pygame.K_DOWN or event.key == ord("s"):
						if y_pos >= 335:
							print("Cannot move further in this direction") 
						else:
							y_pos += 15
							print("backward")
						

			pygame.display.set_caption("Sherlock's Escape")
			screen.blit(bg,(0, 0))	
																			# Setting the bckground image
			
			pygame.draw.rect(screen,(255,255,255),room_border)
			screen.blit(room_map,(1500,100))														# blit = block image transfer 

			pygame.draw.circle(screen,(250,0,0),(x_pos,y_pos),5)
			pygame.draw.rect(screen,(0,0,0),puzzle_rect)

			font = pygame.font.Font('Poppins-Regular.ttf', 75)
			text = font.render('Room 1', True, (255,255,255))
			textRect = text.get_rect()
			textRect.center = (200,100)
			screen.blit(text,textRect)


			#puzzle = PUZZLE()
			pygame.display.update()
			clock.tick(60)																			# Setting the frame rate 

