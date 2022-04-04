print("Welcome to the tip calculator");
total_bill=input("What is total amount of the bill?\n");
tip_perc=input("How much percent of tip you would like to make 0,10,20 ? \n");
num_of_people= input("Total number of people \n");


remain_amount=float(total_bill)-(float(total_bill)*(float(tip_perc)/100));

each_person_pay=remain_amount/float(num_of_people);

individual_pay=round(each_person_pay,2);


print(f"The amount each person have to pay is {individual_pay}");