

def Pecahan(bil, n, d):
    if bil>0:
        return (bil*d+n)/d
    else:
        return (bil*d-n)/d

print(Pecahan(1, 1, 2))

def NIK(nik):
    tanggal = int(nik[6:8])
    if tanggal >= 40:
        tanggal = tanggal - 40

    bulan = nik[8:10]
    if bulan == "01":
        bulan = "januari"
    elif bulan == "02":
        bulan = "februari"
    tahun = int(nik[10:12])
    if tahun>21:
        tahun = 1900+tahun
    else:
        tahun = 2000+tahun
    return f'{tanggal} {bulan} {tahun}'

print(NIK("3375025001900003"))

def square(top, bottom):
    return [top, bottom]

def makeP(x, y):
    return [x, y]

def top(square):
    return square[0]

def bottom(square):
    return square[1]

def absis(point):
    return point[0]

def ordinat(point):
    return point[1]

def GetPanjang(square):
    garis1 = absis(top(square))-absis(bottom(square))
    garis2 = ordinat(top(square))-ordinat(bottom(square))
    if garis1>garis2:
        return garis1
    else:
        return garis2

def GetLebar(square):
    garis1 = absis(top(square))-absis(bottom(square))
    garis2 = ordinat(top(square))-ordinat(bottom(square))
    if garis1<garis2:
        return garis1
    else:
        return garis2

def GetPanjang(square):
    garis1 = absis(top(square))-absis(bottom(square))
    garis2 = ordinat(top(square))-ordinat(bottom(square))
    return garis1*garis2


top1 = makeP(3,2)
bottom1 = makeP(-2,-1)
square1 = square(top1, bottom1)
print(square1)

