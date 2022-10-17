import pprint


class FischerProj:
    up = 1
    down = 2
    left = 3
    right = 4

    def __eq__(self, other):
        if type(other) is type(self):
            return self.__dict__ == other.__dict__
        return False

    def __init__(self, u=1, d=2, l=3, r=4):
        self.up = u
        self.down = d
        self.left = l
        self.right = r

    def __str__(self):
        return f'{self.up}, {self.down}, {self.left}, {self.right}'

    def __hash__(self):
        return hash((self.up, self.down, self.left, self.right))


group = {
    "id": lambda x: FischerProj(x.up, x.down, x.left, x.right),
    "r0": lambda x: FischerProj(x.down, x.up, x.right, x.left),
    "f1": lambda x: FischerProj(x.left, x.right, x.up, x.down),
    "f2": lambda x: FischerProj(x.right, x.left, x.down, x.up),
    "u1": lambda x: FischerProj(x.up, x.left, x.right, x.down),
    "d1": lambda x: FischerProj(x.right, x.down, x.up, x.left),
    "l2": lambda x: FischerProj(x.down, x.right, x.left, x.up),
    "r2": lambda x: FischerProj(x.left, x.up, x.down, x.right),
    "u2": lambda x: FischerProj(x.up, x.right, x.down, x.left),
    "d2": lambda x: FischerProj(x.left, x.down, x.right, x.up),
    "l1": lambda x: FischerProj(x.right, x.up, x.left, x.down),
    "r1": lambda x: FischerProj(x.down, x.left, x.up, x.right),
}

outputs = {v(FischerProj()): k for k, v in group.items()}
id_proj = FischerProj()


def main():
    table = []
    for x in group.values():
        if outputs[x(id_proj)] == "u2":
            break
        table.append([])
        for y in group.values():
            table[-1].append(outputs[x(y(id_proj))])
            if outputs[y(id_proj)] == "u2":
                break

    pprint.pp(table)


if __name__ == '__main__':
    main()
