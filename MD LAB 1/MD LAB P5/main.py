# 5. Sierpinski Triangle:
def sierpinski(a):
    rows = 2 ** (a + 2)
    col = rows
    for r in range(0, rows):
        for c in range(0, col):
            print(' ', end="")  # printing space until star
        col -= 1  # minus one space until the next star in another row
        spbs = 0
        while (spbs + col) < rows:
            if (spbs & col) == 0:
                print('* ', end="")
            else:
                print('  ', end="")
            spbs += 1
        print()


n = int(input("Depth = "))
sierpinski(n)
