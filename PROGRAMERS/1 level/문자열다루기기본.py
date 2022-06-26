def solution(s):
    try:
        a = int(s)
        if len(s) == 4 or len(s) == 6:
            return True
        else:
            return False
    except:
        return False

s = "a234"