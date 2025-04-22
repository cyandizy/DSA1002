def towers(n, src, dest, depth=0):
    if src < 1 or src > 3 or dest < 1 or dest > 3:
        raise ValueError("Source or destination is out of bound.")
    
    if n <= 0:
        raise ValueError("Invalid number of disks")

    if (n == 1):
        move_disk(n, src, dest, depth)
    else:
        tmp = 6 - src - dest
        towers(n - 1, src, tmp, depth + 1)
        move_disk(n, src, dest, depth)
        towers(n - 1, tmp, dest, depth + 1)

def move_disk(n, src, dest, depth):
    global STEPS
    level = "\t" * depth
    print(f"{level}Recursion Level = {depth + 1}")
    print(f"{level}Moved disk from postion {src} to position {dest}")
    print(f"{level}n={n}, src={src}, dest={dest}")
    STEPS += 1

STEPS = 0
print("-" * 60)
towers(3, 1, 3)
print(f"\nThere are {STEPS} moves for this problem.")