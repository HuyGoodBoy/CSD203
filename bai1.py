kichthuoc=int(input('nhap kich thuoc chuoi'))
arr=[]
for i in range(kichthuoc):
    phantu=float(input(f"nhap phan tu{i+1}:"))
    arr.append(phantu)

def timsogantrungbinhnhat(danhsach):
    trungbinhcong=sum(danhsach)/len(danhsach)
    gan_trung_binh = min(danhsach, key=lambda x: abs(x - trungbinhcong))
    vitri= danhsach.index(gan_trung_binh)
    return vitri
ketqua= timsogantrungbinhnhat(arr)
print('so gan nhat la',ketqua)

