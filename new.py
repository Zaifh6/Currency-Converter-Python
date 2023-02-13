import tkinter as tk
import requests

def currency_converter(amount, from_currency, to_currency):
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_currency}&from={from_currency}&amount={amount}"
    headers = {
        "apikey": "eJJqOhLvfbkv4xIboNYS031aTz7yz11l"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        converted_amount = data['result']
        return converted_amount
    else:
        print(f'Failed to fetch the exchange rate. Response code: {response.status_code}. Response text: {response.text}')
        return None

class CurrencyConverter(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        self.title("Currency Converter")
        self.geometry("400x400")
        
        self.amount_label = tk.Label(self, text="Enter amount:")
        self.amount_label.pack()
        
        self.amount_entry = tk.Entry(self)
        self.amount_entry.pack()
        
        self.from_currency_label = tk.Label(self, text="Convert from:")
        self.from_currency_label.pack()
        
        self.from_currency_var = tk.StringVar(self)
        self.from_currency_var.set("USD")
        
        self.from_currency_menu = tk.OptionMenu(self, self.from_currency_var, *available_currencies)
        self.from_currency_menu.pack()
        
        self.to_currency_label = tk.Label(self, text="Convert to:")
        self.to_currency_label.pack()
        
        self.to_currency_var = tk.StringVar(self)
        self.to_currency_var.set("EUR")
        
        self.to_currency_menu = tk.OptionMenu(self, self.to_currency_var, *available_currencies)
        self.to_currency_menu.pack()
        
        self.convert_button = tk.Button(self, text="Convert", command=self.convert)
        self.convert_button.pack()
        
        self.result_label = tk.Label(self, text="")
        self.result_label.pack()

    def convert(self):
        amount = float(self.amount_entry.get())
        from_currency = self.from_currency_var.get()
        to_currency = self.to_currency_var.get()
        
        converted_amount = currency_converter(amount, from_currency, to_currency)
        
        if converted_amount:
            self.result_label.config(text=f"{amount} {from_currency} is equivalent to {converted_amount} {to_currency}")
app = CurrencyConverter()
app.mainloop()
