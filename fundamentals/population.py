def nb_year(p0, percent, aug, p):
    current_poplulation = p0
    year = 0
    while p >= current_poplulation:
        year += 1
        current_poplulation = (
            current_poplulation + current_poplulation * percent / 100 + aug
        )

    return year
