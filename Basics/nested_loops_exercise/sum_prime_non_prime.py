def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_sum = 0
nonprime_sum = 0

while True:
    command = input()
    if command == "stop":
        break

    number = int(command)

    if number < 0:
        print("Number is negative.")
        continue

    if is_prime(number):
        prime_sum += number
    else:
        nonprime_sum += number

print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {nonprime_sum}")
