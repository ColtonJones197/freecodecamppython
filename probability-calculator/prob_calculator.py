import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **arguments) -> None:
    self.contents: list = []
    for color in arguments:
      #important to note that if the user specifies the same color twice
      # that they will not get the expected result
      amt_color = arguments[color]
      for i in range(0, amt_color):
        self.contents.append(color)

  def draw(self, num_balls: int):
    balls_drawn = []
    for i in range(0, num_balls):
      if len(self.contents) == 0:
        return balls_drawn
      random_ball_location = random.randrange(len(self.contents))
      balls_drawn.append(self.contents.pop(random_ball_location))
    return balls_drawn
    

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  successes = 0
  for i in range(0, num_experiments):
    trial = copy.deepcopy(hat)
    sample = trial.draw(num_balls_drawn)
    is_success = True
    for color in expected_balls:
      num_expected = expected_balls[color]
      if sample.count(color) < num_expected:
        is_success = False
    successes += 1 if is_success else 0

  return successes / num_experiments