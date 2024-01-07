danhsach=input('nhap so cach nhau bang dau cach')
def loaisolaplai(so):
    danhsachsau=[]
    socuoicung= []
    for i in so.split():
        if i not in socuoicung:
            danhsachsau.append(i)
        socuoicung.append(i)
    return ' '.join(danhsachsau)
ketqua= loaisolaplai(danhsach)
print('ket qua la',ketqua)