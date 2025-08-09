x = 10
def function():
    global x # used when you want to refer to a global variable inisde a function
    x = 20
function()
print(x)