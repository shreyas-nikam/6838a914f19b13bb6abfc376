
import streamlit as st
import pandas as pd
import plotly.express as px

def run_yield_curve_simulation():
    st.header("Yield Curve Simulation")

    if 'bond_data' not in st.session_state or not st.session_state['bond_data']:
        st.info("No bond data available. Please add bonds on the 'Bond Input' page.")
        return

    df = pd.DataFrame(st.session_state['bond_data'])
    # Calculate metrics
    df[['Macaulay Duration', 'Modified Duration', 'Convexity']] = df.apply(calculate_duration_convexity, axis=1, result_type='expand')

    # Simulate yield curve shift
    yield_shift = st.slider("Yield Curve Shift (%)", min_value=-5.0, max_value=5.0, value=0.0, step=0.1)
    yield_shift /= 100  # Convert to decimal

    # Recalculate bond prices based on the yield curve shift
    df['New Price'] = df.apply(lambda bond: calculate_new_price(bond, yield_shift), axis=1)

    # Calculate market value for each bond
    df['New Market Value'] = df['New Price'] * df['Quantity']

    # Calculate total market value of the portfolio
    total_market_value = df['New Market Value'].sum()

    # Calculate weights
    df['New Weight'] = df['New Market Value'] / total_market_value

    # Calculate weighted duration and convexity
    weighted_duration = (df['New Weight'] * df['Modified Duration']).sum()
    weighted_convexity = (df['New Weight'] * df['Convexity']).sum()


    st.subheader("Portfolio Aggregates (After Yield Shift)")
    st.metric(label="Weighted Average Duration", value=f"{weighted_duration:.2f}")
    st.metric(label="Weighted Average Convexity", value=f"{weighted_convexity:.2f}")

    st.subheader("Bond Data (After Yield Shift)")
    st.dataframe(df)

    # Price Change Visualization
    fig_price_change = px.bar(df, x='Bond Name', y=['Price', 'New Price'],
                             title='Bond Price Change After Yield Shift',
                             labels={'value': 'Price', 'variable': 'Price Type'})
    st.plotly_chart(fig_price_change, use_container_width=True)


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

def calculate_new_price(bond, yield_shift):
    maturity = bond['Maturity']
    ytm = (bond['Yield to Maturity'] / 100) + yield_shift  # Convert to decimal and apply shift
    coupon_rate = bond['Coupon Rate'] / 100  # Convert to decimal
    face_value = bond['Face Value']

    # Number of coupon payments per year (assuming semi-annual)
    n = 2

    # Discount each cash flow and sum them up
    price = 0.0
    for t in range(1, int(maturity) + 1):
        if t < maturity:
            price += coupon_rate * face_value / (1 + ytm / n)**(t*n)
        else:
            price += (coupon_rate * face_value + face_value) / (1 + ytm / n)**(maturity*n)
    return price


if __name__ == "__main__":
    run_yield_curve_simulation()
