#_Function_Create_#
# Membuat Function baru dengan nama belajar_python
def belajar_python():
    print("Halo")

# Memanggil Function "say_hello"
belajar_python() # Halo


#_Function_Argument_1_#
# Membuat Function dengan nama belajar_python yang memiliki satu Arguments "name"
def belajar_python(name):
    print("Halo, Saya %s" % name)

# Memanggil Function belajar_python dengan Arguments "name" berupa string dengan value "Rizqi"
belajar_python("Rizqi") # Halo, Saya Rizqi


#_Function_Argument_2_#
# Membuat Function dengan nama belajar_python yang memiliki dua Arguments: "name" dan "age"
def belajar_python(name, age):
    print("Halo, Saya %s. Umur saya %d" % (name, age))

# Memanggil Function belajar_python 
# dengan Arguments "name" berupa string dengan value "Rizqi"
# dan Arguments "age" berupa integer dengan value "30"
belajar_python("Rizqi", 30) # Halo, Saya Rizqi


