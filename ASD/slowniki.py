# Tworzenie słownika
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Dodawanie i modyfikowanie elementów
my_dict['email'] = 'alice@example.com'
my_dict['age'] = 26

# Dostęp do wartości
print(my_dict['name'])  # Output: Alice

# Usuwanie elementów
del my_dict['city']
email = my_dict.pop('email', 'brak email')

# Iteracja przez słownik
for key, value in my_dict.items():
    print(key, value)

# Sprawdzanie istnienia klucza
if 'age' in my_dict:
    print('age istnieje w słowniku')

# Kopiowanie słownika
copy_dict = my_dict.copy()

# Metody słowników
keys = my_dict.keys()
values = my_dict.values()
items = my_dict.items()

print(keys)    # Output: dict_keys(['name', 'age'])
print(values)  # Output: dict_values(['Alice', 26])
print(items)   # Output: dict_items([('name', 'Alice'), ('age', 26)])