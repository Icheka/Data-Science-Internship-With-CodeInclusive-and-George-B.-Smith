'''
Question 2: Write a program that computes the value of a+aa+aaa+aaaa
with a given digit as the value of a.
'''

def solve(digit):
    digit = str(digit)
    new_digit = ''
    ans = 0

    for i in range(1, 5):
        n = digit * i
        ans += int(n)

    return ans


def main():
    try:
        digit = int(input("Enter a value for a: "))
    except ValueError:
        print("You have to enter an integer!")
    else:
        print(solve(digit))

main()
