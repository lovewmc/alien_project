# coding=gbk
import pygame

class Ship():
	def __init__(self,ai_settings,screen):
		"""��ʼ���ɴ����������ʼλ��"""
		self.screen  = screen
		#�ƶ���־����Ұ��·����ʱ��־��ΪTrue����ʼ�ƶ����ɿ��ͱ��False
		self.moving_right = False
		self.moving_left = False
		self.ai_settings = ai_settings
		
		#���طɴ�ͼ�񲢻�ȡ����Ӿ���,���ص���һ����ʾ�ɴ���surface
		self.image = pygame.image.load('images/ship.bmp').convert_alpha()
		self.oimage = self.image
		#��ȡ��ͼƬ������rect����
		self.rect = self.image.get_rect()
		self.position = self.coprect = self.rect    
		
		#��ȡ��Ļ��rect����
		self.screen_rect = screen.get_rect()
		
		#����ͼ���С
		self.image = pygame.transform.smoothscale(self.oimage,\
		(int(self.position.width*1.5),\
		int(self.position.height*1.5)))
		
		#���»�ȡ�ɴ�ͼƬ��rect����
		self.rect = self.image.get_rect()
		
		#��ÿ���·ɴ�������Ļ�ײ����룬����rect���������
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom	
		
		#�ڷɴ�������center�д洢С��ֵ
		self.center = float(self.rect.centerx)
		
	
	
		
	def blitme(self):
		"""��ָ��λ�û��Ʒɴ�"""
		self.screen.blit(self.image,self.rect)
		
	def update(self):
		"""�����ƶ���־�����ɴ���λ��"""
		
		#���·ɴ���centerֵ��������rect
		#self.rect.right���طɴ���Ӿ��ε��ұ�Ե��X���꣬self.screen_rect.right���ص�����Ļ�ұ�Ե��ֵ������1200
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left>0:
			self.center -= self.ai_settings.ship_speed_factor
		#����self.center����rect����
		self.rect.centerx = self.center
		
	def center_ship(self):
		"""�÷ɴ�����Ļ�Ͼ���"""
		self.center = self.screen_rect.centerx
