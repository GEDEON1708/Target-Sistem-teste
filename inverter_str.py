def inverter_string(string):
    string_invertida = ""
    for char in string:
        string_invertida = char + string_invertida
    return string_invertida

# Teste
string = input("Informe uma string para inverter: ")
print("String invertida:", inverter_string(string))
