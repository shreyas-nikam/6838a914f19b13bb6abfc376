id: 6838a914f19b13bb6abfc376_documentation
summary: s Documentation
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# Bond Portfolio Duration & Convexity Analyzer Codelab

This codelab guides you through a Streamlit application designed for analyzing the interest rate risk of bond portfolios. Understanding duration and convexity is crucial for fixed-income portfolio management, as these metrics help quantify a bond's sensitivity to changes in interest rates. This application provides a user-friendly interface to input bond characteristics, calculate key risk metrics, analyze portfolio-level exposures, and simulate the impact of yield curve shifts.

This codelab will cover the following:

*   Understanding the core concepts of Macaulay Duration, Modified Duration, and Convexity.
*   Navigating the application's user interface built with Streamlit.
*   Implementing bond data input and storage using Streamlit's session state.
*   Performing portfolio analysis to calculate weighted average duration and convexity.
*   Visualizing bond contributions to portfolio risk using Plotly.
*   Simulating the impact of yield curve shifts on bond prices and portfolio value.

## Setting up the Environment
Duration: 00:05

Before diving into the application, ensure you have Python installed along with the necessary libraries. It's recommended to use a virtual environment to manage dependencies.

1.  Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

2.  Install the required packages:

    ```bash
    pip install streamlit pandas plotly
    ```

## Understanding the Application Structure
Duration: 00:10

The application consists of the following files:

*   `app.py`: The main entry point of the Streamlit application. It defines the overall layout, navigation, and calls the functions for each page.
*   `application_pages/bond_input.py`: Contains the logic for inputting bond details and calculating individual bond metrics.
*   `application_pages/portfolio_analysis.py`: Implements portfolio-level calculations and visualizations.
*   `application_pages/yield_curve_simulation.py`: Provides the functionality to simulate yield curve shifts and their impact on the portfolio.

The `app.py` file uses a Streamlit `selectbox` in the sidebar to navigate between the three main sections: "Bond Input", "Portfolio Analysis", and "Yield Curve Simulation".  Each selection calls a corresponding function from the `application_pages` directory.

## Running the Application
Duration: 00:02

To start the application, navigate to the directory containing `app.py` in your terminal and run:

```bash
streamlit run app.py
```

This command will launch the Streamlit application in your web browser.

## Exploring the "Bond Input" Page
Duration: 00:15

The "Bond Input" page (`application_pages/bond_input.py`) allows you to enter the details of individual bonds.

1.  **User Interface:** The page features a Streamlit form with input fields for:
    *   Bond Name/Identifier
    *   Maturity (years)
    *   Yield to Maturity (%)
    *   Coupon Rate (%)
    *   Price
    *   Face Value
    *   Quantity of Bonds

2.  **Data Storage:** The entered bond data is stored in Streamlit's session state (`st.session_state['bond_data']`). This allows the data to persist across different pages of the application.

3.  **Calculations:** When you click the "Add Bond" button, the application calculates Macaulay Duration, Modified Duration, and Convexity for the entered bond. These calculations are performed by the `calculate_duration_convexity` function.

    ```python
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
    ```

4.  **Display:** The entered bond data, along with the calculated metrics, is displayed in a Pandas DataFrame using `st.dataframe(df)`.

<aside class="positive">
The session state is <b>crucial</b> for maintaining data across different pages in Streamlit.  Without it, the data entered on the "Bond Input" page would not be available on the other pages.
</aside>

## Analyzing the Portfolio
Duration: 00:20

The "Portfolio Analysis" page (`application_pages/portfolio_analysis.py`) provides a comprehensive overview of the bond portfolio's risk characteristics.

1.  **Data Retrieval:**  The page retrieves the bond data from `st.session_state['bond_data']`. If no data is available, it displays an informative message.

2.  **Portfolio Aggregates:**  The page calculates the following portfolio-level metrics:

    *   **Market Value:**  Calculated for each bond as `Price * Quantity`.
    *   **Weight:** Calculated for each bond as `Market Value / Total Market Value`.
    *   **Weighted Average Duration:** Calculated as the sum of `Weight * Modified Duration` for all bonds.
    *   **Weighted Average Convexity:** Calculated as the sum of `Weight * Convexity` for all bonds.

    These aggregates are displayed using Streamlit's `st.metric` function, providing a clear summary of the portfolio's overall risk profile.

3.  **Bond Contributions:** The page calculates and displays each bond's contribution to the portfolio's duration and convexity:

    *   **Contribution to Duration:** Calculated as `Weight * Modified Duration`.
    *   **Contribution to Convexity:** Calculated as `Weight * Convexity`.

    These contributions are presented in a Pandas DataFrame, allowing you to identify the bonds that have the most significant impact on the portfolio's interest rate sensitivity.

4.  **Visualizations:**  The page includes bar charts visualizing the contribution of each bond to the portfolio's duration and convexity. These charts are generated using Plotly Express (`plotly.express as px`) and displayed using `st.plotly_chart`.

    ```python
    fig_duration = px.bar(df, x='Bond Name', y='Contribution to Duration',
                         title='Contribution to Portfolio Duration by Bond',
                         labels={'Contribution to Duration': 'Contribution to Duration'})
    st.plotly_chart(fig_duration, use_container_width=True)

    fig_convexity = px.bar(df, x='Bond Name', y='Contribution to Convexity',
                          title='Contribution to Portfolio Convexity by Bond',
                          labels={'Contribution to Convexity': 'Contribution to Convexity'})
    st.plotly_chart(fig_convexity, use_container_width=True)
    ```

<aside class="positive">
The use of <b>visualizations</b> significantly enhances the understanding of portfolio risk.  The bar charts provide a clear and intuitive way to compare the contributions of different bonds to the overall portfolio duration and convexity.
</aside>

## Simulating Yield Curve Shifts
Duration: 00:20

The "Yield Curve Simulation" page (`application_pages/yield_curve_simulation.py`) allows you to simulate the impact of parallel yield curve shifts on the bond portfolio.

1.  **Data Retrieval:** The page retrieves bond data from the session state like the "Portfolio Analysis" page.

2.  **Yield Shift Input:** A Streamlit slider (`st.slider`) allows you to specify the magnitude of the yield curve shift in percentage points.

    ```python
    yield_shift = st.slider("Yield Curve Shift (%)", min_value=-5.0, max_value=5.0, value=0.0, step=0.1)
    yield_shift /= 100  # Convert to decimal
    ```

3.  **Price Recalculation:** For each bond, the application recalculates the price based on the shifted yield to maturity using the `calculate_new_price` function.  This function discounts all future cash flows using the new yield.

    ```python
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
    ```

4.  **Portfolio Aggregates (After Shift):**  The page then recalculates the portfolio aggregates (market value, weights, weighted duration, and weighted convexity) using the new bond prices.  These new values are displayed using `st.metric`.

5.  **Display:**  The page displays the original and new bond prices, along with the updated portfolio metrics.

6.  **Visualization:** A bar chart visualizes the change in bond prices before and after the yield curve shift.

    ```python
    fig_price_change = px.bar(df, x='Bond Name', y=['Price', 'New Price'],
                             title='Bond Price Change After Yield Shift',
                             labels={'value': 'Price', 'variable': 'Price Type'})
    st.plotly_chart(fig_price_change, use_container_width=True)
    ```

## Code Improvements and Considerations
Duration: 00:10

While the provided application offers a good starting point, several improvements and considerations can be made:

*   **Yield Curve Modeling:** The simulation assumes a parallel yield curve shift. More sophisticated models could incorporate non-parallel shifts or changes in the yield curve's shape (e.g., steepening, flattening).
*   **Data Validation:**  Adding input validation to the "Bond Input" page can prevent errors and ensure data quality.
*   **Error Handling:**  Implementing proper error handling (e.g., `try-except` blocks) can make the application more robust.
*   **Advanced Risk Measures:**  Consider incorporating other risk measures, such as Value at Risk (VaR) or Expected Shortfall, for a more comprehensive risk assessment.
*   **User Interface Enhancements:**  Streamlit offers numerous options for customizing the user interface and improving the user experience.

## Conclusion
Duration: 00:03

This codelab provided a detailed walkthrough of a Streamlit application for analyzing bond portfolio duration and convexity. You learned how to input bond data, calculate key risk metrics, analyze portfolio-level exposures, and simulate the impact of yield curve shifts.  By understanding the concepts and code presented in this codelab, you can develop more sophisticated fixed-income portfolio management tools.
