def process_rikkeimart_order(item_status, customer_response):
    try:
        if item_status == "available":
            return "Sản phẩm còn hàng. Tiếp tục mua và xử lý đơn hàng."
        if item_status == "out_of_stock":
            print("Sản phẩm đã hết hàng.")
            print("Tài xế đề xuất sản phẩm thay thế tương đương.")
            print("Đã gửi thông báo đến khách hàng.")
            if customer_response == "accept":
                return "Khách hàng đồng ý. Thay thế sản phẩm và tiếp tục đơn hàng."
            if customer_response == "reject":
                return "Khách hàng từ chối. Xử lý đơn hàng theo chính sách."
            if customer_response == "timeout":
                return "Timeout sau 3 phút. Thực hiện Auto-substitute hoặc Auto-cancel để giải phóng tài xế."
            return "Phản hồi khách hàng không hợp lệ."
        return "Trạng thái sản phẩm không hợp lệ."
    except Exception:
        return "Có lỗi xảy ra nhưng hệ thống không bị crash."

print(process_rikkeimart_order("available", None))
print(process_rikkeimart_order("out_of_stock", "accept"))
print(process_rikkeimart_order("out_of_stock", "reject"))
print(process_rikkeimart_order("out_of_stock", "timeout"))
print(process_rikkeimart_order("unknown", None))
