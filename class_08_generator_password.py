import random, string

length_password = int(input('Length password: '))

chars = string.ascii_letters + string.digits + '%()!çÇ?.=+-*[]{}'

randomic = random.SystemRandom()

print(''.join(randomic.choice(chars) for i in range(length_password)))


# join this command concatenate
# random.SystemRandom() get of system a random value
# choice this function choose between the caracters available randomly