names=input("Give me the names of the people, seperated by a comma ");

person=names.split(", ");
print(person)
import random;

length =len(person)
print(f"{length}")

card_number= random.randint(0,length-1);
print(card_number);

person_to_pay= person[card_number];
print(person_to_pay);
# print(f"{person_to_pay} have to pay the bill ")


