from tabulate import tabulate

def display_records(records):
    if len(records) == 0:
        print("Bảng chấm công hiện đang trống.")
        return
        
    table_data = []
    print("\n--- BẢNG CHẤM CÔNG ---")
    
    for record in records:
        emp_id = record["id"]
        name = record["name"]
        time_in = record["times"][0]
        time_out = record["times"][1]
        
        if time_out is None:
            time_out_display = "[Đang làm việc]"
        else:
            time_out_display = time_out
            
        table_data.append([emp_id, name, time_in, time_out_display])
        
    headers = ["Mã NV", "Tên Nhân Viên", "Giờ Vào", "Giờ Ra"]
    print(tabulate(table_data, headers=headers, tablefmt="orgtbl"))