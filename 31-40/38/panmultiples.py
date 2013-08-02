def is_pan(i):
        return len(i) == 9 and len(i) == len(set(i)) and not "0" in i

