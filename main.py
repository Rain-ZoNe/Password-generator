import random

sumbol = 'qwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*=-+_'
password = ''
for i in range(12):
    password += random.choice(sumbol)
print(password)
