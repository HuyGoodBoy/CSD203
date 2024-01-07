def nhap_diem():
    while True:
        try:
            diem = float(input("Nhập điểm (từ 0 đến 10): "))
            if 0 <= diem <= 10:
                return diem
            else:
                print("Dữ liệu không hợp lệ! Điểm phải nằm trong khoảng từ 0 đến 10.")
        except ValueError:
            print("Dữ liệu không hợp lệ! Vui lòng nhập một số thập phân hợp lệ.")

def convert_to_alphabetic_grade(diem):
    if diem >= 9:
        return 'A'
    elif diem >= 8:
        return 'B'
    elif diem >= 7:
        return 'C'
    elif diem >= 6:
        return 'D'
    else:
        return 'F'

def convert_to_4th_system(diem):
    if diem >= 8:
        return '4.0'
    elif diem >= 7:
        return '3.5'
    elif diem >= 6:
        return '3.0'
    elif diem >= 5:
        return '2.0'
    else:
        return '0.0'

if __name__ == "__main__":
    diem_mon_hoc = nhap_diem()
    grade_alphabetic = convert_to_alphabetic_grade(diem_mon_hoc)
    grade_4th_system = convert_to_4th_system(diem_mon_hoc)

    print(f"Điểm đã nhập là: {diem_mon_hoc}")
    print(f"Grade (theo bảng chữ cái): {grade_alphabetic}")
    print(f"Grade (hệ thống 4.0): {grade_4th_system}")
