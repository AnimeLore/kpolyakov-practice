from itertools import product as combinations

count = 0
k = 3
a = list(combinations("ЫШЧО", repeat=k))

def tw(a):
    global count
    for i in a:
        if len(set(i)) != len(i):
            count += 1
            print("".join(i))
            continue


tw(a)
print(count)
