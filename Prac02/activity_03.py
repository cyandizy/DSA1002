def to_base(decimal, base):
    if base > 16 or base < 2:
        raise ValueError("Base must be between 2 and 16")
    
    if decimal < 0:
        raise ValueError("Decimal must be non-negative")

    if decimal > 0:
        remainder = decimal % base
        if remainder < 10:
            return str(to_base(decimal // base, base)) + str(remainder)
        else:
            return str(to_base(decimal // base, base)) + chr(remainder + 87)
    else:
        return ""
    
try:
    print(to_base(100000, 16))
except TypeError as e:
    print(f"Error: make sure parameters are in int;\n{e}")

