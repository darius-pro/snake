from src.hud import hud

def test_set_score():
    HUD = hud()
    HUD.add_score(8)
    assert HUD.score == 8
    HUD.add_score(12)
    assert HUD.score == 20

def test_reset_score():
    HUD = hud()
    HUD.score = 10
    HUD.reset_score()
    assert HUD.score == 0