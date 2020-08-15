import csv, random

MAX = 1000000

def main():
    # open file
    f = open("probability", "w")
    counter = 0
    # flip MAX coins and add them to a file
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
    # heads followed by tails
    hht = 0
    # heads followed by heads
    hhh = 0
    while True:
        # read a line from the coinflip
        c = z.readline()
        if l == MAX:
            break
        if c == "H\n":
            if head:
                t_head = True
            if t_head:
                hhh += 1
            h += 1
            l += 1
            head = True
        elif c == "T\n":
            if t_head:
                hht += 1
            t += 1
            l += 1
            head = False
            t_head = False
    print(f"{MAX} flips")
    print(f"{round(h / l, 4)} percent heads")
    print(f"{round(t / l, 4)} percent tails")
    l = hhh + hht
    print(f"{round(hhh / l, 4)} percent of streaks of two heads that were followed by a heads")
    print(f"{round(hht / l, 4)} percent of streaks of two heads that were followed by a tails")


main()
