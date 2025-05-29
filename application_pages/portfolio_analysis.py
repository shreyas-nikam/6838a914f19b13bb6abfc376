
import streamlit as st
import pandas as pd
import plotly.express as px

def run_portfolio_analysis():
    st.header("Portfolio Analysis")

    if 'bond_data' not in st.session_state or not st.session_state['bond_data']:
        st.info("No bond data available. Please add bonds on the 'Bond Input' page.")
        return

    df = pd.DataFrame(st.session_state['bond_data'])
    # Calculate metrics
    df[['Macaulay Duration', 'Modified Duration', 'Convexity']] = df.apply(calculate_duration_convexity, axis=1, result_type='expand')

    # Calculate market value for each bond
    df['Market Value'] = df['Price'] * df['Quantity']

    # Calculate total market value of the portfolio
    total_market_value = df['Market Value'].sum()

    # Calculate weights
    df['Weight'] = df['Market Value'] / total_market_value

    # Calculate weighted duration and convexity
    weighted_duration = (df['Weight'] * df['Modified Duration']).sum()
    weighted_convexity = (df['Weight'] * df['Convexity']).sum()

    st.subheader("Portfolio Aggregates")
    st.metric(label="Weighted Average Duration", value=f"{weighted_duration:.2f}")
    st.metric(label="Weighted Average Convexity", value=f"{weighted_convexity:.2f}")

    st.subheader("Bond Contributions")
    df['Contribution to Duration'] = df['Weight'] * df['Modified Duration']
    df['Contribution to Convexity'] = df['Weight'] * df['Convexity']
    st.dataframe(df)

    # --- Charts ---
    st.subheader("Visualizations")

    # Contribution to Duration Chart
    fig_duration = px.bar(df, x='Bond Name', y='Contribution to Duration',
                         title='Contribution to Portfolio Duration by Bond',
                         labels={'Contribution to Duration': 'Contribution to Duration'})
    st.plotly_chart(fig_duration, use_container_width=True)

    # Contribution to Convexity Chart
    fig_convexity = px.bar(df, x='Bond Name', y='Contribution to Convexity',
                          title='Contribution to Portfolio Convexity by Bond',
                          labels={'Contribution to Convexity': 'Contribution to Convexity'})
    st.plotly_chart(fig_convexity, use_container_width=True)


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

if __name__ == "__main__":
    run_portfolio_analysis()
