from collections import Counter
from utils import fileToDict


class Knn:
    def __init__(self, nn=2):
        self.xtrain = list()
        self.ytrain = list()
        self.nn = nn

    def train(self, x: list, y: list):
        self.xtrain += x
        self.ytrain += y

    def predict(self, xpred: dict):
        neighbors = list()
        for xdict, label in zip(self.xtrain, self.ytrain):
            distance = 0
            for key in xdict.keys():
                distance += (xdict[key] - xpred[key])**2
            neighbors.append((distance, label))
        neighbors.sort()
        majority = Counter([tup[1] for tup in neighbors[:self.nn]])
        value, count = majority.most_common()[0]
        return value, count, majority


namkangs = [fileToDict(filename) for filename in list(
    map(lambda y: 'namkang-{y}'.format(y=y), range(1, 4)))]
velodys = [fileToDict(filename) for filename in list(
    map(lambda y: 'velody-{y}'.format(y=y), range(1, 4)))]

model = Knn()
model.train(namkangs[:2]+velodys[:2],
            ['namkang', 'namkang', 'velody', 'velody'])
print(model.predict(namkangs[2]))
print(model.predict(velodys[2]))
