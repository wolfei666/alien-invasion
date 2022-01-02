class Settings():

    def __init__(self):
        #初始化屏幕
        self.screen_width=1200
        self.screen_height=800
        self.bg_color = (153,217,234)
        #初始化飞船移动的速度
        
        self.ship_limit = 3

        #初始化子弹
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 3

        
        self.fleet_drop_speed = 10
        

        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()
    def initialize_dynamic_settings(self):
        self.ship_speed_factor=2
        self.bullet_speed_factor = 3
        self.alien_speed_factor=2
        self.alien_points = 50

        #1右移-1左移
        self.fleet_direction=1
    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)

        
