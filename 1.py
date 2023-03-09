import random

numbers = random.sample(range(1, 50), )

print("樂透號碼開獎：" + " ".join(map(str, sorted(numbers))))
print(f"特別號： {random.randint(1, 50)}")
