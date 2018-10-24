from sys import argv
def liida(arg1, arg2):
    print(arg1+arg2)

script, a, b = argv
a = int(a)
b = int(b)

liida(a, b)