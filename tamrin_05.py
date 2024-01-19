s = 0
st = ""
count = 0
n = "tamrin_05fTable.txt"
file = open(n,"r")
x = file.readlines()
for i in x:
    for j in i:
        if(ord(j) >= 48 and ord(j) <= 57):
            st += j
        else:
            if(st):
                s += int(st)
                count += 1
                st = ""
if(st):
    s += int(st)
    count += 1
    st = ""
file.close()
print(f"count   : {count}")
print(f"sum     : {s}")
if(count):
    print(f"average : {s / count}")