num_list = input("შეიყვანე რიცხვების სია: ").split()

num_list = [int(num) for num in num_list]


max_num = max(num_list)
min_num = min(num_list)


print("მაქსიმალური:", max_num)
print("მინიმალური:", min_num)
