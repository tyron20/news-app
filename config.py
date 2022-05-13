import os

from instance.config import NEWS_API_KEY

class Config:

    NEWS_API_BASE_URL ='htpps://newsapi.org/v2/top-headlines?country=us&apiKey=9f000abf58ce49378250554b38233cf3'
    NEWS_API_KEY = os.environ.get('9f000abf58ce49378250554b38233cf3')



class ProdConfig(Config):
    pass





class DevConfig(Config):
    DEBUG = True

config_option = {
    "development":DevConfig,
    "production":ProdConfig
}