import json
import scipy.signal as signal
import numpy as np


index = []
for i in range(100):
    index.append(1 + i*30)

x_motion = []
y_motion = []
for i in range(2, 299):
    filename = 'D:/camera/mv442/%d.json' %(i)
    if i in index:
        filename = 'D:/camera/mv442/%d.json' % (i-1)
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
        # <class 'dict'>,JSON文件读入到内存以后，就是一个Python中的字典。
        # 字典是支持嵌套的，
        # print(type(data))

    x_frame = []
    y_frame = []
    for j in range(len(data)):
        x_frame.append(data[j]['dx'])
        y_frame.append(data[j]['dy'])

    signal.medfilt(x_frame, 21)
    signal.medfilt(y_frame, 21)
    x_motion.append(np.mean(x_frame))
    y_motion.append(np.mean(y_frame))
    print(i)


print(np.cumsum(x_motion))
