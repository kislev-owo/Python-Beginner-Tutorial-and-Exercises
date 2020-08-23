def number_of_bottles():
    for num in range(99,1,-1):
        print(f'''{num} bottles of milk on the wall, {num} bottles of milk.
Take one down and pass it around, {num-1} bottles of milk on the wall.''' )

    print('''1 bottle of milk on the wall, 1 bottle of milk.
Take one down and pass it around, no more bottles of milk on the wall.

No more bottles of milk on the wall, no more bottles of milk.
Go to the store and buy some more, 99 bottles of milk on the wall''') 

number_of_bottles()