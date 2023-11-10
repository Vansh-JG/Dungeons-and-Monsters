class Map:
    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            # cls._instance.__init__()
        return cls._instance

    def __init__(self):
        file = open("map.txt")
        list2d = []
        for row in file:
            list2d.append(list(row))  # removes '' and '\n'
        self._map = list2d
        if self._initialized:
            return self._map

    def __getitem__(self, row):
        return self._map[row]

    def __len__(self):
        return len(self._map)

    def show_map(self, loc):  # fix
        for i in range(len(self._map)):
            for j in range(len(self._map[i])):
                sloc = False
                if sloc == False:
                    print("X", end="")
                if i == loc[0] and j == loc[1]:
                    self.reveal(sloc)
                    print("*", end="")
                else:
                    print(self._map[i][j], end="")
        print("")

    def reveal(self, loc):
        loc = True

    def remove_at_loc(self, loc):
        if loc != 'n':
            loc = 'n'
        return loc



