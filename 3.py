import sys

import numpy as np
import matplotlib.pyplot as plt


# 数学の教科書の内容
# https://www.amazon.co.jp/Pythonで動かして学ぶ-あたらしい数学の教科書-機械学習・深層学習に必要な基礎知識-AI-TECHNOLOGY/dp/4798161179
class Book(object):

    def __init__(self):
        self.num = sys.argv[1] if len(sys.argv) > 1 else 0
        self.arg1 = sys.argv[2] if len(sys.argv) > 2 else 0
        self.arg2 = sys.argv[3] if len(sys.argv) > 3 else 0
        self.method_name = ''

    @staticmethod
    def plot(x, y):
        plt.plot(x, y)
        plt.xlabel("x", size=14)
        plt.xlabel("y", size=14)
        plt.grid()
        plt.show()

    @staticmethod
    # 関数
    def learn_1(*args):
        a = 1.5
        x = np.linspace(-1, 1)
        y = a * x
        Book.plot(x, y)

    @staticmethod
    # 関数
    def learn_2(*args):
        a = int(args[0])
        x = np.linspace(-1, 1)
        y = a * x
        Book.plot(x, y)

    @staticmethod
    # べき乗
    def learn_3(*args):
        x = np.linspace(-1, 1)
        y = 3 * x + 2
        Book.plot(x, y)

    @staticmethod
    # 平方根
    def learn_4(*args):
        a = int(args[0])
        x = np.linspace(0, 10)
        y = np.sqrt(x) + a
        Book.plot(x, y)

    def func_not_found(self):
        print('No Function ' + str(self.num) + ' Found!')

    def exec(self):
        self.method_name = "learn_{0}".format(str(self.num))
        print(self.method_name)
        func = getattr(self, self.method_name, self.func_not_found)
        func(self.arg1, self.arg2)


if __name__ == '__main__':
    book = Book()
    book.exec()
