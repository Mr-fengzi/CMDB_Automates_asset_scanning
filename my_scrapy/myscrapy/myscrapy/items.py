# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class DouBanMovieItem(scrapy.Item):
    """
    确定要爬取的数据的类型和名称，包含:
        电影名称( title) ;
        电影评分( score) ;
        电影评语( quote) ;
        电影导演( director) ，
        上映日期(release_date)
        评论数(comment_num)
    通过 Field( ) 方法来声明数据字段。
    """
    title = scrapy.Field()  # 电影名称
    score = scrapy.Field()  # 电影评分
    quote = scrapy.Field()  # 电影评语
    director = scrapy.Field()  # 电影导演
    release_date = scrapy.Field()  # 上映日期
    comment_num = scrapy.Field()  # 评论数
    image_url = scrapy.Field()  # 图片的url地址
    detail_url = scrapy.Field()  # 电影详情页信息;
    image_path = scrapy.Field()  # 下載的封面本地存儲位置