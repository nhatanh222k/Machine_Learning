import math

# 1. DỮ LIỆU

# Mỗi dòng gồm:
# [Số tiền, Số lần giao dịch, Khoảng cách, Gian lận]

du_lieu = [
    ["Thap",  "It",    "Gan",  0],
    ["Thap",  "It",    "Xa",   0],
    ["Thap",  "Nhieu", "Gan",  0],
    ["Thap",  "Nhieu", "Xa",   1],

    ["Cao",   "It",    "Gan",  0],
    ["Cao",   "It",    "Xa",   1],
    ["Cao",   "Nhieu", "Gan",  1],
    ["Cao",   "Nhieu", "Xa",   1],

    ["Thap",  "It",    "Gan",  0],
    ["Cao",   "Nhieu", "Xa",   1],
]


# Tên các thuộc tính
ten_thuoc_tinh = [
    "Số tiền",
    "Số lần giao dịch",
    "Khoảng cách"
]

# 2. TÍNH ĐỘ HỖN LOẠN

def tinh_do_hon_loan(nhan):

    # Đếm số lượng từng loại nhãn
    dem = {}

    for gia_tri in nhan:

        if gia_tri not in dem:
            dem[gia_tri] = 0

        dem[gia_tri] += 1

    tong = len(nhan)

    do_hon_loan = 0

    # Công thức:
    # Độ hỗn loạn = - tổng(p * log2(p))

    for so_luong in dem.values():

        p = so_luong / tong

        if p > 0:
            do_hon_loan = do_hon_loan - p * math.log2(p)

    return do_hon_loan

# 3. TÍNH ĐỘ LỢI THÔNG TIN

def tinh_do_loi_thong_tin(X, y, vi_tri):

    # Độ hỗn loạn ban đầu
    do_hon_loan_ban_dau = tinh_do_hon_loan(y)

    # Tìm các giá trị khác nhau của thuộc tính
    cac_gia_tri = set()

    for dong in X:
        cac_gia_tri.add(dong[vi_tri])

    do_hon_loan_sau_khi_chia = 0

    # Chia dữ liệu thành các nhóm
    for gia_tri in cac_gia_tri:

        nhom_nhan = []

        for i in range(len(X)):

            if X[i][vi_tri] == gia_tri:
                nhom_nhan.append(y[i])

        # Tỷ lệ của nhóm
        ty_le = len(nhom_nhan) / len(y)

        # Độ hỗn loạn của nhóm
        do_hon_loan_nhom = tinh_do_hon_loan(nhom_nhan)

        # Cộng vào độ hỗn loạn sau khi chia
        do_hon_loan_sau_khi_chia += (
            ty_le * do_hon_loan_nhom
        )

    # Độ lợi thông tin
    do_loi = (
        do_hon_loan_ban_dau
        - do_hon_loan_sau_khi_chia
    )

    return do_loi

# 4. TÌM THUỘC TÍNH TỐT NHẤT

def tim_thuoc_tinh_tot_nhat(X, y, cac_thuoc_tinh):

    do_loi_lon_nhat = -1

    thuoc_tinh_tot_nhat = None

    for vi_tri in cac_thuoc_tinh:

        do_loi = tinh_do_loi_thong_tin(
            X,
            y,
            vi_tri
        )

        print(
            "Độ lợi thông tin của",
            ten_thuoc_tinh[vi_tri],
            "=",
            round(do_loi, 4)
        )

        if do_loi > do_loi_lon_nhat:

            do_loi_lon_nhat = do_loi

            thuoc_tinh_tot_nhat = vi_tri

    return thuoc_tinh_tot_nhat

# 5. TÌM NHÃN XUẤT HIỆN NHIỀU NHẤT

def tim_nhan_pho_bien_nhat(y):

    dem = {}

    for gia_tri in y:

        if gia_tri not in dem:
            dem[gia_tri] = 0

        dem[gia_tri] += 1

    return max(dem, key=dem.get)

# 6. XÂY DỰNG CÂY ID3

def xay_dung_cay(X, y, cac_thuoc_tinh):

    # Nếu tất cả dữ liệu đều cùng một nhãn
    if len(set(y)) == 1:

        return y[0]


    # Nếu không còn thuộc tính để chia
    if len(cac_thuoc_tinh) == 0:

        return tim_nhan_pho_bien_nhat(y)


    # Tìm thuộc tính tốt nhất
    thuoc_tinh_tot_nhat = tim_thuoc_tinh_tot_nhat(
        X,
        y,
        cac_thuoc_tinh
    )

    ten = ten_thuoc_tinh[thuoc_tinh_tot_nhat]

    print()
    print("Chọn thuộc tính:", ten)
    print("-----------------------------")


    # Tạo nút của cây
    cay = {
        ten: {}
    }


    # Tìm các giá trị khác nhau
    cac_gia_tri = set()

    for dong in X:

        cac_gia_tri.add(
            dong[thuoc_tinh_tot_nhat]
        )


    # Tạo danh sách thuộc tính còn lại
    thuoc_tinh_con_lai = []

    for vi_tri in cac_thuoc_tinh:

        if vi_tri != thuoc_tinh_tot_nhat:

            thuoc_tinh_con_lai.append(vi_tri)


    # Tạo các nhánh
    for gia_tri in cac_gia_tri:

        X_moi = []
        y_moi = []


        for i in range(len(X)):

            if X[i][thuoc_tinh_tot_nhat] == gia_tri:

                X_moi.append(X[i])

                y_moi.append(y[i])


        # Nếu không có dữ liệu
        if len(y_moi) == 0:

            cay[ten][gia_tri] = (
                tim_nhan_pho_bien_nhat(y)
            )

        else:

            cay[ten][gia_tri] = xay_dung_cay(
                X_moi,
                y_moi,
                thuoc_tinh_con_lai
            )


    return cay

# 7. DỰ ĐOÁN MỘT GIAO DỊCH

def du_doan(cay, mau):

    # Nếu đã đến nút cuối
    if not isinstance(cay, dict):

        return cay


    # Lấy tên thuộc tính hiện tại
    ten_hien_tai = list(cay.keys())[0]


    # Tìm vị trí của thuộc tính
    vi_tri = ten_thuoc_tinh.index(
        ten_hien_tai
    )


    # Lấy giá trị của mẫu
    gia_tri = mau[vi_tri]


    # Đi xuống nhánh tương ứng
    cay_con = cay[
        ten_hien_tai
    ][gia_tri]


    return du_doan(
        cay_con,
        mau
    )

# 8. TÁCH DỮ LIỆU ĐẦU VÀO VÀ KẾT QUẢ

X = []
y = []

for dong in du_lieu:

    X.append(dong[:3])

    y.append(dong[3])

# 9. XÂY DỰNG CÂY

print()
print("==========================================")
print("          XÂY DỰNG CÂY ID3")
print("==========================================")

cac_thuoc_tinh = [0, 1, 2]

cay_id3 = xay_dung_cay(
    X,
    y,
    cac_thuoc_tinh
)


print()
print("==========================================")
print("              CÂY QUYẾT ĐỊNH")
print("==========================================")

print(cay_id3)

# 10. DỰ ĐOÁN VÀ IN KẾT QUẢ DỄ HIỂU

print()
print("======================================================")
print("                 KẾT QUẢ DỰ ĐOÁN")
print("======================================================")

y_du_doan = []

for i in range(len(X)):

    mau = X[i]

    # Dự đoán
    ket_qua = du_doan(cay_id3, mau)

    y_du_doan.append(ket_qua)

    # Chuyển 0, 1 thành chữ dễ hiểu
    if y[i] == 1:
        thuc_te = "Gian lận"
    else:
        thuc_te = "Không gian lận"

    if ket_qua == 1:
        du_doan_text = "Gian lận"
    else:
        du_doan_text = "Không gian lận"

    # Kiểm tra dự đoán đúng hay sai
    if y[i] == ket_qua:
        ket_qua_text = "ĐÚNG"
    else:
        ket_qua_text = "SAI"

    print()
    print("Giao dịch", i + 1)
    print("  Số tiền          :", mau[0])
    print("  Số lần giao dịch :", mau[1])
    print("  Khoảng cách      :", mau[2])
    print("  Thực tế          :", thuc_te)
    print("  Dự đoán          :", du_doan_text)
    print("  Kết quả          :", ket_qua_text)

# 11. TÍNH BẢNG ĐỐI CHIẾU

duong_dung = 0
am_dung = 0
duong_sai = 0
am_sai = 0

for i in range(len(y)):

    thuc_te = y[i]
    ket_qua = y_du_doan[i]

    # Thực tế gian lận, dự đoán gian lận
    if thuc_te == 1 and ket_qua == 1:
        duong_dung += 1

    # Thực tế không gian lận, dự đoán không gian lận
    elif thuc_te == 0 and ket_qua == 0:
        am_dung += 1

    # Thực tế không gian lận, dự đoán gian lận
    elif thuc_te == 0 and ket_qua == 1:
        duong_sai += 1

    # Thực tế gian lận, dự đoán không gian lận
    elif thuc_te == 1 and ket_qua == 0:
        am_sai += 1

# 12. IN BẢNG ĐỐI CHIẾU

print()
print("======================================================")
print("                  BẢNG ĐỐI CHIẾU")
print("======================================================")

print()
print("                    Dự đoán")
print("                 Không gian lận     Gian lận")
print()
print(
    "Thực tế không gian lận      ",
    f"{am_dung:^18}",
    f"{duong_sai:^10}"
)
print(
    "Thực tế gian lận            ",
    f"{am_sai:^18}",
    f"{duong_dung:^10}"
)

print()
print("Giải thích:")
print("  - Dự đoán đúng không gian lận :", am_dung)
print("  - Dự đoán đúng gian lận       :", duong_dung)
print("  - Báo gian lận nhưng thực tế không gian lận:", duong_sai)
print("  - Báo không gian lận nhưng thực tế gian lận:", am_sai)

# 13. TÍNH CÁC CHỈ SỐ

do_chinh_xac = (
    duong_dung + am_dung
) / len(y)


if duong_dung + duong_sai != 0:

    do_chinh_xac_du_doan_gian_lan = (
        duong_dung
        / (duong_dung + duong_sai)
    )

else:

    do_chinh_xac_du_doan_gian_lan = 0


if duong_dung + am_sai != 0:

    do_bao_phu = (
        duong_dung
        / (duong_dung + am_sai)
    )

else:

    do_bao_phu = 0


if (
    do_chinh_xac_du_doan_gian_lan
    + do_bao_phu
) != 0:

    diem_f1 = (
        2
        * do_chinh_xac_du_doan_gian_lan
        * do_bao_phu
        /
        (
            do_chinh_xac_du_doan_gian_lan
            + do_bao_phu
        )
    )

else:

    diem_f1 = 0

# 14. IN CÁC CHỈ SỐ ĐÁNH GIÁ

print()
print("======================================================")
print("             ĐÁNH GIÁ MÔ HÌNH")
print("======================================================")

print()
print(
    "Độ chính xác:",
    round(do_chinh_xac * 100, 2),
    "%"
)

print(
    "Độ chính xác khi dự đoán gian lận:",
    round(
        do_chinh_xac_du_doan_gian_lan * 100,
        2
    ),
    "%"
)

print(
    "Độ bao phủ:",
    round(
        do_bao_phu * 100,
        2
    ),
    "%"
)

print(
    "Điểm F1:",
    round(
        diem_f1,
        4
    )
)