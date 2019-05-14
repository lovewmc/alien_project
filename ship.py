# coding=gbk
import pygame

class Ship():
	def __init__(self,ai_settings,screen):
		"""初始化飞船并设置其初始位置"""
		self.screen  = screen
		#移动标志，玩家按下方向键时标志变为True，开始移动，松开就变成False
		self.moving_right = False
		self.moving_left = False
		self.ai_settings = ai_settings
		
		#加载飞船图像并获取其外接矩形,返回的是一个表示飞船的surface
		self.image = pygame.image.load('images/ship.bmp').convert_alpha()
		self.oimage = self.image
		#获取该图片的属性rect对象
		self.rect = self.image.get_rect()
		self.position = self.coprect = self.rect    
		
		#获取屏幕的rect对象
		self.screen_rect = screen.get_rect()
		
		#设置图像大小
		self.image = pygame.transform.smoothscale(self.oimage,\
		(int(self.position.width*1.5),\
		int(self.position.height*1.5)))
		
		#重新获取飞船图片的rect对象
		self.rect = self.image.get_rect()
		
		#将每艘新飞船放在屏幕底部中央，设置rect对象的属性
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom	
		
		#在飞船的属性center中存储小数值
		self.center = float(self.rect.centerx)
		
	
	
		
	def blitme(self):
		"""在指定位置绘制飞船"""
		self.screen.blit(self.image,self.rect)
		
	def update(self):
		"""根据移动标志调整飞船的位置"""
		
		#更新飞船的center值，而不是rect
		#self.rect.right返回飞船外接矩形的右边缘的X坐标，self.screen_rect.right返回的是屏幕右边缘的值，即：1200
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left>0:
			self.center -= self.ai_settings.ship_speed_factor
		#根据self.center更新rect对象
		self.rect.centerx = self.center
		
	def center_ship(self):
		"""让飞船在屏幕上居中"""
		self.center = self.screen_rect.centerx
