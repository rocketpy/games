import pygame


pygame.init()

new_window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("New window")  # Title

x = 50
y = 50
width = 40
height = 60
vel =  #  velocity

run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get()
        if even.type == pygame.QUIT:
            run = False
            
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:    
        y += vel
    pygame.draw.rect(new_window, (255, 0, 0), (x, y, width, height))        
    pygame.display.update()
    
pygame.quit()            
