import json

class GameStats():
    #跟踪游戏信息状态

    def __init__(self,ai_settings):
        #初始化
        self.ai_settings=ai_settings
        self.level=0
        self.highest_score=0
        self.reset_stats()

        filename='record.json'
        with open(filename) as f_obj:
            get_record=json.load(f_obj)
            self.highest_score=int(get_record)
            print("get success!")

        self.game_status=False


    def reset_stats(self):
        #init飞船生命值
        self.ships_left=self.ai_settings.ship_limit
        self.ai_settings.initialize_dynamic_setting()
        self.score=0
        print("初始化成功")
