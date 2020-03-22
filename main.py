import pygame
import random #to generate food

pygame.init()
pygame.mixer.init()

SCREEN_WIDTH=900
SCREEN_HEIGHT=600
#COLORS
red=(255,0,0)
white=(255,255,255)
black=(0,0,0)
wonderfull=(90,15,74)
#Main Game Window

Game_Window=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

pygame.display.set_caption("Python with Python (sarcasm)")

pygame.display.update()


fps=57
clock=pygame.time.Clock()

font=pygame.font.SysFont(None,55)
def score_on_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    Game_Window.blit(screen_text,[x,y])



def plt_snake(Game_Window,red,py_list,python_size):
    for x,y in py_list:
        pygame.draw.rect(Game_Window,red,[x,y,python_size,python_size]) 


def welcome():
    exit_game = False
    while not exit_game:
        Game_Window.fill((233,10,29))
        score_on_screen("Welcome to PYTHON ", black, 260, 250)
        score_on_screen("Press Space Bar To Play", black, 232, 290)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                   
                    maingame()

        pygame.display.update()
        clock.tick(60)



#Main Game Loop
def maingame():
        #Main Game Variables
    exit_game= False
    game_over=False
    python_x=45 
    python_y=45
    python_size=25
    py_list=[]
    py_lenght=1


    food_x=random.randint(20,SCREEN_WIDTH-20)
    food_y=random.randint(20,SCREEN_HEIGHT-20)

    velocity_x=0
    velocity_y=0

    score=0

    while not exit_game:

        if game_over:
            Game_Window.fill(white)
            score_on_screen("Game Over! Press Enter To Continue", red, 100, 250)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        maingame()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_LEFT:
                        velocity_x=-5
                        velocity_y=0
                    if event.key==pygame.K_RIGHT:
                        velocity_x=5
                        velocity_y=0
                    if event.key==pygame.K_UP:
                        velocity_x=0
                        velocity_y=-5       
                    if event.key==pygame.K_DOWN:
                        velocity_x=0
                        velocity_y=5


            python_x+=velocity_x
            python_y+=velocity_y

            if abs(python_x-food_x)<13 and abs(python_y-food_y)<13:
                score+=1
                print("Score = ",score*10)

                
                py_lenght+=5
                food_x=random.randint(20,SCREEN_WIDTH-20)
                food_y=random.randint(20,SCREEN_HEIGHT-20)     #RELOCATING FOOD
            Game_Window.fill(white)
            score_on_screen("Score = "+ str(score*10),wonderfull,400,30)
            pygame.draw.rect(Game_Window,wonderfull,[food_x,food_y,python_size,python_size])

            head=[]
            head.append(python_x)
            head.append(python_y)
            py_list.append(head)
            
            if len(py_list)>py_lenght:
                del py_list[0]

            if head in py_list[:-1]:
                game_over = True    

            if python_x<0 or python_y<0 or python_x>SCREEN_WIDTH or python_y>SCREEN_HEIGHT:
                game_over=True
                print("Game Over")    

            pygame.draw.rect(Game_Window,red,[python_x,python_y,python_size,python_size])
            plt_snake(Game_Window,red,py_list,python_size)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()        

welcome()        
