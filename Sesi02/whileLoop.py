# Python "while" Loops
n = 5
while n > 0 :
    n -= 1      # decrement n = n -1
    print(n)
print('====')

i = 1
while i < 6 :
    print(i)
    i += 1
print('====')

# The Python break and continue Statements
# Make Break
i = 0

while i < 5 :
    j = 0
    
    while j < 3 :
        print(i, j)

        if(j ==2) : 
            break

        print('----')

        j += 1
    i += 1

n = 5
while n > 0:
    n -= 1
    if n == 2:
        break # Break Statement
    print(n)
print('Loop ended.')

# Continue
i = 0

while i < 5 :
    j = 0
    
    while j < 3 :
        print(i, j)

        j += 1

        if(j ==2) : 
            continue

        print('----')

    i += 1


# Nested while loop
n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
print('Loop ended.')

# The else Clause  -> additional statement
n = 5
while n > 0:
    n -= 1
    print(n)
else:
    print('Loop done.')

a = ['foo', 'bar']
while len(a):
    print(a.pop(0))     # pop --> hapus elemen dri list
    
    b = ['baz', 'qux']
    
    while len(b):
        print('>', b.pop(0))

# For-Loop

books = ['book a', 'book b', 'book c']

for book in books: 
    print(book)

# One Line While loop
n = 5
while n > 0: 
    n -= 1; 
    print(n)

# Iterate With Range
# x = range(5) --> [1, 2, 3, 4]
# x  = range(2, 9) --> 2 s/d angka sebelum 9
# x = range(0, 20, 100) --> mulai dri angka 0, incremnt 20, brhenti sblum angka 100

x = range(0, 10)
for n in x:    
    print(n)

# Iterate Dictionary

a = ['foo', 'bar', 'baz']
for i in a:
    print(i)

d = {'foo': 1, 'bar': 2, 'baz': 3}
for k in d:
    print(k)

print('this is dictionary key')

for k in d:
    print(d[k])

print('this is dictionary value')
for k in d.values():
    print(k)

for k, v in d.items(): 
    print(k, ":", v) 

# The range() Function
for n in (0, 1, 2, 3, 4):
    print(n)

# The break and continue Statements
for i in ['foo', 'bar', 'baz', 'qux']:
    if 'b' in i:
        break
    print(i)

# make continue
for i in ['foo', 'bar', 'baz', 'qux']:
    if 'b' in i:
        continue
    print(i)

# The else Clause
for i in ['foo', 'bar', 'baz', 'qux']:
    print(i)
else:
    print('Done.')  # Will execut3

for i in ['foo', 'bar', 'baz', 'qux']:
  if i == 'bar':
    break
  print(i)
else:
  print('Done.') 