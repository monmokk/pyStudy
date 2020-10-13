# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press ⌘F8 to toggle the breakpoint.
    if 4 in [1,2,3,4]: print("4 here")
    languages = ['python', 'perl', 'c', 'java']
    for lang in languages:
        if lang in ['python', 'perl']:
            print("%6s need interpreter" % lang)
        elif lang in ['c', 'java']:
            print("%6s need compiler" % lang)
        else:
            print ("should not reach here")
    a = 2
    b = 3
    print (a**b)
    food = "Python's favorite food is perl"
    print (food)
    a = [1,2,3,4,['a','b','c']]
    print(a[-1])
    print (a[:2])
    print (a[4][:2])
    print (len(a))
    del a[2]
    a.append(3)
    print (a)
    a.reverse()
    print (a)
    a.sort()
    print (a)
    print(a.index(2))
    # 리스트는 값의 생성, 삭제, 수정이 가능
    # 튜플은 불가능





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
