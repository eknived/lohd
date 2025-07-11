# write a program to greet all the persons name listed whihc started with a


n = ["niv","ek","appu","dev","akku"]  #Avoid using list as a variable name
#list is a built-in type in Python, and overwriting it can cause bugs or confusion

for name in n:
    if name.startswith("a"):
        print(f"hello {name}")


    if name[0] == 'a':
        print(f"hello {name}")
