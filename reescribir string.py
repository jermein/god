my_tring = "hello world"
single_quoted_string = "hello world"

#se le asignan a 2 variables formato tipo str

string_with_quotes = "hello, it's me."
another_string_with_quotes = 'he said "you are amazing!" yesterday.'

#las comillas vuelven cualquier numero o letra en tipo texto

escaped_quotes = 'He said "you are amazing!" yesterday.'


multiline = """Hello, world
my name is jose. welcome to my program."""
print(multiline)

#Cuando habro las 3 comillas todo lo que tenga abajo sera formato tipo texto hasta que lo cierre 

name = "jose"
greeting = "hello, " + name

print(greeting)

#Aqui se estahaciendo una concatenacion

age = 34
print("you are " + age)

#Sale error por que no se pueden sumar dos varibles de diferente tipo

age = 34
age_as_string = str(34)
print("you are " + age_as_string)

#para solucionar el herror del ejercisio pasado se convierte una variable int en una str para poder sumarla 
