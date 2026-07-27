lst = []
num = 57
check = 0
var = 0
condition = True

while condition:
    check += 1
    var = num * check

    digit = [x for x in str(var)]
    print(f"check: {check}, var: {var} / digit : {digit}")


    verify = digit[1:]
    joined_str = "".join(verify)
    result = int(joined_str)
    print(f"verify : {verify}, result: {result}")

    if result * num == var:
        condition = False

print(f"Positive integer: {var} becomes 57 times smaller when the first digit is deleted")


