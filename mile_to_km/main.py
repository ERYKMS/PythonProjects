import tkinter

def calculate_km():
    try:
        miles = float(miles_entry.get())
        km = miles * 1.60934  # 1 mil = 1.60934 kilometre
        km_label.config(text=f"{km:.2f} Km")  # Güncellenen km değerini etikete yazdır
    except ValueError:
        km_label.config(text="Invalid input")

window = tkinter.Tk()
window.minsize(width=150, height=75)

miles_entry = tkinter.Entry()
miles_entry.grid(column=0, row=0)

miles_label = tkinter.Label(text="Mile")
miles_label.grid(column=1, row=0)

km_is_equal_label = tkinter.Label(text="is equal to")
km_is_equal_label.grid(column=0, row=1)

km_label = tkinter.Label(text="0 Km")  # Başlangıçta 0 Km olarak ayarla
km_label.grid(column=1, row=1)

km_unit_label = tkinter.Label(text="Km")  # Km birim etiketi
km_unit_label.grid(column=2, row=1)

calculate_button = tkinter.Button(text="Calculate", command=calculate_km)
calculate_button.grid(column=1, row=2)

window.mainloop()
