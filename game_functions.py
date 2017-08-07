#coding=utf-8
import sys
import pygame
from bullet import Bullet
from time import sleep
from alien import Alien

def check_keydown_events(event, ai_settings, screen, ship, bullets):
	#"""��Ӧ����"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings, screen, ship, bullets)
	elif event.key == pygame.K_q:
		sys.exit()
		
def fire_bullet(ai_settings, screen, ship, bullets):
	#"""�����û�е������ƣ��ͷ���һ���ӵ�"""	
	#�������ӵ�����������뵽����bullets��
	if len(bullets) < ai_settings.bullets_allowed:
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)

def check_keyup_events(event, ship):
	#"""��Ӧ�ɿ�"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
	#"""��Ӧ����������¼�"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, ship, bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)
			
def update_bullets(ai_settings, screen, ship, aliens, bullets):
	#"""�����ӵ���λ�ã���ɾ������ʧ���ӵ�"""
	# �����ӵ���λ��
	bullets.update()
	# ɾ������ʧ���ӵ�
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	# ����Ƿ����ӵ�������������
	# �������������ɾ����Ӧ���ӵ���������	
	check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)
		
def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
	#"""��Ӧ�ӵ��������˵���ײ"""
	# ɾ��������ײ���ӵ���������
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
	if len(aliens) == 0:
		# ɾ�����е������ӵ���������һ���µ�������Ⱥ
		bullets.empty()
		create_fleet(ai_settings, screen, ship, aliens)
				
def update_screen(ai_settings, screen, ship, aliens, bullets):
	#������Ļ�ϵ�ͼ�񣬲��л�������Ļ
	# ÿ��ѭ��ʱ���ػ���Ļ
	screen.fill(ai_settings.bg_color)	
	# �ڷɴ��������˺����ػ������ӵ�
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
	#aliens.blitme()
	aliens.draw(screen)
	# ��������Ƶ���Ļ�ɼ�
	pygame.display.flip()


def get_number_aliens_x(ai_settings, alien_width):
	#"""����ÿ�п����ɶ��ٸ�������"""
	available_space_x = ai_settings.screen_width - 2 * alien_width
	number_aliens_x = int(available_space_x / (2 * alien_width))
	return number_aliens_x
	
def get_number_rows(ai_settings, ship_height, alien_height):
	#"""������Ļ�����ɶ�����������"""
	available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
	number_rows = int(available_space_y / (2 * alien_height))
	return number_rows
	
def create_alien(ai_settings, screen, aliens, alien_number, row_number):
	#"""����һ�������˲�������ڵ�ǰ��"""
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width
	alien.x = alien_width + 2 * alien_width * alien_number
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
	aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
	#"""����������Ⱥ"""	
	# ����һ�������ˣ�������һ�п����ɶ��ٸ�������
	# �����˼��Ϊ�����˿��
	alien = Alien(ai_settings, screen)
	number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
	number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
	# ������һ��������
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			create_alien(ai_settings, screen, aliens, alien_number, row_number)

def check_fleet_edges(ai_settings, aliens):
#"""�������˵����Եʱ��ȡ��Ӧ�Ĵ�ʩ"""
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings, aliens)
			break
			
def change_fleet_direction(ai_settings, aliens):
	#"""����Ⱥ���������ƣ����ı����ǵķ���"""
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *= -1

def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
	#"""��Ӧ��������ײ���ķɴ�"""
	# ��ships_left��1
	if stats.ships_left > 0:
		stats.ships_left -= 1
		# ����������б���ӵ��б�
		aliens.empty()
		bullets.empty()
		# ����һȺ�µ������ˣ������ɴ��ŵ���Ļ�׶�����
		create_fleet(ai_settings, screen, ship, aliens)
		ship.center_ship()
		# ��ͣ
		sleep(0.5)
	else:
		stats.game_active = False

def update_aliens(ai_settings, status, screen, ship, aliens, bullets):
	#"""	
	#����Ƿ���������λ����Ļ��Ե����������Ⱥ�����˵�λ��
	#"""
	check_fleet_edges(ai_settings, aliens)
	aliens.update()
	
	# ��������˺ͷɴ�֮�����ײ
	if pygame.sprite.spritecollideany(ship, aliens):
		ship_hit(ai_settings, status, screen, ship, aliens, bullets)
	
#def dectet_fire(bullets, aliens):
	#for bullet in bullets.sprites():
		#for alien in aliens.sprites():
			#if(bullet.rect.top <= alien.rect.bottom and bullet.rect.bottom > alien.rect.top and bullet.rect.right >= alien.rect.left and bullet.rect.left <= alien.rect.right):
				#aliens.remove(alien)
