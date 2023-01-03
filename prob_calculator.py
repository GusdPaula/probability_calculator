import copy
import random
# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        # creating a list without numbers, only with words
        for k, v in kwargs.items():
            self.contents += [k] * v

    def draw(self, num):
        try:
            # randomly select numm of balls
            balls = random.sample(self.contents, num)
        except:
            balls = copy.deepcopy(self.contents)

        # remove balls from contents
        for ball in balls:
            self.contents.remove(ball)
        
        # return selected balls
        return balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0
    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        balls = hat_copy.draw(num_balls_drawn)
       
        # check if balls match expectation
        eb_list = []
        for k, v in expected_balls.items():
            eb_list += [k] * v

        if contains_ball(eb_list, balls):
            M += 1
        
    probability = M / num_experiments
    return probability

def contains_ball(expected_balls, actual_balls):
    for b in expected_balls:
        if b in actual_balls:
            actual_balls.remove(b)
        else:
            return False
    return True
    