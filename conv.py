import streamlit as st

def convert_units(value, from_unit, to_unit):
    conversions = {
        'meters': {'kilometers': value / 1000},
        'kilometers': {'meters': value * 1000},
        'miles': {'meters': value / 0.000621371, 'kilometers': value / 0.621371},
        'feet': {'meters': value / 3.28084, 'kilometers': value / 3280.84, 'miles': value / 5280}
    }
    return conversions.get(from_unit, {}).get(to_unit, 'Invalid conversion')

st.title("Unit Converter")

value = st.number_input("Enter value:", min_value=0.0, step=0.1)
from_unit = st.selectbox("From unit:", ['meters', 'kilometers', 'miles', 'feet'])
to_unit = st.selectbox("To unit:", ['meters', 'kilometers', 'feet'])

if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit)
    st.write(f"{value} {from_unit} = {result} {to_unit}")
