a = [1, 2, 3, 4]
print(a)

b = [
    1,
    2,
    3,
    4,
    5
]
print(b)

c = (
    1,
    2,
    3,
    4
)
print(c)

d = {
    'k1': 1,
    'k2': 2,
    'k3': 3
}
print(d)

def func(
    a,
    b,
    c
):
    print(a, b, c)

func(1,2,3)

a = 10
b = 20
c = 30

if a > 5 and b > 10 and c > 20:
    print('yes')

if a > 5 \
    and b > 10 \
    and c > 20:
    print('yes')

txt = '''this is a string'''
print(txt)

txt = '''
    this
    is a string'''
print(txt)