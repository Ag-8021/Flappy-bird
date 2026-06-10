import pygame
import random

#Start
pygame.init()

#Open window
screen=pygame.display.set_mode((400,600))

#Clock
clock=pygame.time.Clock()

#Font
font = pygame.font.SysFont(None, 36)
title_font = pygame.font.SysFont(None, 40)
score_font = pygame.font.SysFont(None, 30)

#Colour
SKY_BLUE = (135, 206, 235)   
YELLOW=(255,255,0)
GREEN=(0,255,0)

#Bird variables
bird_y=300
gravity=0.2
bird_vy=0

#Pipe variables
pipe_x=300
pipe_gap=150
pipe_height=random.randint(50,400)
passed_pipe=False

#Score counter
score=0

#Ready screen
screen.fill(SKY_BLUE)
ready_surface=font.render(f"FLAPPY BIRD",True,(0,0,0))
screen.blit(ready_surface,(120,300))
pygame.display.flip()

#Time delay-2s
pygame.time.delay(2000)

#Running
running=True
while running:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                bird_vy=-6
    
    bird_vy+=gravity
    bird_y+=bird_vy
    pipe_x-=4

    if pipe_x<=-70:
        pipe_x=400
        pipe_height=random.randint(50,400)
        passed_pipe=False

    screen.fill(SKY_BLUE)

    pygame.draw.circle(screen,YELLOW,(40,int(bird_y)),20)
    pygame.draw.rect(screen, GREEN, (pipe_x, 0, 70, pipe_height))
    bottom_y=pipe_height+pipe_gap
    bottom_height=600-bottom_y
    pygame.draw.rect(screen, GREEN, (pipe_x, bottom_y, 70, bottom_height))

    bird_rect=pygame.Rect(20,int(bird_y)-20,40,40)
    top_pipe_rect=pygame.Rect(pipe_x,0,70,pipe_height)
    bottom_pipe_rect=pygame.Rect(pipe_x,bottom_y,70,bottom_height)

    if bird_rect.colliderect(top_pipe_rect) or bird_rect.colliderect(bottom_pipe_rect):
        running=False
    if bird_y>600 or bird_y<0:
        running=False
    if pipe_x<40 and passed_pipe==False:
        score+=1
        passed_pipe=True
    
    score_surface=font.render(f"Score:{score}",True,(0,0,0))
    screen.blit(score_surface,(10,10))

    pygame.display.flip() 

game_over=True
while game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=False

    box_rect = pygame.Rect(0, 0, 250, 150)
    box_rect.center = screen.get_rect().center

    pygame.draw.rect(screen, (255, 255, 255), box_rect)
    pygame.draw.rect(screen, (50, 50, 50), box_rect, 4)

    title_surface = title_font.render("GAME OVER", True, (200, 0, 0))
    title_rect = title_surface.get_rect(center=(box_rect.centerx, box_rect.centery - 20))

    final_score_surface = score_font.render(f"Final Score: {score}", True, (0, 0, 0))
    score_rect = final_score_surface.get_rect(center=(box_rect.centerx, box_rect.centery + 20))

    screen.blit(title_surface, title_rect)
    screen.blit(final_score_surface, score_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()