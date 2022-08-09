import sys

def solve(num):
    result = 0
    while num >= 3:
        drink = num//3
        result += drink
        num = num%3+drink
    if num == 2:
        result += 1
    return result

def main():
    for line in sys.stdin:
        num = int(line)
        if num <= 0:
            return
        print(solve(num))


if __name__ == '__main__':
    main()