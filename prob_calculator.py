import copy
import random

class Hat:
    
		def __init__(self, **balls):
				self.contents = []
				for color, count in balls.items():
						self.contents += [color] * count
						

		def draw(self, num_balls):
				num_balls = min(num_balls, len(self.contents))
				drawn_balls = random.sample(self.contents, num_balls)
				for ball in drawn_balls:
						self.contents.remove(ball)
				return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
		successful_experiments = 0

		for _ in range(num_experiments):
				hat_copy = copy.deepcopy(hat)
				drawn_balls = hat_copy.draw(num_balls_drawn)

				#check if hte drawn balls contain at least the expected balls
				expected_found = True
				for color, count in expected_balls.items():
						if drawn_balls.count(color) < count:
								expected_found = False
								break
				if expected_found:
						successful_experiments += 1

		probability = successful_experiments / num_experiments
		return probability




hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={"black":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)
print("Probability:", probability)