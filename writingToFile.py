f = open("scores.txt", "w")

while True:
    part = input("Enter Name :")

    if part == "quit":
        break
     
    score = input("Enter Score :")

    f.write(part +" " + "score")