class GameStatus():
	#"""������Ϸ��ͳ����Ϣ"""
	def __init__(self, ai_settings):
		#"""��ʼ��ͳ����Ϣ"""
		self.ai_settings = ai_settings
		self.reset_stats()
		# ��Ϸ������ʱ���ڻ״̬
		self.game_active = True
	def reset_stats(self):
		#"""��ʼ������Ϸ�����ڼ���ܱ仯��ͳ����Ϣ"""
		self.ships_left = self.ai_settings.ship_limit
