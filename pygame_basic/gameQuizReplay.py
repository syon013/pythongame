import pygame
import random

# 기본 초기화 (반드시 해야 하는 것들)
#########################################################################################################################
pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("파이썬 게임") # 게임 이름

# FPS
clock = pygame.time.Clock()
#########################################################################################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
#########################################################################################################################

# 배경 이미지 불러오기

background = pygame.image.load("D:/pythongame/pygame_basic/background.png")

# 스프라이트 (캐릭터) 불러오기

character = pygame.image.load("D:/pythongame/pygame_basic/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_hight = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_hight

# 이동할 좌표

to_x = 0
to_y = 0

# 이동 속도

character_speed = 0.6

# 스프라이트 적 enemy 캐릭터 불러오기

enemy = pygame.image.load("D:/pythongame/pygame_basic/enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_hight = enemy_size[1]
enemy_x_pos = (screen_width / 2) - (enemy_width / 2)
enemy_y_pos = (screen_height / 2) - (enemy_hight / 2)

# 폰트 정의

game_font = pygame.font.Font(None, 40)

# 총 시간

total_time = 0

# 시작 시간

start_ticks = pygame.time.get_ticks()


# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(30) # 게임화면의 초당 프레임 수를 설정

#########################################################################################################################

    # 2. 이벤트 처리 (키보드, 마우스 등)
#########################################################################################################################    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 

        if event.type == pygame.KEYDOWN: # 방향키가 눌리면
            if event.key == pygame.K_LEFT: 
                to_x -= character_speed

            elif event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
            to_x == 0

#########################################################################################################################

    # 3. 게임 캐릭터 위치 정의
#########################################################################################################################

 

#########################################################################################################################

    # 4. 충돌 처리
#########################################################################################################################

 

    # 충돌 체크
    

#########################################################################################################################
#    # 5. 화면에 그리기        

    screen.blit(background, (0, 0))

    screen.blit(character, (character_x_pos, character_y_pos))

    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
   

    # 타이머 집어 넣기
    # 경과 시간 계산
   

#########################################################################################################################
#   # 6. 게임 화면을 다시 그리기    
    
    pygame.display.update() # 게임화면을 다시 그리기

# 잠시 대기
pygame.time.delay(2000) # 2초 정도 대기(ms)


# pygame 종료
pygame.quit()