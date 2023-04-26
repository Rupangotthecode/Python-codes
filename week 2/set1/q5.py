
def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n-1) + fibonacci(n-2)

fibonacci_list = [fibonacci(i) for i in range(11)]

odd_fibonacci = list(filter(lambda x: x%2 != 0, fibonacci_list))
even_fibonacci = list(filter(lambda x: x%2 == 0, fibonacci_list))

print("Fibonacci Numbers: ", fibonacci_list)
print("Odd Fibonacci Numbers: ", odd_fibonacci)
print("Even Fibonacci Numbers: ", even_fibonacci)
