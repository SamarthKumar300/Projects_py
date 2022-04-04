print("Welcome to the love calculator ");

name1=input("Please enter your name ");
name2=input("Please enter your love name ");

combined_name = name1+name2;

new_name= combined_name.lower();

t=new_name.count("t");
r=new_name.count("r");
u=new_name.count("u");
e=new_name.count("e");

true= t+r+u+e;

l=new_name.count("l");
o=new_name.count("o");
v=new_name.count("v");
e=new_name.count("e");

love= l+o+v+e;

new_love= str(true) + str(love)
true_love = int(new_love)
print(true_love)
print(type(true_love));

if true_love <10 or true_love> 90:
    print(f"Your love score is {true_love}, your relationship is like coke and mentos ")
elif true_love <=40 and  true_love >=50:
    print(f"Your love score is {true_love}, you both are alright together ")
