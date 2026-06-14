import datetime

def evaluate_flex_time(records):
    if len(records) == 0:
        print("Không có dữ liệu để đánh giá.")
        return
        
    print("\n--- ĐÁNH GIÁ VI PHẠM (FLEX-TIME) ---")
    limit_time = datetime.datetime.strptime("10:00", "%H:%M")
    
    for record in records:
        emp_id = record["id"]
        time_in_str = record["times"][0]
        time_out_str = record["times"][1]
        
        if time_out_str is None:
            print(f"{emp_id} - Chưa đánh giá: Nhân viên đang trong ca làm việc.")
            continue
            
        try:
            time_in = datetime.datetime.strptime(time_in_str, "%H:%M")
            time_out = datetime.datetime.strptime(time_out_str, "%H:%M")
            
            if time_in > limit_time:
                print(f"{emp_id} - Vi phạm: Đến muộn quá 90 phút.")
            else:
                work_duration = time_out - time_in
                total_seconds = work_duration.total_seconds()
                
                if total_seconds < 32400:
                    print(f"{emp_id} - Vi phạm: Về sớm, chưa hoàn thành đủ 9 tiếng bù giờ.")
                else:
                    print(f"{emp_id} - Hợp lệ: Hoàn thành ca làm việc.")
                    
        except ValueError:
            print(f"{emp_id} - Lỗi: Định dạng chuỗi thời gian trong hệ thống bị sai rác.")