import pyodbc
import csv
import os

def connect_to_sql_server(server: str, database: str) -> pyodbc.Connection:
    """
    Kết nối đến SQL Server.
    Args:
        server (str): Tên server SQL Server.
        database (str): Tên database cần kết nối.

    Returns:
        pyodbc.Connection: Đối tượng kết nối đến SQL Server.
    """
    conn_str = (
        r'DRIVER={SQL Server};'
        r'SERVER=' + server + ';'
        r'DATABASE=' + database + ';'
        r'Trusted_Connection=yes;'
    )
    try:
        cnxn = pyodbc.connect(conn_str)
        print("Kết nối thành công đến SQL Server.")
        return cnxn
    except pyodbc.Error as ex:
        print(f"Lỗi kết nối SQL Server: {ex}")
        raise

def export_table_to_csv(cursor, table_name: str, output_folder: str = "./"):
    """
    Xuất một bảng SQL Server ra file CSV.
    Args:
        cursor: Đối tượng cursor để thực hiện truy vấn SQL.
        table_name (str): Tên bảng cần xuất.
        output_folder (str): Thư mục để lưu file CSV. Mặc định là thư mục hiện tại.

    Returns:
        None
    """
    try:
        query = f"SELECT * FROM dbo.{table_name}"
        cursor.execute(query)
        column_names = [column[0] for column in cursor.description]
        
        # Đảm bảo thư mục tồn tại
        os.makedirs(output_folder, exist_ok=True)
        
        csv_file_name = os.path.join(output_folder, f"{table_name}.csv")
        with open(csv_file_name, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(column_names)  # Ghi tiêu đề cột
            for row in cursor:
                writer.writerow(row)
        print(f"Đã xuất bảng {table_name} thành file {csv_file_name}")
    except pyodbc.Error as ex:
        print(f"Lỗi khi truy vấn hoặc ghi file CSV cho bảng {table_name}: {ex}")

def export_multiple_tables_to_csv(server: str, database: str, tables: list, output_folder: str = "./"):
    """
    Xuất nhiều bảng SQL Server ra file CSV.
    Args:
        server (str): Tên server SQL Server.
        database (str): Tên database cần kết nối.
        tables (list): Danh sách tên các bảng cần xuất.
        output_folder (str): Thư mục để lưu file CSV. Mặc định là thư mục hiện tại.

    Returns:
        None
    """
    try:
        cnxn = connect_to_sql_server(server, database)
        cursor = cnxn.cursor()
        for table_name in tables:
            export_table_to_csv(cursor, table_name, output_folder)
    finally:
        if cnxn:
            cnxn.close()
            print("Đã đóng kết nối SQL Server.")

def process_csv_file(input_file: str, output_file: str, processing_func):
    """
    Xử lý file CSV theo một hàm xử lý tùy chỉnh.
    Args:
        input_file (str): Đường dẫn file CSV gốc.
        output_file (str): Đường dẫn file CSV sau xử lý.
        processing_func (callable): Hàm xử lý dữ liệu (nhận DataFrame, trả về DataFrame).

    Returns:
        None
    """
    import pandas as pd

    try:
        df = pd.read_csv(input_file)
        processed_df = processing_func(df)
        processed_df.to_csv(output_file, index=False, encoding='utf-8')
        print(f"Đã xử lý và lưu file CSV vào {output_file}")
    except Exception as e:
        print(f"Lỗi khi xử lý file CSV: {e}")

import csv

def txt_to_csv(input_txt_file, output_csv_file, delimiter=','):
    """
    Chuyển đổi file txt thành file csv.

    :param input_txt_file: Đường dẫn đến file txt đầu vào.
    :param output_csv_file: Đường dẫn đến file csv đầu ra.
    :param delimiter: Ký tự phân cách trong file txt. Mặc định là dấu phẩy ','.
    """
    try:
        # Mở file txt để đọc
        with open(input_txt_file, 'r', encoding='utf-8') as txt_file:
            # Đọc tất cả các dòng trong file txt
            lines = txt_file.readlines()

        # Mở file csv để ghi
        with open(output_csv_file, 'w', newline='', encoding='utf-8') as csv_file:
            # Tạo đối tượng writer để ghi dữ liệu vào file csv
            csv_writer = csv.writer(csv_file)

            # Xử lý từng dòng trong file txt
            for line in lines:
                # Loại bỏ ký tự xuống dòng và tách các cột bằng delimiter
                row = line.strip().split(delimiter)
                # Ghi dòng vào file csv
                csv_writer.writerow(row)

        print(f"File '{input_txt_file}' đã được chuyển đổi thành '{output_csv_file}'.")

    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")
# Chuyển từ txt -> sql

import csv

def txt_to_csv(txt_file, csv_file, delimiter=','):
    try:
        # Đọc nội dung từ file txt
        with open(txt_file, 'r', encoding='utf-8') as txt:
            lines = txt.readlines()
        
        # Ghi nội dung vào file csv
        with open(csv_file, 'w', newline='', encoding='utf-8') as csvf:
            writer = csv.writer(csvf, delimiter=',')
            
            for line in lines:
                # Loại bỏ các khoảng trắng thừa và tách thành danh sách
                row = line.strip().split(delimiter)
                writer.writerow(row)
                
        print(f"Đã chuyển đổi {txt_file} thành {csv_file} thành công.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

# Sử dụng hàm
txt_file_path = 'example.txt'  # Đường dẫn file txt
csv_file_path = 'output.csv'   # Đường dẫn file csv
txt_to_csv(txt_file_path, csv_file_path, delimiter=',')
