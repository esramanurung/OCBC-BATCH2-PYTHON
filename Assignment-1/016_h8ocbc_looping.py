print("\n\t================ ASSIGNMENT 1 ================")
print("\t================ Kode Peserta FSDO002ONL016 ================\n")
numbers = [
  951, 402, 984, 651, 360, 69, 408, 319, 601, 485,
  980, 507, 725, 547, 544, 615, 83, 165, 141, 501,
  263, 617, 865, 575, 219, 390, 984, 592, 236, 105,
  942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 
  823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 
  758, 219, 918, 237, 412, 566, 826, 248, 866, 950,
  626, 949
]
# Improve Code dengan menggunakan inputan
# i disini sebagai loopingan nya
i = 0
while i == 0:
    batasan = input("Enter Number Limit : ")
    for check in numbers:   # Melakukan Pengechek-an apakah number yang di input terdapat pada list atau tidak
        if batasan == str(check): 
            i = 1
            break
    else:
        print("Oops..! Sorry,The number limit entered is not on the list") 

    if i == 1: 
        for x in numbers:   
            if x % 2 == 0: 
                print(x)
            if x == int(batasan): 
                print("\n\n\t=========================== Loop Ended / Done ===========================")
                print("The end of the number loop : ", batasan)
                print("\n\n\t===========================Sekian Assignment Saya, Terimakasih!!!===========================")
                break


#Cara Kedua Seperti pada Modul Kode.id
'''
numbers = [
  951, 402, 984, 651, 360, 69, 408, 319, 601, 485,
  980, 507, 725, 547, 544, 615, 83, 165, 141, 501,
  263, 617, 865, 575, 219, 390, 984, 592, 236, 105,
  942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 
  823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 
  758, 219, 918, 237, 412, 566, 826, 248, 866, 950,
  626, 949
]
i = 0
print('Semua yang termasuk bilangan genap')

for x in numbers:
    if(x < 918):
        if (x % 2) == 0:
            print(x, end=' ')
        i = i + 1
print('Done')
'''