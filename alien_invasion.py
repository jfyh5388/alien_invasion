#coding=utf-8
import pygame
from pygame.sprite import Group
from settings import Settings
from game_status import GameStatus
from ship import Ship
from alien import Alien
from button import Button
from scoreboard import Scoreboard
import game_functions as gf
def run_game():
	# 初始化游戏并创建一个屏幕对象
	pygame.init();	
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	play_button = Button(ai_settings, screen, "Play")
	
	# 创建一艘飞船
	ship = Ship(ai_settings, screen)	
	
	# 创建一个用于存储子弹的编组
	bullets = Group()
	aliens = Group()
	
	# 创建外星人群
	gf.create_fleet(ai_settings, screen, ship, aliens)
	
	# 创建一个用于存储游戏统计信息的实例
	status = GameStatus(ai_settings)
	
	sb = Scoreboard(ai_settings, screen, status)
	
	pygame.mixer.music.load("sounds/background.wav")
	pygame.mixer.music.play(-1, 0.0)

	#开始游戏的主循环
	while True:
		# 监视键盘和鼠标事件
		gf.check_events(ai_settings, screen, status, play_button, ship, aliens, bullets, sb)
		if status.game_active:
			ship.update()
			# 删除已消失的子弹
			gf.update_bullets(ai_settings, screen, ship, aliens, bullets, status, sb)
			gf.update_aliens(ai_settings, status, screen, ship, aliens, bullets, sb)
			#gf.dectet_fire(bullets, aliens)
		gf.update_screen(ai_settings, screen, status, ship, aliens, bullets, play_button, sb)	
		
			
run_game()
