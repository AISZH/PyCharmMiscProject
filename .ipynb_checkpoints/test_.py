import string
def fun(password):
    if len(password) < 8:
        return "Weak"
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    Count=sum([has_lower,has_lower,has_digit,has_special])

    if Count==4:
        return "Strong"
    if Count==3:
        return "Medium"
    else:
        return "Weak"

def main():
    try:
        number=int(input())
    except EOFError:
        print("请输入一个整数")
        return

    Print=[]
    for i in range(number):
        try:
            password=input()
            Result=fun(password)
            Print.append(Result)
        except EOFError:
            break

    for i in range(number):
        print(Print[i])

if __name__=="__main__":
    main()
