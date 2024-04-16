alphabet=["a","b","c","d","e"]
first_letter=alphabet[0]
last_letter=alphabet[-1]
first_three = alphabet[:3]
last_three = alphabet[-3:]
print(f"{alphabet}\n{first_letter}\n{last_letter}\n{first_three}\n{last_three}")
alphabet.append("f")
alphabet.append("g")
alphabet.append("h")
print(f"{alphabet}")
last_three = alphabet[-3:] 
alphabet.remove("h")
print(f"{last_three}\n{alphabet}")