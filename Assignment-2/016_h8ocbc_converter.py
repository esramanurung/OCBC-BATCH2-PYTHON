print("\n\t================ ASSIGNMENT 2 ================")
print("\t================ Kode Peserta FSDO002ONL016 ================\n")

def convert_kelvin_and_celcius(value: float, reverse: bool = False):
    ''' 
    convert_kelvin_and_celcius(value, reverse) mengkonversi suhu dari Kelvin ke Celcius dan Celcius ke Kelvin,
    :param value: float | integer
    :param reverse: bool | default: False 
    :return return_value: float dari nilai temperature yang di konversi
    '''
    if(reverse == True):
        # Formula Celcius to kelvin  : 0°C + 273.15 = 273.15K 
        value += 273.15
    else:
        # Formula Kelvin to celcius  : 0K − 273.15 = -273.1°C 
        value -=  273.15
    return_value = round(value, 2)
    return return_value

def convert_to_fahrenheit(value: float, unit: str):
    '''
    convert_to_fahrenheit(value, unit)adalah fungsi mengkonversi dari Fahrenheit ke Celcius atau Kelvin
    dengan memasukkan parameter di fungsi ini(convert_to_fahrenheit), fungsi  convert_kelvin_and_celcius otomatis akan mengkonversi suhunya 
    :param value: float | integer
    :param unit: str
    :assert InvalidUnit: jika nilai satuan bukan 'celcius' atau 'kelvin'
    :return return_value: float nilai yang dikonversi Celcius atau Kelvin ke Fahrenheit 
    '''
    assert unit in ['celcius', 'kelvin'], "InvalidUnit: unit value hanya menerima 'celcius' or 'kelvin'"
    # Formula Celcius to Fahrenheit : (0°C × 9/5) + 32 = 32°F
    celcius = value if unit == 'celcius' else convert_kelvin_and_celcius(value)
    return_value = round(((celcius * 9/5) + 32), 2)
    return return_value

def convert_from_fahrenheit(value: float, output: str):
    '''
    convert_from_fahrenheit(value, unit) adalah fungsi mengkonversi dari Fahrenheit ke Celcius atau Kelvin
    dengan memasukkan parameter di fungsi ini(konversi_from_fahrenheit), fungsi convert_kelvin_and_celcius otomatis akan mengkonversi suhunya 
    :param value: float | integer
    :param output: str
    :assert InvalidOutput: jika output value bukan 'celcius' or 'kelvin'
    :return return_value: float nilai yang dikonversi Fahrenheit ke Celcius atau Kelvin
    '''
    assert output in ['celcius', 'kelvin'], "InvalidOutput: unit value hanya menerima output 'celcius' or 'kelvin'"
    # Formula Fahrenheit to Celcius : (0°F − 32) × 5/9 = -17.78°C
    celcius = (value - 32) * (5/9)
    temp_value = celcius if output == 'celcius' else convert_kelvin_and_celcius(celcius, reverse = True)
    return_value = round(temp_value, 2)
    return return_value

## Perintah untuk Entri Menu yang di ingin kan
print("\n\t\t=================== Melakukan Konversi Suhu ===================")
isFinish = False
defaultValue = 50
intro = '''
Pilih menu:
1. Kelvin to Celcius
2. Celcius to Kelvin
3. Celcius to Fahrenheit
4. Kelvin to Fahrenheit
5. Fahrenheit to Celcius
6. Fahrenheit to Kelvin
7. Melakukan test untuk semua Value
8. Exit
''' 
print("\n\t\t----------------- Mau konversi apa? -----------------")
print("")
while isFinish == False:
    try:
        print(intro)
        menu = int(input("Masukkan Menu Pilihan Yang di Inginkan? : "))
        if(menu == 1): 
            temperature = float(input("Masukkan nilai suhu Kelvin yang ingin dikonversi? : ")) #Masukkan Nilai Suhu -> mis: 30 || 30.5 dst...
            print("Value dalam Celcius : {result}".format(result = convert_kelvin_and_celcius(temperature)))
        if(menu == 2): 
            temperature = float(input("Masukkan nilai suhu Celcius yang ingin dikonversi? : ")) #Masukkan Nilai Suhu -> mis: 30 || 30.5 dst...
            print("Value dalam Kelvin : {result}".format(result = convert_kelvin_and_celcius(temperature, reverse = True)))
        if(menu == 3): 
            temperature = float(input("Masukkan nilai suhu Celcius yang ingin dikonversi? : ")) #Masukkan Nilai Suhu -> mis: 30 || 30.5 dst...
            print("Value dalam Fahrenheit : {result}".format(result = convert_to_fahrenheit(temperature, 'celcius')))
        if(menu == 4): 
            temperature = float(input("Masukkan nilai suhu Kelvin yang ingin dikonversi? : ")) #Masukkan Nilai Suhu -> mis: 30 || 30.5 dst...
            print("Value dalam Fahrenheit : {result}".format(result = convert_to_fahrenheit(temperature, 'kelvin')))
        if(menu == 5): 
            temperature = float(input("Masukkan nilai suhu Fahrenheit yang ingin dikonversi? : ")) #Masukkan Nilai Suhu -> mis: 30 || 30.5 dst...
            print("Value dalam Celcius : {result}".format(result = convert_from_fahrenheit(temperature, 'celcius')))
        if(menu == 6): 
            temperature = float(input("Masukkan nilai suhu Fahrenheit yang ingin dikonversi? : ")) #Masukkan Nilai Suhu -> mis: 30 || 30.5 dst...
            print("Value dalam Kelvin : {result}".format(result = convert_from_fahrenheit(temperature, 'kelvin')))
        if(menu == 7):
            defaultValue = float(input("Masukkan nilai untuk semua testCase yang ingin di konversi: ")) #Masukkan Nilai Suhu -> mis: 30 || 30.5 dst...
            print("\n\t Menampilkan result dari semua test konversi suhu:\n")
            print(defaultValue,"K -> C = ",  convert_kelvin_and_celcius(defaultValue))
            print(defaultValue,"C -> K = ",  convert_kelvin_and_celcius(defaultValue, True))
            print(defaultValue,"C -> F = ",  convert_to_fahrenheit(defaultValue, 'celcius'))
            print(defaultValue,"K -> F = ",  convert_to_fahrenheit(defaultValue, 'kelvin'))
            print(defaultValue,"F -> C = ",  convert_from_fahrenheit(defaultValue, 'celcius'))
            print(defaultValue,"F -> K = ",  convert_from_fahrenheit(defaultValue, 'kelvin'))
        if menu == 8: isFinish = True

        input("\n\t\t Press any key to continue or exit .......!")

    except:
        print("Inputan Tidak Sesuai, Masukkan Inputan dengan Benar")
        continue
else:
    print("\n\n\t===========================Sekian Assignment Saya, Terimakasih!!!===========================")