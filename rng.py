import random
import time

if __name__ == '__main__':

    while True:
        time.sleep(1.0)
        with open('prng-service.txt', 'r') as f:
            read_data = f.readline()
        if read_data == "run":
            num = {random.randint(1, 100)}
            with open('prng-service.txt', 'w') as f:
                f.write(f"{random.randint(1, 15)}")
