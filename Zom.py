# Simple pygame program

# Import and initialize the pygame library
import pygame
import os



pygame.init()

# Set up the drawing window (input take a list or a tuple)
window = (1600, 800)
screen = pygame.display.set_mode(window)

# background image
bg = pygame.image.load(os.path.join('textures', 'bg.jpg')) #.convert()
bgX = 0 # x position of first image
bgX2 = bg.get_width() # x position of second image (starts when the first one ends)

# clock setting
clock = pygame.time.Clock()



def updateScreen():
    screen.blit(bg, (bgX, 0))
    screen.blit(bg, (bgX2, 0))
    pygame.display.update()
    # update vs flip:
    # flip updates ALL screen
    # update only updates part of the screen.
    #   called with no arguments is the same as flip



# custom events
increaseSpeed = pygame.USEREVENT + 1

# trigger custom event every 500 ms
pygame.time.set_timer(increaseSpeed, 500)

speed = 30

# Run until the user asks to quit
running = True
while running:

    updateScreen()

    bgX -= 1.4
    bgX2 -= 1.4
    if bgX < bg.get_width() * -1:
        bgX = bg.get_width()
    if bgX2 < bg.get_width() * -1:
        bgX2 = bg.get_width()

    # Handles events within the game execution
    for event in pygame.event.get():

        # if the user wants to quit
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()
        if event.type == increaseSpeed:
            speed += 1

    # tick the game clock at "speed" variable intervals
    clock.tick(speed)



    # # other custom code
    # # Fill the background with white
    # screen.fill((255, 255, 255))

    # # Draw a solid blue circle in the center
    # pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
    # #                           RGB values   center     radius

    # # Updates the display content
    # pygame.display.flip()




# Done! Time to quit.
pygame.quit()