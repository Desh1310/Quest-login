from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(
  r"/home/runner/Tkinter-Designer/result/build1/assets/frame0"
)


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("526x364")
window.configure(bg = "#090909")


canvas = Canvas(
    window,
    bg = "#090909",
    height = 364,
    width = 526,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    526.0,
    364.0,
    fill="#FFFFFF",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    315.0,
    313.9999977350235,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    437.42877197265625,
    303.2634559869766,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    283.6414794921875,
    252.78390729427338,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    213.94384765625,
    253.70566022396088,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    223.0,
    350.9999977350235,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    405.0,
    172.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    306.0,
    194.0000022649765,
    image=image_image_7
)

canvas.create_text(
    368.0,
    40.0,
    anchor="nw",
    text="Login",
    fill="#FFFFFF",
    font=("JockeyOne Regular", 32 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    405.0,
    129.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#C6C5C5",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=338.5,
    y=115.0,
    width=133.0,
    height=27.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    405.0,
    188.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#C6C5C5",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=338.5,
    y=174.0,
    width=133.0,
    height=27.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    405.0,
    247.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#C6C5C5",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=338.5,
    y=233.0,
    width=133.0,
    height=27.0
)

canvas.create_text(
    340.0,
    97.0,
    anchor="nw",
    text="Username",
    fill="#FFFFFF",
    font=("JockeyOne Regular", 14 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png")
    file=relative_to_assets("buttonhover.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=368.0,
    y=281.0,
    width=74.0,
    height=23.0
)

canvas.create_text(
    339.0,
    157.0,
    anchor="nw",
    text="Email",
    fill="#FFFFFF",
    font=("JockeyOne Regular", 14 * -1)
)

canvas.create_text(
    340.0,
    212.0,
    anchor="nw",
    text="Password",
    fill="#FFFFFF",
    font=("Product Sans Regular", 14 * -1)
)
window.resizable(False, False)
window.mainloop()
