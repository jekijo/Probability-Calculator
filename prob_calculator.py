import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        self.k = kwargs
        for i,j in self.k.items():
            for num in range(j):
                self.contents.append(str(i))
                
    def draw(self, num):
        new_contents = []
        if num >= len(self.contents)+1:
            return self.contents
        else:
            for i in range(num):
                r_ind = random.randrange(0,len(self.contents)-1)
                new_contents.append(self.contents[r_ind])
                del self.contents[r_ind]
                
            return new_contents
                

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0
    for i in range(num_experiments):
        d = {}
        balls = copy.deepcopy(hat)
        l = balls.draw(num_balls_drawn)
        for i in l:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for i,j in expected_balls.items():
            check = True
            try:
                if expected_balls[i] < d[i]:
                    check = False
            except:
                pass
        if check == True:
            m += 1
    p = m/num_experiments
    return p 
