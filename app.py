
import streamlit as st

st.set_page_config(page_title="Bond Portfolio Analyzer", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("Bond Portfolio Duration & Convexity Analyzer")
st.divider()

st.markdown(""
"""
Welcome to the Bond Portfolio Duration & Convexity Analyzer!

This application allows you to analyze and compare the interest rate risk of different bond portfolios. 
You can input bond characteristics such as maturity, yield to maturity, coupon rate, price, face value, and quantity 
to calculate key risk metrics like Macaulay Duration, Modified Duration, and Convexity.

Use the navigation menu on the left to explore the different pages of the application.
"""
)

# Your code starts here
page = st.sidebar.selectbox(label="Navigation", options=["Bond Input", "Portfolio Analysis", "Yield Curve Simulation"])

if page == "Bond Input":
    from application_pages.bond_input import run_bond_input
    run_bond_input()
elif page == "Portfolio Analysis":
    from application_pages.portfolio_analysis import run_portfolio_analysis
    run_portfolio_analysis()
elif page == "Yield Curve Simulation":
    from application_pages.yield_curve_simulation import run_yield_curve_simulation
    run_yield_curve_simulation()
# Your code ends

st.divider()
st.write("© 2025 QuantUniversity. All Rights Reserved.")
st.caption("The purpose of this demonstration is solely for educational use and illustration. "
           "Any reproduction of this demonstration "
           "requires prior written consent from QuantUniversity.")
