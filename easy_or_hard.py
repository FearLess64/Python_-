num = int(input("შეიყვანეთ რიცხვი: "))

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "ეს რთული რიცხვია")
            break
    else:
        print(num, "ეს მარტივი რიცხვია")
