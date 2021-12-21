'''
f = open("test.txt")
f = open("test.txt", 'w') # write -> menulis dan menimpa (replace) existing teksnya
f = open("test.txt", 'a') # append -> menulis tapi di paling akhir (setelah EOF, end of Line) // append = menambahkan
f = open("test.txt", 'r') # read --> membaca
'''
print('file')

file = open('Hack8_Sample_Text.txt')

try:
   f = open("Hack8_Sample_Text.txt", encoding = 'utf-8')
   # perform file operations
finally:
   f.close()

#tambahan
f = open("Hack8_Sample_Text.txt")
   # perform file operations
print(f.read(4), "\n--\n")
print(f.read(6),"\n--\n")
print(f.tell())

print(f.read(12),"\n--\n")
f.seek(0)
print(f.tell())

#print(f.read(),"\n--\n")
f.close()

f = open("Hack8_Sample_Text.txt")
f.seek(0)   # bring file cursor to initial position
for line in f: # line disini gak harus line penamaan nya bisa saja i, x dst..
  print(line, end = '')

##Tambahan
f = open("Hack8_Sample_Text.txt")
f.seek(0)   
print(f.readline())



##Tambahan
f = open("Hack8_Sample_Text.txt") 
print(f.readline())
our_rows = f.readline()
print(our_rows[6])

# should be leaser
'''
x = 10
if x > 5:
    raise Exception('x should not exceed 5. The value of x was: {}'.format(x))
'''
# should be greater
x = 10
if x < 5:
    raise Exception('x should not exceed 5. The value of x was: {}'.format(x))


'''
x = 22
#assert x == 20
assert x == 20, "x harus 20"
'''

'''
# Tambahan
def perkalian_dengan_0(num1):
   return 0 * num1 + 1

a = 0

# sepuluh_kali_0 = perkalian_dengan_0(10)
sepuluh_kali_0 = perkalian_dengan_0(10)
assert sepuluh_kali_0 == 0, "fungsi masih salah"
'''
