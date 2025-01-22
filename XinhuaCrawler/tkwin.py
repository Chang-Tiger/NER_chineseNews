import tkinter as tk

def on_button_click(entry, root, result_var):
    input_text = entry.get()
    root.destroy()
    result_var.set(input_text)

def showWindow():
    root = tk.Tk()
    root.title("your text")

    result_var = tk.StringVar()

    label = tk.Label(root, text="Please enter your keyword to XinhuaNet:")
    label.pack(pady=10)

    # 創建一個文字輸入框
    entry = tk.Entry(root, width=40)
    entry.pack(pady=10)

    # create button to invoke on_button_click()
    button = tk.Button(root, text="Confirm", command=lambda: on_button_click(entry, root, result_var))
    button.pack(pady=10)

    root.mainloop()

    return result_var.get()


# input_text = showWindow()
# print(f"input: {input_text}")
