from hrm_package.view import display_records as view_board
from hrm_package.check import clock_in as check_in_emp, clock_out as check_out_emp
from hrm_package.calc import evaluate_flex_time as evaluate_shifts

attendance_book = [
    {"id": "NV01", "name": "Nguyễn Văn A", "times": ("08:30", "17:30")},
    {"id": "NV02", "name": "Trần Thị B", "times": ("09:30", None)}, 
    {"id": "NV03", "name": "Lê Văn C", "times": ("10:15", "19:15")}
]

while True:
    print("=== HỆ THỐNG CHẤM CÔNG  ===")
    print("1. Xem bảng chấm công ngày")
    print("2. Chấm công Vào (Clock-in)")
    print("3. Chấm công Ra (Clock-out)")
    print("4. Đánh giá vi phạm")
    print("5. Thoát chương trình")
    
    choice = input("Chọn chức năng (1-5): ").strip()
    
    match choice:
        case "1":
            view_board(attendance_book)
        case "2":
            check_in_emp(attendance_book)
        case "3":
            check_out_emp(attendance_book)
        case "4":
            evaluate_shifts(attendance_book)
        case "5":
            print("Tạm biệt! Hệ thống chấm công đóng cửa.")
            break
        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại số từ 1 đến 5!")
