import random


ice_cream = {"Alice": "choco"} 

print(ice_cream["Alice"])


print(random.randint(1, 6))


cards = ["hack", "smith", "ate", "now"]

print("physics\nchem\nbio")


print("""aksmdaksdmaskdmaskdlmasdmas
      dmalsdmaslkdmasldkamslkdma
      ;asldmlasdmas;lmdasdl;ams;ldmasl
      """)


captitals = {
    "Zim": "Hre",
    "SA" : "Pta",
    "Zam": "Lus",
    "Mal": "Blantyre",
    "Bots": "Gabs",
    "Ken" : "Nai"
}


country = list(captitals.keys())

for n in country:
    print(n)

# for i in [1, 2, 3, 4, 5]:
#     count = random.choice(country)
#     cap = captitals[count]
#     cap_guess = input("What is the capital of " + count + " ? ")

#     if cap_guess == cap:
#         print("nice!!")
#     else:
#         print("Nope! Correct answer is " + cap)

# print("and done")

t = 0
while t < 5:
    print("Mee!")
    print(t)
    t += 1

t = 0
while True:
    user_input = input(">")
    if user_input == "quit":
        print("goodbye")
        break
    else:
        print("Hi")