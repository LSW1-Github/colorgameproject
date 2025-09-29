
clrs = [
    'red',      #0
    'orange',   #1
    'yellow',   #2
    'green',    #3
    'blue',     #4
    'purple',   #5
    'brown',    #6
    'black',    #7
    'white',    #8
    ]


wet = [
    0, 0, 0, 0, 0, 0, 0, 9, 1]

cvs = [
    0, #red
    0, #orange
    0, #yellow
    0, #green
    0, #blue
    0, #purple
    0, #brown
    0, #black
    0, #white
    ]



def replace_number(old, new):
    global numbers
    numbers = [new if num == old else num for num in numbers]