def digita_root(a):
    while a>=10:
        a=sum(int(digit) for digit in str(a))
        return a
print(digita_root(87))
print(digita_root(100))