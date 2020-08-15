import random

MAX = 1000000

def main():
    
    # open file
    f = open("probability", "w")
    
    # create counter for number of coins
    counter = 0
    
    # flip MAX coins and add the results to a file
    while counter < MAX:
        n = random.randint(0, 1)
        if n == 0:
            f.write("H\n")
        if n == 1:
            f.write("T\n")
        counter += 1
    
    # close file
    f.close()
    
    # open file in read mode
    d = open("probability", "r")
    
    # check the file
    check(d)


def check(z):
    # total heads
    h = 0
    
    # total tails
    t = 0
    
    # total flips
    l = 0
    
    # was the previous flip a head
    head = False
    
    # were the previous 2 flips heads
    t_head = False
    
    # 2 x heads followed by tails
    hht = 0
    
    # 2 x heads followed by heads
    hhh = 0
    
    while True:
        # read a line from the coinflip
        c = z.readline()
    
        # check if all the coins have been read
        if l == MAX:
            break

        # check if the coin is heads
        if c == "H\n":

            # check if the previous coin was heads
            if head:
                t_head = True
            
            # add 1 to hhh if the previous 2 flips were heads
            if t_head:
                hhh += 1

            # add 1 to total heads, total coins, and set heads to true
            h += 1
            l += 1
            head = True

        # check if the coin is tails
        elif c == "T\n":
            
            # add 1 to hht if the previous 2 flips were heads
            if t_head:
                hht += 1
            
            # add 1 to total tails, total coins, and set heads and t_heads to false
            t += 1
            l += 1
            head = False
            t_head = False

    # print results
    print(f"{MAX} flips")
    print(f"{round(h / l, 4)} percent heads")
    print(f"{round(t / l, 4)} percent tails")
    l = hhh + hht
    print(f"{round(hhh / l, 4)} percent of streaks of two heads that were followed by a heads")
    print(f"{round(hht / l, 4)} percent of streaks of two heads that were followed by a tails")


main()
