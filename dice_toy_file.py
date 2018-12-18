import random
import re

def input_taker(entry):
    #Prompts the user to input how many times to roll
    # https://stackoverflow.com/questions/19970532/how-to-check-a-string-for-a-special-character
    # https://stackoverflow.com/questions/4666973/how-to-extract-the-substring-between-two-markers
    dice = entry
    dice = dice.replace("+"," plus ")
    dice = dice.replace("-", " minus ")
    dicelist = re.sub("[^\w]", " ",  dice).split()

    dice_coords = [ ] #this shows where the dice belong in the original dicelist
    space = " "
    a = 1
    b = 0
    letters = set("d")
    while a <= len(dicelist):
        a += 1
        for w in dicelist:
            if letters & set(w):
                dice_location = dicelist.index(w)
                #print(w + " "+ str(dice_location))
                dicelist[dice_location] = space
                dice_coords.append(w)
                dice_coords.append(dice_location)
                b += 1
                #print(dice_coords)

    the_dice_var = dice_coords[0::2]
    the_location_var = dice_coords[1::2]

    quantity_1 = 0
    dice_post_while = [ ]
    while quantity_1 < len(the_dice_var):
        the_dice_var_while = the_dice_var[quantity_1].split("d")
        quantity_1 += 1
        dice_post_while.append(the_dice_var_while)
    #print(dice_post_while)

    quantity_2 = 0
    times_to_roll = [ ]
    dice_type = [ ]
    while quantity_2 < len(dice_post_while):
        times_to_roll_while = dice_post_while[quantity_2][0]
        dice_type_while = dice_post_while[quantity_2][1]
        quantity_2 += 1
        times_to_roll.append(times_to_roll_while)
        dice_type.append(dice_type_while)

    roll_entry = 0
    master_dice_numbers = []
    j = 1
    a = len(times_to_roll)
    while j <= a:
        j += 1
        x = 1
        dice_numbers = []
        master_dice_numbers.append(dice_numbers)
        t = times_to_roll[roll_entry]
        d = dice_type[roll_entry]
        roll_entry += 1

        while x <= int(t):
                roll = random.randint(1, int((d)))
                dice_total = 0
                dice_total += roll
                x += 1
                dice_numbers.append(dice_total)
        #print(dice_numbers)

    x = 1
    e = 0
    d = 0
    while x <= len(the_location_var):
        c = int(the_location_var[e])
        b = (master_dice_numbers[d])
        dicelist[c] = b  # insert location, then thing you want to insert
        x += 1
        e += 1
        d += 1

    x = 1
    a = 0
    while x <= len(the_location_var):
        Q = the_location_var[a]
        dice_string = "+".join(str(e) for e in (dicelist[Q]))  # - to turn a list into a string
        dicelist[Q] = ("("+dice_string+")")
        x += 1
        a += 1
    #print(dicelist)

    dicelist = "".join(dicelist)

    sum_of_dice = dicelist.replace("plus", "+")
    sum_of_dice = sum_of_dice.replace("minus", "-")
    print(sum_of_dice)
    dicelist = eval(sum_of_dice)
    print(dicelist)

input_taker(input("What dice? "))