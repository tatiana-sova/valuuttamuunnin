"""
HELPOMPI VAIHTOEHTO

Tee Valuuttamuunnin. Tarvitset ainakin kaksi tekstikenttää (annettu määrä ja tulos) sekä "MUUNNA" napin. 

Yksinkertaisimmassa muodossa muuntaa aina esim. euroista jeneiksi. 

Voit lisätä alasvetovalikon (drop down menu), josta valitset valuutan jota muunnat.
"""
import tkinter as tk 

def muunna():
    teksti = tekstikentta_syota_maara.get()
    valuutta_1 = float(teksti)
    euro = muunna_valuutasta1_euroon(valuutta_1)
    valuutta_2 = muunna_eurosta_valuuttaan2(euro)
    valuutta_2 = round(valuutta_2,2)
    tekstikentta_tulos.delete(0, tk.END)
    tekstikentta_tulos.insert(0, str(valuutta_2))

def muunna_valuutasta1_euroon(valuutta):
    if valinta_1.get() == "EUR":
        euro = valuutta
    elif valinta_1.get() == "RUB":
        euro = valuutta*0.011
    elif valinta_1.get() == "JPY":
        euro = valuutta*0.0054
    elif valinta_1.get() == "USD":
        euro = valuutta*0.85
    elif valinta_1.get() == "CZK":
        euro = valuutta*0.041
    elif valinta_1.get() == "TRY":
        euro = valuutta*0.019
    return euro
    
def muunna_eurosta_valuuttaan2(euro):
    if valinta_2.get() == "EUR":
        valuutta = euro
    elif valinta_2.get() == "RUB":
        valuutta = euro / 0.011
    elif valinta_2.get() == "JPY":
        valuutta = euro / 0.0054
    elif valinta_2.get() == "USD":
        valuutta = euro / 0.85
    elif valinta_2.get() == "CZK":
        valuutta = euro / 0.041
    elif valinta_2.get() == "TRY":
        valuutta = euro / 0.019
    return valuutta

#ikkuna
ikkuna = tk.Tk()
ikkuna.title("Valuuttamuunnin")
ikkuna.geometry("300x400")


#valuutta_1_frame:
valuutta_1_frame = tk.LabelFrame(ikkuna, text="Valuutta 1", width=100, height=50)
valuutta_1_frame.pack(padx=10, pady=5, fill='x')

row_1_frame = tk.Frame(valuutta_1_frame)
row_1_frame.pack()

tekstikentta_syota_maara = tk.Entry(row_1_frame, width=10)
tekstikentta_syota_maara.pack(side=tk.LEFT, padx=5)

valinta_1 = tk.StringVar()
valinta_1.set("EUR")  

menu_1 = tk.OptionMenu(row_1_frame, valinta_1,"EUR","RUB","JPY","USD", "CZK", "TRY")
menu_1.pack(side=tk.LEFT, padx=5)


# nappula MUUNNA:
nappula_muunna = tk.Button(ikkuna, text="MUUNNA", command=muunna) 
nappula_muunna.pack(padx=10, pady=10)


#valuutta_2_frame: 
valuutta_2_frame = tk.LabelFrame(ikkuna, text="Valuutta 2", width=100, height=50)
valuutta_2_frame.pack(padx=10, pady=5, fill='x')

row_2_frame = tk.Frame(valuutta_2_frame)
row_2_frame.pack()

tekstikentta_tulos = tk.Entry(row_2_frame, width=10)
tekstikentta_tulos.pack(side=tk.LEFT, padx=5)

valinta_2 = tk.StringVar()
valinta_2.set("EUR")  

menu_2 = tk.OptionMenu(row_2_frame, valinta_2,"EUR","RUB","JPY","USD", "CZK", "TRY")
menu_2.pack(side=tk.LEFT, padx=5)


ikkuna.mainloop()