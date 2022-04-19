from itertools import product as combinations

count = 0
k = 3
a = list(combinations("ЫШЧО", repeat=k))
def tw(a):
    global count
    for i in a:
        if i[1].lower() == "ы":
            count += 1
            print("".join(i))
            continue


tw(a)
print(count)
