from random import randint

cargo = [12, 30, 30, 32, 42, 49]

list_min_disbalances = []



for _ in range(10000):

    min_disbalance = sum(cargo)

    for _ in range(300):

        cargo_left = []
        cargo_right = []

        for i in cargo:
            cargo_left.append(i) if randint(0, 1) else cargo_right.append(i)

        tmp_disbalance = abs(sum(cargo_left) - sum(cargo_right))

        min_disbalance = tmp_disbalance if min_disbalance>tmp_disbalance else min_disbalance

        # print("cargo_left", cargo_left)
        # print("cargo_right", cargo_right)
    list_min_disbalances.append(min_disbalance)
    # print("\n", "min_disbalance", min_disbalance)


print(list_min_disbalances, list_min_disbalances.count(9))