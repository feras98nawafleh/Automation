import re

with open("assets/potential-contacts.txt") as R:
    all_data = R.read()

allMails = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', all_data)
allMails.sort()
allMails =list(dict.fromkeys(allMails))

allPhoneNumbers = re.findall(r"\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}", all_data)
allPhoneNumbers.sort()
allPhoneNumbers = list(dict.fromkeys(allPhoneNumbers))
list_of_numbers = []

for i in allPhoneNumbers:
    i=i.replace(".","-")  
    i=i.replace(")","-")  
    i=i.replace("(","")  
    if len(i) == 10:
        i = i[:3] + "-" + i[3:6] + "-" + i[6:]
    list_of_numbers.append(i)


with open("assets/allPhoneNumbers.txt" , "w") as f:
    f.write(f"{list_of_numbers}")

with open("assets/allMails.txt" , "w") as f:
    f.write(f"{list_of_numbers}")




