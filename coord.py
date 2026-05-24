import tkinter as tk

root = tk.Tk()
root.attributes('-fullscreen', True)
root.attributes('-topmost', True)
root.attributes('-transparentcolor', 'white')
root.config(bg='white')

canvas = tk.Canvas(root, bg='white', highlightthickness=0)
canvas.pack(fill='both', expand=True)

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
canvas.create_line(0, h//2, w, h//2, fill='red')
canvas.create_line(w//2, 0, w//2, h, fill='red')

print("Program is working now...")
root.mainloop()