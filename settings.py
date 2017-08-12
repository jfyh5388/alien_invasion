#coding=utf-8
class Settings():
	#�洢�����������֡����������õ���
	def __init__(self):
		#��ʼ����Ϸ������
		# ��Ļ����
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)
		#self.bg_color = (0, 0, 255)
		
		# �ӵ�����
		self.bullet_speed_factor = 3
		self.bullet_width = 300
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		self.bullets_allowed = 3
		
		self.alien_speed_factor = 1
		self.fleet_drop_speed = 10
		# fleet_directionΪ1��ʾ�����ƣ�Ϊ-1��ʾ������
		self.fleet_direction = 1
		
		# �ɴ�����
		self.ship_speed_factor = 1.5
		self.ship_limit = 3
		
		# ��ʲô�����ٶȼӿ���Ϸ����
		self.speedup_scale = 1.5
		self.initialize_dynamic_settings()
		
	def initialize_dynamic_settings(self):
		#"""��ʼ������Ϸ���ж��仯������"""
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 3
		self.alien_speed_factor = 1
		# fleet_directionΪ1��ʾ���ң�Ϊ-1��ʾ����
		self.fleet_direction = 1
	
	def increase_speed(self):
		#"""����ٶ�����"""
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
