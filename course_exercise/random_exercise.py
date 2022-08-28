# رندوم متفاوت: تابعی بنویس که عدد رندوم بین ۱ تا ۱ میلیون برگردونه و
#  این عدد رندوم با ۱۰ عدد قبلی که این تابع  برگردانده متفاوت باشه.
import random

previous_amounts = []


def rand():
    random_number = random.randrange(1, 1000000)
    if len(previous_amounts) > 10:
        previous_amounts.pop(0)
    if random_number in previous_amounts:
        return rand()
    previous_amounts.append(random_number)
    return random_number


for num in range(0, 20):
    print(rand())
