#coding=utf-8
import pygame
from pygame.sprite import Group
from settings import Settings
from game_status import GameStatus
from ship import Ship
from alien import Alien
import game_functions as gf
def run_game():
	# ��ʼ����Ϸ������һ����Ļ����
	pygame.init();	
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	
	# ����һ�ҷɴ�
	ship = Ship(screen, ai_settings)	
	
	# ����һ�����ڴ洢�ӵ��ı���
	bullets = Group()
	aliens = Group()
	
	# ����������Ⱥ
	gf.create_fleet(ai_settings, screen, ship, aliens)
	
	# ����һ�����ڴ洢��Ϸͳ����Ϣ��ʵ��
	status = GameStatus(ai_settings)

	# ��ʼ��Ϸ����ѭ��
	while True:
		# ���Ӽ��̺�����¼�
		gf.check_events(ai_settings, screen, ship, bullets)
		if status.game_active:
			ship.update()
			# ɾ������ʧ���ӵ�
			gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
			gf.update_aliens(ai_settings, status, screen, ship, aliens, bullets)
			#gf.dectet_fire(bullets, aliens)
		gf.update_screen(ai_settings, screen, ship, aliens, bullets)	
		
			
run_game()
