def escape(jar, fly):
    W, H, d = jar
    x0, y0, vx, vy = fly

    # Let the fly move with a very small step and at that
    # the moment when it reaches the "exit" return True or exit on a crowded iteration

    n = 0
    dx = vx/10000
    dy = vy/10000

    while n < 20:

        # Check for fly out. If it flies along the wall - let it fly
        if ((W-d)/2 < round(x0,1) < (W+d)/2) and (H == round(y0,1)):
            x0 += dx
            y0 += dy
            continue

        # If it flies outside the window - return True
        if ((W-d)/2 < round(x0,1) < (W+d)/2) and (H < round(y0,1)):
            print("Fly is free", "(", round(x0,1), round(y0,1), ")")
            return True

        # If the fly hits the wall along the X axis, expand it
        if 0 <= x0 <= W:
            x0 += dx
        else:
            n += 1
            print(n, "Knock", "(", x0, y0, ")")
            dx = -dx
            x0 += dx

        # If the fly hits the wall along the Y axis, expand it
        if 0 <= y0 <= H:
            y0 += dy
        else:
            n += 1
            print(n, "Knock", "(", x0, y0, ")")
            dy = -dy
            y0 += dy

    return False


if __name__ == '__main__':
    # print("Example:")
    # print(escape([1000, 1000, 200], [0, 0, 100, 0]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert escape([1000, 1000, 200], [0, 0, 100, 0]) == False, "First"
    assert escape([1000, 1000, 200], [450, 50, 0, -100]) == True, "Second"
    assert escape([1000, 1000, 200], [450, 1000, 100, 0]) == False, "Third"
    assert escape([1000, 1000, 200], [250, 250, -10, -50]) == False, "Fourth"
    assert escape([1000, 2000, 200], [20, 35, 100, 175]) == True, "Fifth"
    assert escape([1200,2000,400],[700,500,100,-500]) == False
    assert escape([1200,2000,350],[600,2000,600,1]) == True
    assert escape([1000,2000,200],[0,0,21,2000]) == False
    assert escape([1000,4000,200],[0,0,2000,5000]) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")