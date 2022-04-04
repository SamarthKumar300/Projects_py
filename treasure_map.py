# from turtle import position


row1=["😄","😄","😄"];
row2=["😄","😄","😄"];
row3=["😄","😄","😄"];

map =[row1,row2,row3];

print(f"{row1}\n,{row2}\n,{row3}\n ");

position=input("Where you want to put your treasure? Write the row and column number "); 

print(position);
print(type(position));

num_row=int(position[0])-1;
num_column=int(position[1])-1;

print(type(num_column));
print(type(num_row));

map[num_row][num_column] ="X";

print(f"{row1},\n{row2},\n{row3}");


