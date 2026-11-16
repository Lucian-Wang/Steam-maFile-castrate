import os
import json
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

COPYRIGHT = "灯火通明（济宁）网络有限公司"

def is_mafile(filename):
    return filename.endswith('.maFile') or filename.endswith('.json')

def strip_identity_secret_and_save(src_filepath, src_root, dst_root, output_func):
    rel_path = os.path.relpath(src_filepath, src_root)
    dst_filepath = os.path.join(dst_root, rel_path)
    os.makedirs(os.path.dirname(dst_filepath), exist_ok=True)

    try:
        with open(src_filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        output_func(f"[!] 跳过无法解析的文件: {src_filepath}\n错误: {e}\n")
        return

    if 'identity_secret' in data and data['identity_secret']:
        data['identity_secret'] = ""
        result = f"[+] 阉割 identity_secret 成功: {src_filepath}\n"
    else:
        result = f"[-] 未发现 identity_secret 字段或已为空: {src_filepath}\n"

    try:
        with open(dst_filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        result += f"[√] 已保存阉割文件: {dst_filepath}\n"
    except Exception as e:
        result += f"[!] 写入新文件失败: {dst_filepath}\n错误: {e}\n"
    output_func(result)

def batch_strip(src_dir, dst_dir, output_func):
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if is_mafile(file):
                src_filepath = os.path.join(root, file)
                strip_identity_secret_and_save(src_filepath, src_dir, dst_dir, output_func)
    output_func("批量阉割完成。\n")

class MafileStripperApp:
    def __init__(self, master):
        self.master = master
        master.title("Steam maFile 阉割工具 - 灯火通明")
        master.geometry("700x420")
        master.resizable(False, False)

        self.src_dir = tk.StringVar()
        self.dst_dir = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        frame1 = tk.Frame(self.master)
        frame1.pack(pady=8, padx=10, fill="x")
        label1 = tk.Label(frame1, text="源maFile根目录：")
        label1.pack(side="left")
        entry1 = tk.Entry(frame1, textvariable=self.src_dir, width=50)
        entry1.pack(side="left", padx=5)
        browse_btn1 = tk.Button(frame1, text="浏览", command=self.browse_src)
        browse_btn1.pack(side="left")

        frame2 = tk.Frame(self.master)
        frame2.pack(pady=8, padx=10, fill="x")
        label2 = tk.Label(frame2, text="阉割文件存放目录：")
        label2.pack(side="left")
        entry2 = tk.Entry(frame2, textvariable=self.dst_dir, width=50)
        entry2.pack(side="left", padx=5)
        browse_btn2 = tk.Button(frame2, text="浏览", command=self.browse_dst)
        browse_btn2.pack(side="left")

        strip_btn = tk.Button(self.master, text="批量阉割", command=self.strip_files, bg="#4caf50", fg="white", width=15)
        strip_btn.pack(pady=10)

        self.output_text = scrolledtext.ScrolledText(self.master, width=90, height=15)
        self.output_text.pack(padx=10, fill="both", expand=True)

        copyright_label = tk.Label(self.master, text=f"© {COPYRIGHT}", anchor="e", fg="gray")
        copyright_label.pack(side="bottom", fill="x", pady=3)

    def browse_src(self):
        directory = filedialog.askdirectory(title="选择源maFile目录")
        if directory:
            self.src_dir.set(directory)

    def browse_dst(self):
        directory = filedialog.askdirectory(title="选择阉割文件保存目录")
        if directory:
            self.dst_dir.set(directory)

    def strip_files(self):
        src = self.src_dir.get()
        dst = self.dst_dir.get()
        if not src or not os.path.isdir(src):
            messagebox.showwarning("提示", "请先选择正确的源maFile目录！")
            return
        if not dst or not os.path.isdir(dst):
            messagebox.showwarning("提示", "请先选择正确的阉割文件保存目录！")
            return
        if os.path.abspath(src) == os.path.abspath(dst):
            messagebox.showwarning("提示", "源目录和目标目录不能相同！")
            return
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, f"开始批量阉割：\n源目录：{src}\n保存到：{dst}\n\n")
        def output_func(msg):
            self.output_text.insert("end", msg)
            self.output_text.see("end")
        batch_strip(src, dst, output_func)
        self.output_text.insert("end", "全部完成！（原始文件未被覆盖，新文件已存到指定目录）\n")
        messagebox.showinfo("完成", "批量阉割已完成！新文件已存到指定目录，原文件保持不变。")

if __name__ == '__main__':
    root = tk.Tk()
    app = MafileStripperApp(root)
    root.mainloop()