# Generate a random IP address
import random
S1 = random.randint(1,255)
S2 = random.randint(1,255)
S3 = random.randint(1,255)
S4 = random.randint(1,255)
IP = str(S1) + '.' + str(S2) + '.' + str(S3) + '.' + str(S4)
print(IP)