# Block positions by rotation

# focal point is (1, 0)
I = {"identity": [(0, 0), (1, 0), (2, 0), (3, 0)],
     "clockwise": [(1, -1), (1, 0), (1, 1), (1, 2)],
     "counterclockwise": [(1, -2), (1, -1), (1, 0), (1, 1)],
     "half-turn": [(0, 0), (1, 0), (2, 0), (3, 0)]}

# focal point is (0, 1)
L = {"identity": [(0, 0), (0, 1), (0, 2), (1, 2)],
     "clockwise": [(-1, 1), (-1, 2), (0, 1), (1, 1)],
     "counterclockwise": [(-1, 1), (0, 1), (1, 1), (1, 0)],
     "half-turn": [(-1, 0), (0, 0), (0, 1), (0, 2)]}

# focal point is (1, 1)
rL = {"identity": [(1, 0), (1, 1), (1, 2), (0, 2)],
      "clockwise": [(0, 0), (0, 1), (1, 1), (2, 1)],
      "counterclockwise": [(0, 1), (1, 1), (2, 1), (2, 2)],
      "half-turn": [(0, 0), (1, 0), (0, 1), (0, 2)]}

# focal point is (0, 1)
Z = {"identity": [(1, 0), (0, 1), (1, 1), (0, 2)],
     "clockwise": [(0, 0), (1, 0), (1, 1), (2, 1)],
     "counterclockwise": [(0, 0), (1, 0), (1, 1), (2, 1)],
     "half-turn": [(1, 0), (0, 1), (1, 1), (0, 2)]}

# focal point is (0, 1)
S = {"identity": [(0, 0), (0, 1), (1, 1), (1, 0)],
     "clockwise": [(0, 0), (0, 1), (1, 1), (1, 0)],
     "counterclockwise": [(0, 0), (0, 1), (1, 1), (1, 0)],
    "half-turn": [(0, 0), (0, 1), (1, 1), (1, 0)]}

blocks = {"I": I, "L": L, "rL": rL, "Z": Z, "S": S}