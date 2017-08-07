#coding=utf-8
import pygame
class Ship():
	def __init__(self, screen, settings):
		#��ʼ���ɴ����������ʼλ��
		self.screen = screen
		self.ai_settings = settings
		# ���طɴ�ͼ�񲢻�ȡ����Ӿ���
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		# ��ÿ���·ɴ�������Ļ�ײ�����
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
		# �ڷɴ�������center�д洢С��ֵ
		self.centerx = float(self.rect.centerx)
		# �ƶ���־
		self.moving_right = False
		self.moving_left = False
		
	def update(self):
		#"""�����ƶ���־�����ɴ���λ��"""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.centerx += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.centerx -= self.ai_settings.ship_speed_factor
			
		# ����self.center����rect����
		self.rect.centerx = self.centerx
			
	def blitme(self):
		#��ָ��λ�û��Ʒɴ�
		self.screen.blit(self.image, self.rect)

	def center_ship(self):
		#"""�÷ɴ�����Ļ�Ͼ���"""
		self.centerx = self.screen_rect.centerx
