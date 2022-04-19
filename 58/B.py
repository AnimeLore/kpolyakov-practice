from itertools import product as combinations

count = 0
k = 3
a = list(combinations("ЫШЧО", repeat=k))

def tw(a):
    o = True
    global count
    for i in a:
        for k in range(1,len(i)):
            if i[k-1]==i[k]:
                o=False
                break
        if not o:
            o=True
            count += 1
            print("".join(i))
            continue


tw(a)
print(count)
