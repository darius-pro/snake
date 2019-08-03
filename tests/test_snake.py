from src.snake import location_start, Snake

DIRECTIONS = ["left", "right", "up", "down"]

def test_location_start():
    assert location_start() == [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

def test_right():
    mapping = {
              "right" : "right",
              "left" : "left",
              "up" : "right",
              "down" : "right"
              }
    for key in DIRECTIONS:
      snake = Snake()
      snake.direction = key
      snake.right()
      assert snake.direction == mapping[key]


def test_left():
    mapping = {
              "right" : "right",
              "left" : "left",
              "up" : "left",
              "down" : "left"
              }
    for key in DIRECTIONS:
      snake = Snake()
      snake.direction = key
      snake.left()
      assert snake.direction == mapping[key]

def test_down():
    mapping = {
              "right" : "down",
              "left" : "down",
              "up" : "up",
              "down" : "down"
              }
    for key in DIRECTIONS:
      snake = Snake()
      snake.direction = key
      snake.down()
      assert snake.direction == mapping[key]

def test_up():
    mapping = {
              "right" : "up",
              "left" : "up",
              "up" : "up",
              "down" : "down"
              }
    for key in DIRECTIONS:
      snake = Snake()
      snake.direction = key
      snake.up()
      assert snake.direction == mapping[key]

def test_simulate():
    snake = Snake()
    snake.simulate()
    assert type(snake.head_location[0]) is int
    assert type(snake.head_location[1]) is int
    for i, val1 in enumerate(snake.snake_matrix):
      for j, val2 in enumerate(snake.snake_matrix[i]):
        assert type(snake.snake_matrix[i][j]) is int

def test_eat():
    snake = Snake()
    before = snake.length
    snake.eat()
    assert before == snake.length - 1
