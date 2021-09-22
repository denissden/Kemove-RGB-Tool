from tkinter import *
from tkinter import Frame as TkFrame
from tkinter import filedialog
from keyboard_image import KeyboardImage
from functions import *
from map import Map
from export import *

WIDTH, HEIGHT = 850, 400
IMAGE = "images/gradient.jpg"


class MainWindow(TkFrame):
    def __init__(self, root):
        self.root = root
        super().__init__()
        self.filename = None

        self.canvas = Canvas(root, width=WIDTH, height=HEIGHT - 100)
        self.map = Map(KEY_MAP, (WIDTH, HEIGHT - 100))
        self.image = KeyboardImage(IMAGE)
        self.keys_list = []
        self.canvas.pack()

        self.init_window()

    def init_window(self):
        self.master.title("Keyboard Lighting Tool")

        # MENU
        self.init_menu()

        # KEYBOARD
        keys_list = []
        for i in range(len(self.map)):
            color = rgb_to_hex(self.image[i])
            k = self.canvas.create_rectangle(self.map[i], fill=color)
            keys_list.append(k)
        self.keys_list = keys_list

        # CONTRAST
        self.constrast_slider = Scale(self.root,
                                      from_=0, to=300,
                                      orient=HORIZONTAL,
                                      length=200,
                                      label="Contrast",
                                      command=self.change_constrast)
        self.constrast_slider.set(100)
        self.constrast_slider.pack(side=LEFT)

        # HUE
        self.hue_slider = Scale(self.root,
                                      from_=0, to=360,
                                      orient=HORIZONTAL,
                                      length=200,
                                      label="Hue",
                                      command=self.change_hue)
        self.hue_slider.set(0)
        self.hue_slider.pack(side=LEFT)

    def init_menu(self):
        # MENU
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # FILE
        file = Menu(menu)
        file.add_command(label="Open", command=self.open_image)
        file.add_command(label="Export", command=self.export_file)
        file.add_command(label="Exit", command=self.exit_program)
        menu.add_cascade(label="File", menu=file)

    def change_constrast(self, value):
        factor = self.constrast_slider.get()
        self.image.set_contrast(factor / 100)
        self.update_keyboard()

    def change_hue(self, value):
        self.image.set_hue(value)
        self.update_keyboard()

    def update_keyboard(self):
        for i in range(len(self.image)):
            color = rgb_to_hex(self.image[i])
            self.canvas.itemconfig(self.keys_list[i], fill=color)

    def exit_program(self):
        exit(0)

    def open_image(self):
        self.filename = filedialog.askopenfilename(initialdir="/",
                                                        title="Select file",
                                                        filetypes=(
                                                            ("jpeg files", "*.jpg"),
                                                            ("png files", "*.png"),
                                                            ("all files", "*.*")
                                                        ))
        self.image = KeyboardImage(self.filename)
        self.update_keyboard()

    def export_file(self):
        save_file = filedialog.asksaveasfilename(initialdir="/",
                                                 title="Select file",
                                                 filetypes=(
                                                    ("APEX Color Profile", "*.Advanced"),
                                                    ("all files", "*.*")
                                                    ))
        export_advanced(save_file, self.image)


if __name__ == '__main__':
    app = Tk()
    app.geometry(f"{WIDTH}x{HEIGHT}")
    window = MainWindow(app)
    app.mainloop()
