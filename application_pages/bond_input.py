
import streamlit as st
import pandas as pd
from datetime import date

def calculate_duration_convexity(bond):
    # Extract bond details
    maturity = bond['Maturity']
    ytm = bond['Yield to Maturity'] / 100  # Convert to decimal
    coupon_rate = bond['Coupon Rate'] / 100  # Convert to decimal
    price = bond['Price']
    face_value = bond['Face Value']
    quantity = bond['Quantity']

    # Number of coupon payments per year (assuming semi-annual)
    n = 2

    # Calculate Macaulay Duration
    cf_times = [(i + 1) for i in range(int(maturity))]
    pv_cf = []
    for t in cf_times[:-1]:
        pv_cf.append(coupon_rate * face_value / (1 + ytm / n)**(t*n))
    pv_cf.append((coupon_rate * face_value + face_value) / (1 + ytm / n)**(maturity*n))

    mac_dur = sum([t * pv_cf[i] for i, t in enumerate(cf_times)]) / price

    # Calculate Modified Duration
    mod_dur = mac_dur / (1 + (ytm / n))

    #Calculate Convexity
    convexity = (1/price) * sum([(t**2 + t) * pv_cf[i] / (1+ytm)**t for i, t in enumerate(cf_times)]) / (1+ytm)**2

    return mac_dur, mod_dur, convexity

def run_bond_input():
    st.header("Enter Bond Details")

    if 'bond_data' not in st.session_state:
        st.session_state['bond_data'] = []

    with st.form(key='bond_form'):
        bond_name = st.text_input("Bond Name/Identifier")
        maturity = st.number_input("Maturity (years)", min_value=1, max_value=50, value=5)
        ytm = st.number_input("Yield to Maturity (%)", min_value=0.0, max_value=20.0, value=5.0)
        coupon_rate = st.number_input("Coupon Rate (%)", min_value=0.0, max_value=20.0, value=5.0)
        price = st.number_input("Price", min_value=0.0, value=100.0)
        face_value = st.number_input("Face Value", min_value=0.0, value=1000.0)
        quantity = st.number_input("Quantity of Bonds", min_value=1, value=1)

        submit_button = st.form_submit_button(label='Add Bond')

    if submit_button:
        bond = {
            'Bond Name': bond_name,
            'Maturity': maturity,
            'Yield to Maturity': ytm,
            'Coupon Rate': coupon_rate,
            'Price': price,
            'Face Value': face_value,
            'Quantity': quantity
        }
        st.session_state['bond_data'].append(bond)

    if st.session_state['bond_data']:
        df = pd.DataFrame(st.session_state['bond_data'])
        # Calculate metrics
        df[['Macaulay Duration', 'Modified Duration', 'Convexity']] = df.apply(calculate_duration_convexity, axis=1, result_type='expand')
        st.dataframe(df)
    else:
        st.info("No bonds added yet. Please enter bond details and click 'Add Bond'.")

if __name__ == "__main__":
    run_bond_input()
