import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
	#"""��ʾ���������˵���"""
	def __init__(self, ai_settings, screen):
	#"""��ʼ�������˲���������ʼλ��"""
		super(Alien, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings
		# ����������ͼ�񣬲�������rect����
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()
		# ÿ�����������������Ļ���ϽǸ���
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		# �洢�����˵�׼ȷλ��
		self.x = float(self.rect.x)

	def blitme(self):
		#"""��ָ��λ�û���������""
		self.screen.blit(self.image, self.rect)