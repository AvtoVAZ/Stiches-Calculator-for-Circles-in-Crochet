a1 = int(input("How many stitches should the first row have (recommended 6): "))
knownorunkown = int(input("Do you know the increase if yes press (1) or if not press (2): "))
if knownorunkown == 1:
    omega3 = int(input("How much should the increase be: "))
    n = int(input("What is the number of the row you want to check the number of stitches: "))
    an = (a1) + (n - 1) * (omega3)
    print("If the number of the rows are", an, "and the increase is", omega3, "the row", n, "should have", an,
          "stitches.")
if knownorunkown == 2:
    omega1 = int(input("Number of stitches in the previous row: "))
    omega2 = int(input("Number of stitches in current row: "))
    omega3 = (omega2) - (omega1)
    n = int(input("What is the number of the row you want to check the number of stitches: "))
    an = (a1) + (n - 1) * (omega3)
    print("If the number of the rows are", an, "and the increase is", omega3, "the row", n, "should have", an,
          "stitches.")
    if omega3 < 0:
        print("Invalid increase shutting down.")
    if omega3 == 0:
        print("Invalid increase shutting down.")
if knownorunkown > 3:
    print("Invalid output shutting down.")
