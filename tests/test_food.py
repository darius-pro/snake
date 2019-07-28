from src.food import Food

def test_consumed():
    food = Food()
    food.consumed()
    assert food.location[0] < 600
    assert food.location[1] < 600