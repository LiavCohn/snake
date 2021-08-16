import pygame
import os
import random
pygame.init()
pygame.font.init()

pygame.display.set_caption("Snake")

#Global Varibles
FPS=15


#Window vars
WIDTH=450
HEIGHT=450
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
BLOCK_SIZE=20
FOOD_SIZE=30


#images/font etc...
SPACE_BACKGROUND=pygame.image.load(os.path.join('Assets','space.png'))
HEALTH_FONT= pygame.font.SysFont('comicsans', 30)
FOOD_IMAGE=pygame.image.load(os.path.join('Assets','snake_food.png'))
FOOD=pygame.transform.scale(FOOD_IMAGE,(FOOD_SIZE,FOOD_SIZE))

#Colors
WHITE=(255,255,255)
BLACK=(0,0,0)
RED= (255,0,0)
YELLOW=(255,255,0)
BLUE=(0, 96, 128)
DARK_BLUE=(0, 37, 51)
GREEN=(113, 218, 113)

def draw_grid():
    
    for x in range(0,WIDTH,BLOCK_SIZE):
        for y in range(0,HEIGHT,BLOCK_SIZE):
            rect= pygame.Rect(x,y,BLOCK_SIZE,BLOCK_SIZE)
            pygame.draw.rect(WIN,WHITE,rect,1)


    #pygame.display.update()

def draw_window(snake,x,y):
    snake.x+=x
    snake.y+=y
    pygame.draw.rect(WIN,YELLOW,snake)
    pygame.display.update()

def draw_snake(snake_list):
    i=1
    for x in snake_list:
        if i==len(snake_list):
            pygame.draw.rect(WIN,YELLOW,(x[0], x[1], 20,20))
            
        else:
            pygame.draw.rect(WIN,DARK_BLUE,(x[0], x[1], 20,20))
            i+=1
        
def generate_food(food,snake_list):
    found=False
    while(not found):
        x=random.randrange(0,WIDTH-FOOD_SIZE)
        y=random.randrange(0,HEIGHT-FOOD_SIZE)
        if not [x,y] in snake_list:
            found= True

    food_x= x
    food_y= y
    food.center=(food_x,food_y)

def display_message(text):
    draw_text = HEALTH_FONT.render(text, 1,WHITE)
    WIN.blit(draw_text, (WIDTH//2- draw_text.get_width()/2, HEIGHT//2- draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)

def display_score(score):
    score_text= HEALTH_FONT.render("Score: "+str(score), 1, WHITE)
    WIN.blit(score_text, (10, 10))

def lost_game():
    WIN.fill(DARK_BLUE)
    display_message("You Lost!")
    pygame.quit()

def food_gen():
    food_x= random.randrange(0,WIDTH)
    food_y= random.randrange(0,HEIGHT)
    WIN.blit(FOOD,(food_x,food_y))

def main():
    run=True
    clock= pygame.time.Clock()
    score=0
    x=WIDTH//2-11
    y=HEIGHT//2-11
    x_change=0
    y_change=0
    snake_len=1

    #make a rect object for the food
    food=FOOD.get_rect()

    time_since_last_action = 0
    snake_list=[]

    generate_food(food,snake_list)

    while run:
        
        dt=clock.tick(FPS)
        time_since_last_action += dt

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False


            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    x_change=0
                    y_change=-20
                elif event.key== pygame.K_DOWN:
                    x_change= 0
                    y_change= 20
                elif event.key== pygame.K_LEFT:
                    x_change= -20
                    y_change=0
                elif event.key== pygame.K_RIGHT:
                    x_change=20
                    y_change=0
        if not(run):
            pygame.quit()
            break

        if x>=WIDTH-20 or x<=0 or y<=0 or y>=HEIGHT-20:
            lost_game()
            break
     
        snake_head=[]

        x+=x_change
        y+=y_change

        WIN.blit(SPACE_BACKGROUND,(0,0))

        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)
        
        if len(snake_list)>snake_len:
            del snake_list[0]

        for body_part in snake_list[:-1]:
            if body_part==snake_head:
                lost_game()
                break

        
        WIN.blit(FOOD,food)
        

        if time_since_last_action>=4000:
            generate_food(food,snake_list)
            dt=0
            WIN.blit(FOOD,food)
            time_since_last_action=0


        display_score(score)
        draw_snake(snake_list)
        pygame.display.update()

    
        snake=pygame.Rect(x, y ,20,20)
        if food.colliderect(snake):
            score+=1
            generate_food(food,snake_list)
            WIN.blit(FOOD,food)
            snake_len+=1

        

    #main() 
    #pygame.quit()
    #quit()

if __name__=="__main__":
    main()  




  
