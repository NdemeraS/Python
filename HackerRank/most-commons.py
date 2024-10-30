##
## https://www.hackerrank.com/challenges/most-commons/problem?isFullScreen=true
##


s = "tctesvgnclzykpmbcqixlonfidpdjbynrcpxsjmucpeyormenrjbibafpzkquminfnnbizgbpxeovefuykjrcebfnntvyamkgykcnvjqxvnprwrarpcgrjoucywgfnbnysgwzymcxyachlpsglosflsubqhvobedbtzuqmvgyvrpeclcsoeemysuyuejpjtahnrzmebztrjtzhhjtqlmhttxdnjilqsqymmhjmlzikkdzasshfktbfsaozyhaduyqcufucqxxuksnfjaiwacvlyiimfrzyxwobrfoalhmowcobbpwuqpwvlstbngxjrebfnckbcagoacmfuzvmqxefiwqkgfwgghxbulvhqiaqewdmmizjfgyymchohejdpsnnpvmtgqzxkesnrikywoolootuuikapycpxhkrplyuhzhndxckbvaynkzreybomwuemxtgmrjxbysarlsemwambppmrumivznuaqskzgpamfsjwwrjvtwyqpainuyyfmwnegjlmanqwvshvpsbpeykfwykdumdgjlkuwoxwqctihfdwvxrefggsxmjtxmpdcigjertcxwennzyamqpahytneybgmdyupusarhemazvozdqurftdvbnavynrsdzxjebjrdatbkoezdgwznplqqzakozjecyewsidawuxfpusmeusantzdglridxnwvbgwjcaofbplnwyxtmwerskdzwhgxfdqbpfhymlgwtvqeehnnhwgklxqkdjgmfxvuxwwpmnqxsaiitfehhbqdyveqfrqjjfnggmhjrgldgctnhzrrqdtbunxxcuwibqkjdickhrtbznevczqoidnfmtaveysysrgbhctwxmevuutrwyriugtuvhuxkqapfjyplczgekxisffoivofobqmipqxzunlrrtcmaivvhbfjvgywwtqubwszqwjtskyuxljhinqrhcgddejurivukcspaazjjwwloreqlreqjifwsv"

# s = input()

letter_dict = {}


for item in s:
    if item in letter_dict.keys():
        letter_dict[item] = letter_dict[item] + 1
    else:
        letter_dict[item] = 1


# print(letter_dict)

myKeys = list(letter_dict.keys())
myKeys.sort()

sd = {i: letter_dict[i] for i in myKeys}


val_based_rev = {k: v for k, v in sorted(sd.items(), key=lambda item: item[1], reverse=True)}

print(val_based_rev)


x = 1

for item in val_based_rev:
    print(str(item) + " " + str(val_based_rev[item]))
    x = x + 1

    if x > 4:
        break

# l = {"a": 1}

# print(l["a"])

# l["a"] = l["a"] + 1

# print(l["a"])