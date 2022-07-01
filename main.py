def CheckID(ID):
    if (len(ID) != 9):
        return False

    IdList = list()

    try:
        id = list(map(int, ID))
    except:
        return False

    counter = 0

    for i in range(9):
        id[i] *= (i % 2) + 1
        if (id[i] > 9):
            id[i] -= 9
        counter += id[i]

    if (counter % 10 == 0):
        return True
    else:
        return False
file = open(input("enter file link here\n"), "r", encoding="utf8")
ctovet = open("ctovet.txt", "w", encoding="utf8")
city = open("city.txt", "w", encoding="utf8")
isvote = open("isvote.txt", "w", encoding="utf8")
id = open("id.txt", "w", encoding="utf8")
name = open("name.txt", "w", encoding="utf8")
all = open("all.txt", "w", encoding="utf8")
family_name = open("familyname.txt", "w", encoding="utf8")
print("'o','First Name','Last Name','Tehudat Zhut','Phone','Address','s','t','Voted','City ID'")
x = file.read()
x = x.split("\n")
maybetz = ""
ctovet1 = ""
for i in range(len(x) - 1):
    y = (x[i].split(","))
    isvote.write(str("0" in y[-1]).replace("'", "") + "\n")
    name.write(str(y[1]).replace("'", "") + "\n")
    family_name.write(str(y[2]).replace("'", "") + "\n")
    city.write(str(y[6].replace("'", "") + "\n"))
    if str(y[5].replace("'", ""))=="":
        pass
    else:
        ctovet1=str(y[5].replace("'", ""))
        ctovet.write(str(y[5].replace("'", "") + "\n"))

    for i in range(len(y)):
        if CheckID(y[i].replace("'", "")):
            maybetz = y[i].replace("'", "")
    id.write(maybetz + "\n")
    all.write(str(y[1]).replace("'", "")+","+str(y[2]).replace("'", "")+","+maybetz+","+str(y[6].replace("'", ""))+","+str(y[6].replace("'", "")+","+ctovet1+"\n"))
family_name.close()
all.close()
name.close()
id.close()
isvote.close()
city.close()
ctovet.close()
file.close()
