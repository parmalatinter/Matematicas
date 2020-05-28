import inspect
import sys

import matplotlib
import numpy as np
import matplotlib.pyplot as plt

# matplotlib.use('Agg')


# 数学の教科書の内容
# https://www.amazon.co.jp/Pythonで動かして学ぶ-あたらしい数学の教科書-機械学習・深層学習に必要な基礎知識-AI-TECHNOLOGY/dp/4798161179
class Book(object):

    def __init__(self):
        self.num = sys.argv[1] if len(sys.argv) > 1 else 0
        self.arg1 = sys.argv[2] if len(sys.argv) > 2 else 0
        self.arg2 = sys.argv[3] if len(sys.argv) > 3 else 0
        self.method_name = ''

    @staticmethod
    def plot(x, y, file_name):
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        plt.plot(x, y, marker='o', label='Result')
        plt.legend()

        plt.xlabel("x", size=14)
        plt.xlabel("y", size=14)
        ax.legend(loc='best')
        ax.legend(loc='best')
        ax.set_title(file_name)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        plt.savefig("images/{0}.png".format(file_name))

        plt.grid()
        plt.show()

    @staticmethod
    # 関数
    def learn_1(*args):
        a = 1.5
        x = np.linspace(-1, 1)
        y = a * x

        file_name = inspect.currentframe().f_code.co_name
        Book.plot(x, y, file_name)

    @staticmethod
    # 関数
    def learn_2(*args):
        a = int(args[0])
        x = np.linspace(-1, 1)
        y = a * x

        file_name = inspect.currentframe().f_code.co_name
        Book.plot(x, y, file_name)

    @staticmethod
    # べき乗
    def learn_3(*args):
        x = np.linspace(-1, 1)
        y = 3 * x + 2

        file_name = inspect.currentframe().f_code.co_name
        Book.plot(x, y, file_name)

    @staticmethod
    # 平方根
    def learn_4(*args):
        a = int(args[0])
        x = np.linspace(0, 10)
        y = np.sqrt(x) + a

        file_name = inspect.currentframe().f_code.co_name
        Book.plot(x, y, file_name)

    def func_not_found(self, *args):
        print('No Function ' + "learn_{0}".format(str(self.num)) + ' Found!')

    def exec(self):
        self.method_name = "learn_{0}".format(str(self.num))
        print(self.method_name)
        func = getattr(self, self.method_name, self.func_not_found)
        func(self.arg1, self.arg2)


if __name__ == '__main__':
    book = Book()
    book.exec()
