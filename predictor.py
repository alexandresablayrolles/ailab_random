import torch
from torch.autograd import Variable

class Predictor:

    def __init__(self):
        pass

    def __call__(self, data):
        return Variable(torch.randn((data.size(0), 27)))
