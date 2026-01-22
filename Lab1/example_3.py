def is_even(num: int) -> bool:
    return num % 2 == 0

sample_input = int(input("Write a number: "))

sample_output = print("Even" if is_even(sample_input) else "Odd")
