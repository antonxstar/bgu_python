for p in range(1,51):           # перебирать p в диапозоне от 1 до 51
    for q in range(p+1,51):         # перебирать q в диапозоне от p + 1 до 51
        for r in range(q+1,51):       # перебирать r в диапозоне от q + 1 до 51
            if p**2 + q**2 == r**2:          # если p^2 + q^2 = r^2, то вывести эту тройку
                print(p,q,r)