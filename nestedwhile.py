players = 3
i = 1

while i <= players:
    print("\nPlayer", i)

    runs = 0
    balls = 0
    fours = 0
    sixes = 0
    j = 1

    while j <= 6:
        r = int(input("Enter runs: "))

        runs += r
        balls += 1

        if r == 4:
            fours += 1
        elif r == 6:
            sixes += 1

        j += 1

    print("\nRuns :", runs)
    print("Balls:", balls)
    print("Fours:", fours)
    print("Sixes:", sixes)
    print("----------------")

    i += 1