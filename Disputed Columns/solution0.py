def main():
    n, m = map(int, input().split())
    strings = []

    for _ in range(n):
        strings.append(input().strip())

    disputed = 0

    for col in range(m):
        distinct = set()

        for row in range(n):
            character = strings[row][col]

            if character != "*":
                distinct.add(character)

            if len(distinct) >= 2:
                disputed += 1
                break

    print(disputed)


if __name__ == "__main__":
    main()
