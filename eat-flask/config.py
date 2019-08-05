# -*- coding=utf-8 -*-
class Config:
    SECRET_KEY = 'mrsoft'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # 小程序配置信息
    AppID = 'wxa19a5fe3f2b83a96'
    AppSecret = '5dbf486ee2a9e9a4daad5245852b7e54'
    # 聚合数据菜谱api
    CookAppKey = '48721c8833c964c86d484b3927230bfb'

    @staticmethod
    def init_app(app):
        pass


# the config for development
class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Chengyu0402_@111.231.56.173:3306/eatFlask'
    DEBUG = True


# define the config
config = {
    'default': DevelopmentConfig
}
