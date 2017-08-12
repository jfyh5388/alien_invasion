#coding=utf-8
import sys
import pygame
from bullet import Bullet
from time import sleep
from alien import Alien
import file_io

def check_keydown_events(event, ai_settings, screen, ship, bullets, status):
	#"""��Ӧ����"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE and status.game_active == True:
		fire_bullet(ai_settings, screen, ship, bullets)
	elif event.key == pygame.K_q:
		file_io.writedata(status.high_score, ai_settings.store_file)
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

def check_events(ai_settings, screen, status, play_button, ship, aliens, bullets, sb):
	#"""��Ӧ����������¼�"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, ship, bullets, status)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_play_button(ai_settings, screen, status, play_button, ship, aliens, bullets, mouse_x, mouse_y, sb)
			

def check_play_button(ai_settings, screen, status, play_button, ship, aliens, bullets, mouse_x, mouse_y, sb):
	#"""����ҵ���Play��ťʱ��ʼ����Ϸ"""
	button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
	if button_clicked and not status.game_active:		
		# ������Ϸ����
		ai_settings.initialize_dynamic_settings()
		# ���ع��
		pygame.mouse.set_visible(False)
		#������Ϸͳ����Ϣ
		# ������Ϸͳ����Ϣ
		status.reset_status()		
		status.game_active = True		
		# ���üǷ���ͼ��
		sb.prep_score()
		sb.prep_high_score()
		sb.prep_level()
		sb.prep_ships()
		# ����������б���ӵ��б�
		aliens.empty()
		bullets.empty()
		# ����һȺ�µ������ˣ����÷ɴ�����
		create_fleet(ai_settings, screen, ship, aliens)
		ship.center_ship()
		#status.ships_left = status.ai_settings.ship_limit
			
def update_bullets(ai_settings, screen, ship, aliens, bullets, status, sb):
	#"""�����ӵ���λ�ã���ɾ������ʧ���ӵ�"""
	# �����ӵ���λ��
	bullets.update()
	# ɾ������ʧ���ӵ�
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	# ����Ƿ����ӵ�������������
	# �������������ɾ����Ӧ���ӵ���������	
	check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets, status, sb)
		
def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets, status, sb):
	#"""��Ӧ�ӵ��������˵���ײ"""
	# ɾ��������ײ���ӵ���������
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
	if collisions:
		for aliens in collisions.values():
			status.score += ai_settings.alien_points * len(aliens)
			sb.prep_score()
		check_high_score(status, sb)
	if len(aliens) == 0:
		# ɾ�����е������ӵ���������һ���µ�������Ⱥ
		bullets.empty()
		ai_settings.increase_speed()
		# ��ߵȼ�
		status.level += 1
		sb.prep_level()
		create_fleet(ai_settings, screen, ship, aliens)
		
def check_high_score(status, sb):
	#"""����Ƿ������µ���ߵ÷�"""
	if status.score > status.high_score:
		status.high_score = status.score
		sb.prep_high_score()
				
def update_screen(ai_settings, screen, status, ship, aliens, bullets, play_button, sb):
	#������Ļ�ϵ�ͼ�񣬲��л�������Ļ
	# ÿ��ѭ��ʱ���ػ���Ļ
	screen.fill(ai_settings.bg_color)	
	# �ڷɴ��������˺����ػ������ӵ�
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
	#aliens.blitme()
	aliens.draw(screen)
	# �����Ϸ���ڷǻ״̬���ͻ���Play��ť
	if not status.game_active:
		play_button.draw_button()
	sb.show_score()
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

def ship_hit(ai_settings, status, screen, ship, aliens, bullets, sb):
	#"""��Ӧ��������ײ���ķɴ�"""
	# ��ships_left��1
	if status.ships_left > 1:
		status.ships_left -= 1
		# ����������б���ӵ��б�
		# ���¼Ƿ���
		sb.prep_ships()
		aliens.empty()
		bullets.empty()
		# ����һȺ�µ������ˣ������ɴ��ŵ���Ļ�׶�����
		create_fleet(ai_settings, screen, ship, aliens)
		ship.center_ship()
		# ��ͣ
		sleep(0.5)
	else:
		status.ships_left -= 1
		sb.prep_ships()
		status.game_active = False
		pygame.mouse.set_visible(True)

def update_aliens(ai_settings, status, screen, ship, aliens, bullets, sb):
	#"""	
	#����Ƿ���������λ����Ļ��Ե����������Ⱥ�����˵�λ��
	#"""
	check_fleet_edges(ai_settings, aliens)
	aliens.update()
	
	# ��������˺ͷɴ�֮�����ײ
	if pygame.sprite.spritecollideany(ship, aliens):
		ship_hit(ai_settings, status, screen, ship, aliens, bullets, sb)
		
	# ����Ƿ��������˵�����Ļ�׶�
	check_aliens_bottom(ai_settings, status, screen, ship, aliens, bullets, sb)
		
def check_aliens_bottom(ai_settings, status, screen, ship, aliens, bullets, sb):
	#"""����Ƿ��������˵�������Ļ�׶�"""
	screen_rect = screen.get_rect()	
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			# ��ɴ���ײ��һ�����д���
			ship_hit(ai_settings, status, screen, ship, aliens, bullets, sb)
			break
		

	
#def dectet_fire(bullets, aliens):
	#for bullet in bullets.sprites():
		#for alien in aliens.sprites():
			#if(bullet.rect.top <= alien.rect.bottom and bullet.rect.bottom > alien.rect.top and bullet.rect.right >= alien.rect.left and bullet.rect.left <= alien.rect.right):
				#aliens.remove(alien)
