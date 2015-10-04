from itertools import combinations

print(sum(all(((d1 in c1 and d2 in c2) or (d2 in c1 and d1 in c2))
              for d1, d2 in ((0, 1),
                             (0, 4),
                             (0, 6),
                             (1, 6),
                             (2, 5),
                             (3, 6),
                             (4, 6),
                             (8, 1)))
          for c1, c2 in combinations(combinations(list(range(9))+[6], 6), 2)))
