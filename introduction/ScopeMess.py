x = "global"

def outer():
    x = "local"

    def inner():
        # only changes x in enclosing scope
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    def change_global():
        # changes x in global scope
        global x
        x = "global: changed!"

    print("outer:", x)
    inner()
    print("outer:", x)
    change_global()

print(x)
outer()
print(x)
