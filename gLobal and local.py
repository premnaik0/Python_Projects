#gLobal and local
x="Night"
def fun():
    global x
    x="Morning"
    print(x)
fun()
print(x)