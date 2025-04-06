import tkinter as tk

# Definir a funçôes de conversão

def convert():
    input.value = float(input_entry.get())
    from_unit = from_unit_var.get()
    to_unit = to_unit_var.get()

    # Definir as unidades de conversão
    conversion_rates = [
        ("miles", "kilometers"): 1.60934,
        ("kilometers", "miles"): 0.621371,
        
        ("inches", "centimeters"): 2.54,
        ("centimeters", "inches"): 0.393701,

        ("fahrenheit", "celsius"): lambda f: (f - 32) * 5/9,
        ("celsius", "fahrenheit"): lambda c: c * 9/5 + 32,

        ("pounds", "kilograms"): 0.453592,
        ("kilograms", "pounds"): 2.20462,
    ]

    # Perform the conversion
    result = input_value * conversion_rates[(from_unit, to_unit)]
    result_label.config(text=f"{result} {to_unit}")

# Create the main window
root = tk.Tk()
root.title("Unit Converter")

# Create the widgets
input_label = tk.Label(root, text="Enter the value to convert:")

...