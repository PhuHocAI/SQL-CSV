# SQL-CSV Data Handler

## Giới thiệu

**SQL-CSV Data Handler** là một tập hợp các hàm Python mạnh mẽ được thiết kế để **xử lý, chuyển đổi và tương tác dữ liệu** giữa hai định dạng phổ biến: **SQL** và **CSV**. Repository này giúp bạn dễ dàng thực hiện các tác vụ như:

- Xuất dữ liệu từ SQL sang CSV
- Nhập dữ liệu từ CSV vào SQL
- Chuyển đổi qua lại giữa các định dạng
- Xử lý và thao tác dữ liệu nhanh chóng và hiệu quả.

## Tính năng chính

- **Xuất dữ liệu từ SQL sang CSV**:
  - Kết nối đến cơ sở dữ liệu SQL.
  - Chạy câu truy vấn và lưu kết quả vào file CSV.

- **Nhập dữ liệu từ CSV vào SQL**:
  - Đọc dữ liệu từ file CSV.
  - Chèn dữ liệu vào bảng SQL.

- **Xử lý và thao tác dữ liệu**:
  - Tích hợp các hàm để lọc, làm sạch và chuẩn hóa dữ liệu.
  - Hỗ trợ chuyển đổi kiểu dữ liệu khi cần thiết.

- **Tương thích cao**:
  - Hỗ trợ SQLite, MySQL, PostgreSQL và nhiều hệ quản trị cơ sở dữ liệu khác.
  - Làm việc tốt với các file CSV lớn.

## Yêu cầu hệ thống

- Python >= 3.7
- Các thư viện Python cần thiết:
  - `pandas`
  - `pyodbc`

Cài đặt các thư viện bằng lệnh sau:
```bash
pip install pandas pyodbc
