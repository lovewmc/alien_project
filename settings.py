class Settings():
	""" 存储《外星人入侵》的所有设置的类"""
	
	def __init__(self):
		""" 初始化游戏的外观和飞船的速度 """
		#屏幕设置   //为什么这么设置
		#创建一个名为screen的显示窗口,实参(1200,800)是一个元组，指定了游戏窗口的尺寸
		self.screen_width = 1200
		self.screen_height = 660
		#设置背景色，颜色是以RGB值指定的
		self.bg_color = (230,230,230)	
		#self.bg_color = (0,0,0)
		#飞船的速度设置
		self.ship_speed_factor = 2
		#一个玩家所拥有的飞船数量
		self.ship_limit = 3
		
		#存储新类Bullet所需要的值
		#子弹设置
		self.bullet_speed_factor = 3
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 250,0,0
		#将屏幕中的子弹数限制为3个
		self.bullets_allowed = 5
		
		#外星人速度设置
		self.alien_speed_factor = 1
		#代表外星人群向下移动的速度
		self.fleet_drop_speed = 10
		#等于1代表向右移，等于-1代表向左移
		self.fleet_direction = 1
		
		#以什么样的速度加快游戏节奏
		self.speedup_scale = 1.1
		#调用该函数，以初始化随游戏进行而变化的属性
		self.initialize_dynamic_settings()
		
	def initialize_dynamic_settings(self):
		"""初始化随游戏进行而变化的设置"""
		self.ship_speed_factor = 1.5
		self.bullrt_speed_factor = 3
		self.alien_speed_factor = 1
		
		#每个外星人的分数
		self.alien_points = 50
		#外星人得分的提高速度
		self.score_scale = 1.5
		
		#fleet_direction为1表示向右：为-1表示向左
		self.fleet_direction = 1
	def increase_speed(self):
		"""每提高一个等级，提高速度设置，增大外星人的分值"""
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
		#提高每个外星人的分值
		self.alien_points = int(self.alien_points * self.score_scale)
		print(self.alien_points)
