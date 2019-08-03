from src.spider import *

def test_spider_init():
        spider = Spider(6)
        assert spider.alive == False
        assert spider.time == 0
        assert spider.just_consumed == 0
        assert spider.last_score == 0
        assert spider.difficulty == 6

def test_score():
    spider = Spider(6)
    spider.time = 100
    assert spider.score() == 60

def test_spider_reset():
    spider = Spider(6)
    spider.reset()
    assert spider.alive == False
    assert spider.just_consumed == 0
    assert spider.time == 0
    assert spider.last_score == 0

def test_consumed():
    spider = Spider(6)
    spider.consumed()
    assert spider.alive == False
    assert spider.time == 0
    assert spider.just_consumed == 3