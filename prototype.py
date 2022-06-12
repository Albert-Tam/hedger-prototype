import streamlit as st
from currency_converter import CurrencyConverter
from datetime import datetime


c = CurrencyConverter()
st.title("FX Hedging")
currency_list = ['AUD', 'BGN', 'BRL', 'CAD', 'CHF', 'CNY', 'CYP', 'CZK', 'DKK', 'EEK', 'EUR', 'GBP', 'HKD', 'HRK', 'HUF', 'IDR', 'ILS', 'INR', 'ISK', 'JPY', 'KRW', 'LTL', 'LVL', 'MTL', 'MXN', 'MYR', 'NOK', 'NZD', 'PHP', 'PLN', 'ROL', 'RON', 'RUB', 'SEK', 'SGD', 'SIT', 'SKK', 'THB', 'TRL', 'TRY', 'USD', 'ZAR']

transaction_type = st.radio("Type of transaction", ["Payable", "Receivable"])
foreign_currency = st.selectbox(label="Foreign Currency", options=currency_list)
foreign_amount = st.number_input('Enter an amount', min_value=0, step=1)
domestic_currency = st.selectbox(label="Domestic Currency", options=currency_list)
converted = c.convert(foreign_amount, foreign_currency, domestic_currency)
st.write(f"{foreign_amount} {foreign_currency} = {round(converted, 2)} {domestic_currency}")
date = st.date_input("Fixed date", min_value=datetime.today())
hedging_type = st.radio("Type of hedging", ["Forward", "Options"])
submit = st.button("Schedule")
if submit:
    st.write("You've successfully hedged your money!")
