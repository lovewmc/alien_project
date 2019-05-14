import pygame.font

class Scoreboard():
	"""显示得分信息的类"""
	
	def __init__(self,ai_settings,screen,stats):
		"""初始化显示得分涉及的属性"""
		self.screen = screen
		self.screen_rect  = screen.get_rect()
		self.ai_settings = ai_settings
		self.stats = stats
		
		#显示得分信息时使用的字体设置
		self.text_color = (30,30,30)
		self.font = pygame.font.SysFont(None,48)
		
		#准备初始得分图像，将要显示的文本转换为图像
		self.prep_score()
		
	def prep_score(self):
		"""将得分转换为一幅渲染的图像"""
		rounded_score = int(round(self.stats.score,-1))
		score_str = "{:,}".format(rounded_score)
		#将数字值stats.score转换为字符串
		score_str = str(self.stats.score)
		#将字符串传给创建图像的render（）
		self.score_image = self.font.render(score_str,True,self.text_color,self.ai_settings.bg_color)
	
		#创建一个名为score_rect的rect，让其右边缘与屏幕右边缘相距20像素，上边缘与屏幕上边缘相距20像素
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20
	
	def show_score(self):
		"""在屏幕上显示渲染好的得分图像文本"""
		self.screen.blit(self.score_image,self.score_rect)
