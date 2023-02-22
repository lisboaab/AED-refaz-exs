# nao funciona

import os
from tkinter import *
from tkinter import filedialog


master = Tk()
master.title("Gestor de Fotos")

# -----------FUNCOES-------------
def select_image(self):
        # abre o FileDialog para seleção da imagem
        file_path = filedialog.askopenfilename(filetypes=[("Imagens", "*.png;*.gif")])

        # adiciona o caminho do arquivo selecionado à Listbox
        if file_path:
            listbox.insert(END, os.path.basename(file_path))

            # abre a imagem e adiciona à lista de imagens
            image = PhotoImage(file=file_path)
            images.append(image)

            # atualiza a imagem atual
            current_image_index = len(images) - 1

            # exibe a imagem atual
            show_image()

def remove_image(self):
        # remove o item selecionado da Listbox
        selection = self.listbox.curselection()
        if selection:
            index = selection[0]
            self.listbox.delete(index)

            # remove a imagem da lista de imagens
            self.images.pop(index)

            # atualiza a imagem atual
            if self.current_image_index >= len(self.images):
                self.current_image_index = len(self.images) - 1

            # exibe a imagem atual
            self.show_image()

def first_image(self):
        self.current_image_index = 0
        self.show_image()

def prev_image(self):
        if self.current_image_index > 0:
            self.current_image_index -= 1
            self.show_image()

def next_image(self):
        if self.current_image_index < len(self.images) - 1:
            self.current_image_index += 1
            self.show_image()

def last_image(self):
        self.current_image_index = len(self.images) - 1
        self.show_image()

def show_image(self):
        # exibe a imagem atual na canvas
        self.canvas.delete("all")
        if self.images:
            self.canvas.create




#--------- GUI------------



images = []  # lista de imagens
current_image_index = 0  # índice da imagem atual

# criação dos widgets
listbox = Listbox(master)
listbox.pack(padx=10, pady=10)

select_button = Button(master, text="Selecionar Imagem", command=select_image)
select_button.pack(side=LEFT, padx=10)

remove_button = Button(master, text="Remover Imagem", command=remove_image)
remove_button.pack(side=LEFT, padx=10)

first_button = Button(master, text="<<", command=first_image)
first_button.pack(side=LEFT, padx=10)

prev_button = Button(master, text="<", command=prev_image)
prev_button.pack(side=LEFT, padx=10)

next_button = Button(master, text=">", command=next_image)
next_button.pack(side=LEFT, padx=10)

last_button = Button(master, text=">>", command=last_image)
last_button.pack(side=LEFT, padx=10)

# criação da canvas para exibição das imagens
canvas = Canvas(master, width=500, height=500)
canvas.pack(padx=10, pady=10)

