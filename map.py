class Map:
    _instance = None
    _initialised = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self._map = []
        self._revealed = []
        self.load_map(1)

    def load_map(self, map_num):
        self._map = []
        self._revealed = []
        map_list = ["map1.txt", "map2.txt", "map3.txt"]
        file = open(map_list[map_num - 1], 'r')
        contents = file.read()
        lines = contents.split("\n")
        for line in lines:
            temp = []
            for i in line:
                temp.append(i)
            self._map.append(temp)
        file.close()
        for i in range(len(self._map)):
            row = []
            for j in range(len(self._map[i])):
                row.append(False)
            self._revealed.append(row)

    def __getitem__(self, row):
        return self._map[row]

    def __len__(self):
        return len(self._map)

    def show_map(self, loc):

        for i in range(len(self._map)):
            for j in range(len(self._map[i])):
                if i == loc[0] and j == loc[1]:
                    print("*", end="  ")
                elif self._revealed[i][j]:
                    print(self._map[i][j], end="  ")
                else:
                    print("X", end="  ")
                # print(self._map[i][j], end="  ")
            print()

    def reveal(self, loc):
        r, c = loc
        self._revealed[r][c] = True

    def remove_at_loc(self, loc):
        r, c = loc
        self._map[r][c] = 'n'
