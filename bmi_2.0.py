height=float(input("Please enter your height "));
weight=float(input("Please enter your weight"));

bmi= weight/(height**2);

int_bmi= round(bmi,1);

if int_bmi <18.5:
    print(f"Your BMI is {int_bmi}, you are underweight");
elif int_bmi <25:
    print(f"Your BMI is {int_bmi}, you have a normal weight ");
elif int_bmi <30:
    print(f"Your BMI is {int_bmi}, you are overweight");
elif int_bmi <35:
    print(f"Your BMI is {int_bmi}, you are obese");
else:
    print(f"Your BMI is {int_bmi}, you are clinically obese");
