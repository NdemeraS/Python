f = open("scores.txt", "w")

while True:
    p = input("name :")

    if p == "quit":
        print("Quit")
        break

    s = input("score :")
    
    f.write(p + " "  +  s + "\n")

f.close()