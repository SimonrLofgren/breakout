


def lvl_1():
    x = 50
    y = 0
    lines = 5
    objects = []
    for l in range(lines):
        x = 50
        y += 30
        for _ in range(9):
            color = RED
            screen = lvl_screen
            obst = Rect(x, y, 70, 20, color, screen, True, False)
            objects.append(obst)
            x += 80
    return objects
















def main():
    pass


if __name__ == "__main__":
    main()
