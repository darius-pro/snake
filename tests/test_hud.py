from src.hud import hud

def test_set_score():
    HUD = hud()
    HUD.set_score(8)
    assert HUD.score == 8