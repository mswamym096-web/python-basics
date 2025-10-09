#for  loop on list

for i in [1,2,3,4,5]:
     print(i)


     # for loop on tuples

for i in (1,2,3,4,5):
      print(i)


# for loop on string

for i in "hello":
    print(i)


# for loop on dictionary

family = {
    "name":"a",
    "fname":"fa",
    "mname":"ma",

}

for fam in family:
    print(fam, family[fam])


familylist =[
    {    
        "name":"a",
        "fname":"fa",
        "mname":"ma",
    },
    {   
        "name":"a1",
        "fname":"fa",
        "mname":"ma",

    },
    {
        "name":"a2",
        "fname":"fa",
        "mname":"ma",
    }
]
for flist in familylist:
    print(flist["name"])
    if flist["name"]=='a':
        continue
    flist.update({"country":"india"})
    print(flist)

print("list:",familylist)

# range

for i in range(1,10):
    print(i)

#continue and break

vowels = ['a','i','e','u','o']
countryname = "india"


for char in countryname:
    if char in vowels:
        continue
    print(char)

for char in countryname:
    if char =='a':
        break
    print(char)

print("I AM OUTSIDE")

