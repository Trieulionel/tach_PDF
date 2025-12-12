import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfReader, PdfWriter

def chon_file_pdf():
    duong_dan = filedialog.askopenfilename(
        title="Chọn file PDF cần tách",
        filetypes=[("PDF files", "*.pdf")]
    )
    if duong_dan:
        entry_file.delete(0, tk.END)
        entry_file.insert(0, duong_dan)

def tach_pdf():
    duong_dan_pdf = entry_file.get()
    if not duong_dan_pdf or not os.path.exists(duong_dan_pdf):
        messagebox.showerror("Lỗi", "Vui lòng chọn file PDF hợp lệ!")
        return

    thu_muc_luu = filedialog.askdirectory(title="Chọn thư mục lưu các file PDF tách ra")
    if not thu_muc_luu:
        return

    try:
        pdf = PdfReader(duong_dan_pdf)
        tong_trang = len(pdf.pages)

        for i in range(tong_trang):
            writer = PdfWriter()
            writer.add_page(pdf.pages[i])

            ten_file_moi = f"page_{i+1}.pdf"
            duong_dan_moi = os.path.join(thu_muc_luu, ten_file_moi)

            with open(duong_dan_moi, "wb") as output_pdf:
                writer.write(output_pdf)

        messagebox.showinfo("Hoàn tất", f"Đã tách {tong_trang} trang thành các file riêng lẻ!")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể tách file PDF.\nChi tiết: {e}")

# -----------------------------
# GIAO DIỆN CHÍNH
# -----------------------------
root = tk.Tk()
root.title("Tách PDF thành các file riêng lẻ")
root.geometry("500x200")
root.resizable(False, False)

label_file = tk.Label(root, text="Chọn file PDF:")
label_file.pack(pady=10)

frame_file = tk.Frame(root)
frame_file.pack()

entry_file = tk.Entry(frame_file, width=50)
entry_file.pack(side=tk.LEFT, padx=5)

btn_chon = tk.Button(frame_file, text="Duyệt...", command=chon_file_pdf)
btn_chon.pack(side=tk.LEFT)

btn_tach = tk.Button(root, text="Tách PDF", width=20, bg="#4CAF50", fg="white", command=tach_pdf)
btn_tach.pack(pady=20)

root.mainloop()
