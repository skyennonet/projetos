from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

def calcular_volume():
    raio = float(all_values)
    volume_esfera = (4/3) * 3.14159 * raio**3
    volume_cubo = raio**3

    label_esfera.config(text=f"o volume da esfera é: {formatar_numero(volume_esfera, 'metro cubico')}")
    label_cubo.config(text=f"O volume do cubo é: {formatar_numero(volume_cubo, 'metro cúbico')}")


def formatar_numero(numero, unidade):
    return "{:,.2f}".format(numero,unidade)

janela = Tk()
janela.title('')
janela.geometry('400x200')
janela.configure(bg=fundo)

style = ttk.Style(janela)
style.theme_use("clam")

frame_logo = Frame(janela, width=400, height=56, bg=fundo, pady=0, padx=0, relief="flat")
frame_logo.grid(row=1, column=0, sticky="nw")

app_lg = Image.open('logo.png')
app_lg = app_lg.resize((40,40))
app_lg = ImageTk.PhotoImage(app_lg)
app_logo = Label(frame_logo, image=app_lg, text="calculadora de volume", width=850, compound="left", anchor="nw", font=('Verdana 15'), bg=fundo, fg=co2)
app_logo.place(x=5, y=0)

all_values = ""
value_text = StringVar()

def handle_key(event):
    global all_values
    if event.char.isdigit() or event.char == ".":
        all_values = all_values = str(event.char)
        entry_raio.delete(0, END)
        entry_raio.insert(0, all_values)
        calcular_volume()

    if event.keysym =="BackSpace":
        all_values = all_values[:-1]
        entry_raio.delete(0, END)
        entry_raio.insert(0, all_values)
        calcular_volume()

entry_raio = ttk.Entry(frame_resultado, textvariable=value_text, width=10, font=('Tahoma 25 bold'), justify='center')
entry_raio.place(x=10, y=0)
entry_raio.bind("<KeyRelease>", handle_key)

label_esfera = Label(frame_resultado, text='',width=850, compound="left", anchor="nw", font=('calibri 12'), bg=fundo, fg=co2)
label_esfera.place(x=10, y=70)

label_cubo = Label(frame_resultado, text='', width=850, compound="left", anchor="nw", font('calibri 12'), bg=fundo, fg=c02)
label_cubo.place(x=10, y=90)


janela.mainloop()



