abc = 1
for _ in range(3):
    input_data = int(input())
    abc *= input_data


for i in range(10):
    print(str(abc).count(str(i)))