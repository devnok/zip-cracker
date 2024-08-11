from util import extract

# 비밀번호가 맞으면 비밀번호 return


def bruteforce(zFile):
    flag = extract(zFile, "123")
    if flag:
        return "123"
    return False
