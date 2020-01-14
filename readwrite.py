# 1. reads name.txt into a variable my_name
with open('name.txt') as f:
    my_name = f.read()

# 2. writes a new file named hello.txt 
#    with the contents 
#    Hello, my name is <my_name>.
with open('hello.txt', 'w') as f:
    f.write('hello, my name is ' + my_name)
    f.write('\n')