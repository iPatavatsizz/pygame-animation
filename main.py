import pygame
from sys import exit

if not pygame.get_init(): pygame.init()

"""
load your animations dictionary list like:
animations = {
	'left': [animation surfaces],
	'right': [animation surfaces],
}
"""
animations = {}
animation_count = 0
animation_state = 'idle'
animation_direction = 'left'
pos = [0, 0]
speed =  1

# create timer
animate = pygame.USEREVENT
pygame.time.set_timer(animate, 75)  # set this number in ms by yourself, my character had 3 frame animation, so I set this.

pygame.display.set_caption('implementing timer based animation')
display = pygame.display.set_mode((800, 600), depth=32)

while True:
	# get key list
	keys = pygame.key.get_pressed()
	if self.keys[pygame.K_ESCAPE]: exit()

	# initial events and check animation timer.
	for event in pygame.event.get():
		if event.type == animate:
			if character_state == 'running': animation_count += 1
			if character_state == 'idle': animation_count = 0


	# clean the surface/display.
	display.fill('black')

	if keys[pygame.K_w]:
		pos[1] -= speed
		character_state = 'running'
	if keys[pygame.K_s]:
		pos[1] += speed
		character_state = 'running'
	if keys[pygame.K_a]:
		animation_direction = 'left'
		character_state = 'running'
		pos[0] -= speed
	if keys[pygame.K_d]:
		animation_direction = 'right'
		character_state = 'running'
		pos[0] += speed

	# if animation count exceed max. animation limit, set 0 for repeating animation.
	if animation_count >= len(animations.get(animation_direction)): animation_count = 0
	display.blit(animations.get(animation_direction)[animation_count], pos)
