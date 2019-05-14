"""创建一个空的pygame窗口"""
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_status import GameStats
from botton import Button
from scoreboard import Scoreboard

def run_game():
	pygame.init()
	#实例化一个Settings对象，对象名为ai_settings
	ai_settings = Settings()
	#set_mode()返回的surface表示整个游戏窗口
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion ding")	
	#创建一艘飞船
	ship = Ship(ai_settings,screen)
	#创建一个用于存储子弹的编组
	bullets = Group()
	#创建一个外星人编组
	aliens = Group()
	#创建外星人群
	gf.create_fleet(ai_settings,screen,ship,aliens)
	#创建一个用于统计游戏信息的实例
	stats = GameStats(ai_settings)
	#创建积分牌
	sb = Scoreboard(ai_settings,screen,stats)
	#创建play按钮
	play_button = Button(ai_settings,screen,"play")
	
    #开始游戏的主循环，
	while True:
		#监视键盘和鼠标事件
		gf.check_events(ai_settings,screen,stats,play_button,ship,aliens,bullets)
		if stats.game_active:
			#更新飞船的位置
			ship.update()
			#更新子弹的位置，并删除已消失的子弹
			gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
			gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)
		#更新屏幕上的图像，并切换到新屏幕
		gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)

run_game()


                
	
