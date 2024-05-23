import os
import re

def read_log(_path_):
    with open(_path_, 'r') as f:
        data = f.readlines()
    return data

if __name__ == '__main__':
    path = './jobs/cifar10__approach-CoreSet/Init1000_S10000_B1000/Seed-0/accuracy.log'
    data = read_log(path)
    data = [re.findall("\d+.\d+", d)[-1] for d in data if 'Cycle' in d]
    print(','.join(data))