def clock_in(records):
    print("\n--- CHẤM CÔNG VÀO (CLOCK-IN) ---")
    emp_id = input("Nhập mã nhân viên: ").strip().upper()
    if emp_id == "":
        print("Lỗi: Mã nhân viên không được để trống!")
        return
        
    for record in records:
        if record["id"] == emp_id:
            print(f"Lỗi: Mã nhân viên {emp_id} đã tồn tại trong hệ thống!")
            return
            
    name = input("Nhập tên nhân viên: ").strip().title()
    if name == "":
        print("Lỗi: Tên nhân viên không được để trống!")
        return
        
    time_in = input("Nhập giờ vào (HH:MM): ").strip()
    if len(time_in) != 5 or ":" not in time_in:
        print("Lỗi: Định dạng giờ vào phải là HH:MM!")
        return
        
    new_record = {
        "id": emp_id,
        "name": name,
        "times": (time_in, None)
    }
    records.append(new_record)
    print(f"Thành công: Đã ghi nhận {emp_id} chấm công vào lúc {time_in}!")

def clock_out(records):
    print("\n--- CHẤM CÔNG RA (CLOCK-OUT) ---")
    emp_id = input("Nhập mã nhân viên: ").strip().upper()
    if emp_id == "":
        print("Lỗi: Mã nhân viên không được để trống!")
        return
        
    target_record = None
    for record in records:
        if record["id"] == emp_id:
            target_record = record
            break
            
    if target_record is None:
        print(f"Lỗi: Không tìm thấy nhân viên mang mã {emp_id}!")
        return
        
    time_out = input("Nhập giờ ra (HH:MM): ").strip()
    if len(time_out) != 5 or ":" not in time_out:
        print("Lỗi: Định dạng giờ ra phải là HH:MM!")
        return
        
    time_in_old = target_record["times"][0]
    new_tuple = (time_in_old, time_out)
    target_record["times"] = new_tuple
    print(f"Thành công: Đã ghi nhận {emp_id} chấm công ra lúc {time_out}!")