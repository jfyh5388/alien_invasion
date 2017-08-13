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
	# ��ʼ����Ϸ������һ����Ļ����
	pygame.init();	
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	play_button = Button(ai_settings, screen, "Play")
	
	# ����һ�ҷɴ�
	ship = Ship(ai_settings, screen)	
	
	# ����һ�����ڴ洢�ӵ��ı���
	bullets = Group()
	aliens = Group()
	
	# ����������Ⱥ
	gf.create_fleet(ai_settings, screen, ship, aliens)
	
	# ����һ�����ڴ洢��Ϸͳ����Ϣ��ʵ��
	status = GameStatus(ai_settings)
	
	sb = Scoreboard(ai_settings, screen, status)
	
	pygame.mixer.music.load("sounds/background.wav")
	pygame.mixer.music.play(-1, 0.0)

	#��ʼ��Ϸ����ѭ��
	while True:
		# ���Ӽ��̺�����¼�
		gf.check_events(ai_settings, screen, status, play_button, ship, aliens, bullets, sb)
		if status.game_active:
			ship.update()
			# ɾ������ʧ���ӵ�
			gf.update_bullets(ai_settings, screen, ship, aliens, bullets, status, sb)
			gf.update_aliens(ai_settings, status, screen, ship, aliens, bullets, sb)
			#gf.dectet_fire(bullets, aliens)
		gf.update_screen(ai_settings, screen, status, ship, aliens, bullets, play_button, sb)	
		
			
run_game()
