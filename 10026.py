import sys
import random
import time
def main():
    input = sys.stdin.readline
    for _ in range(100):
        random_numbers = random.sample(range(10),4)
        random_numbers_str = ' '.join(map(str, random_numbers))
        bigyo = ''.join(map(str, random_numbers))
        print(random_numbers_str)

        start_time = time.time()
        user_input = input().strip()
        end_time = time.time()
        

        if user_input == bigyo:
            chai = end_time - start_time
            print(f"time: {chai:4f}초")
        else:
            print("너 이러면 또 망해")
if __name__ == '__main__':
    main()



    