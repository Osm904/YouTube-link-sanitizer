# Made by Osm904 (me)

x = input("YouTube link: ")
x = x.partition("=")
xtwo = x[2].partition("&t=")
if(len(xtwo) == 3):
    x = x[0] + "=" + xtwo[1] + xtwo[2]
    print(x)
else: #how would you ever fuck this up in any other way
    x = x[0] + "="
    print(x)