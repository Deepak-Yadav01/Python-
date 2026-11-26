# Local: Function के अंदर बनाया गया variable.
# Global: सभी functions के बाहर बनाया गया variable.
# Nonlocal: Nested function में outer function का variable.

# Global Keyword
# अगर किसी function के अंदर Global Variable की value change करनी है, तो global keyword इस्तेमाल करते हैं।
count = 10

def update():

    global count

    count = 50

update()

print(count)



# Nonlocal Keyword
# nonlocal का इस्तेमाल Nested Functions में किया जाता है।

# जब किसी Inner Function को अपने Outer Function के variable की value modify करनी हो, तो nonlocal इस्तेमाल करते हैं।

def outer():

    count = 10

    def inner():

        nonlocal count

        count = 50

    inner()

    print(count)


outer()