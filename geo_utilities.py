def rozpoznaj_uklad(x: float, y: float):
    """Zwraca kod EPSG jednego z polskich układów, na podstwie wspolrzednych"""
    x, y = int(x), int(y)
    coord_len = (len(str(x)), len(str(y)))

    if coord_len == (6, 6):
        return "2180"
    elif coord_len == (7, 7):
        return strefa_2000(y)
    else:
        return None


def strefa_2000(y):
    cecha = int(str(y)[0])

    kody = {5: "2176", 6: "2177", 7: "2178", 8: "2179"}

    result = kody.get(cecha, None)
    return result
