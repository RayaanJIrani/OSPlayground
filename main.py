import os
from datetime import datetime

def main():
    os.chdir('/Users/rayaanirani/Desktop/OSPlayground')
    cpp_list = []
    for file in os.listdir():
        if os.path.splitext(file)[1] == '.cpp':
            cpp_list.append(file)

    for file in cpp_list:
        os.system('g++ -std=c++11' + ' ' + file)
        os.system('./a.out')
        os.system('rm a.out')

if __name__ == '__main__':
    main()

