
## Overview

This Streamlit application, titled "Bond Portfolio Duration & Convexity Analyzer," is designed for portfolio managers and fixed-income enthusiasts to analyze and compare the interest rate risk of different bond portfolios. The application allows users to input bond characteristics, view key risk metrics, and understand the impact of individual bonds on the overall portfolio's risk profile.

## Step-by-Step Generation Process

1.  **Initialize the Streamlit App:**
    *   Import necessary libraries (`streamlit`, `pandas`, potentially `numpy`, etc.).
    *   Set the title of the application.
    *   Add a descriptive header or introductory text.

2.  **Create Input Forms for Bond Data:**
    *   Design input widgets for users to define bond characteristics. Key inputs would include:
        *   Bond Name/Identifier (text input)
        *   Maturity (date input or numeric input for years)
        *   Yield to Maturity (numeric input)
        *   Coupon Rate (numeric input)
        *   Price (numeric input)
        *   Face Value (numeric input)
        *   Quantity of Bonds (numeric input)

    *   Use `streamlit.form` to group the input widgets for each bond.
    *   Provide a button within the form to add the bond to the portfolio.

3.  **Store Bond Data:**
    *   Initialize an empty list or Pandas DataFrame to store bond data.
    *   When a user adds a bond via the form, append the bond's data to the list or DataFrame.

4.  **Calculate Bond Metrics:**
    *   Create functions to calculate key bond metrics:
        *   **Macaulay Duration:** This measure represents the weighted average time until a bondholder receives the bond's cash flows.
        *   **Modified Duration:** An estimate of the percentage change in a bond's price for a 1% change in yield, assuming parallel shift in the yield curve.
        *   **Convexity:** A measure of the curvature in the relationship between bond prices and yields, indicating how duration changes as yields change.
        *   **Contribution to Portfolio Risk:**  The percentage of portfolio risk that can be attributed to a single bond.

    *   Apply these functions to each bond in the portfolio.

5.  **Create Interactive Table:**
    *   Use `streamlit.dataframe` or `streamlit.table` to display the bond data and calculated metrics in an interactive table.  The table should include columns for:
        *   Bond Name
        *   Maturity
        *   Yield to Maturity
        *   Coupon Rate
        *   Price
        *   Face Value
        *   Quantity
        *   Macaulay Duration
        *   Modified Duration
        *   Convexity
        *   Contribution to Portfolio Duration
        *   Contribution to Portfolio Convexity

6.  **Calculate Portfolio Aggregates:**
    *   Calculate the weighted-average duration and convexity for the entire portfolio.  The weights should be based on the market value of each bond in the portfolio.

7.  **Display Portfolio Aggregates:**
    *   Use `streamlit.metric` or `streamlit.write` to display the calculated portfolio aggregates (weighted-average duration and convexity) prominently.

8.  **Implement Yield Curve Shift Simulation:**
    *   Add an input widget (e.g., `streamlit.slider`) to allow users to simulate a parallel shift in the yield curve.
    *   Recalculate bond prices and portfolio aggregates based on the simulated yield curve shift.
    *   Update the interactive table and displayed aggregates with the simulated results.  This will allow users to see the impact of yield changes on portfolio risk.

9. **Interactive Charts**
     *   Incorporate interactive charts, such as line charts, bar graphs, and scatter plots to display trends and correlations.

10. **Annotations and Tooltips**
    *   Provide detailed insights and explanations directly on the charts via annotations and tooltips, to help interpret the data.

11. **Documentation**
    *   Include inline help and tooltips to guide users through each step of the data exploration process.

## Important Definitions, Examples, and Formulae

*   **Bond:** A debt instrument in which an investor loans money to an entity (corporate or governmental) that borrows the funds for a defined period of time at a fixed or variable interest rate.

*   **Yield to Maturity (YTM):** The total return an investor can expect if they hold the bond until it matures.  It takes into account the bond's current market price, par value, coupon interest rate, and time to maturity.

*   **Coupon Rate:** The annual interest rate stated on a bond when it's issued. It is expressed as a percentage of the bond's par value.

*   **Duration:** A measure of the sensitivity of the price of a bond or other debt instrument to a change in interest rates. There are two main types: Macaulay Duration and Modified Duration.

    *   **Macaulay Duration (MacDur):** The weighted average time until the bondholder receives the bond's cash flows. It's measured in years.

        *   Formula:  `MacDur = Σ [t * (CFt / (1 + y)t)] / P`  where:
            *   `t` = time period
            *   `CFt` = cash flow in period t
            *   `y` = yield to maturity
            *   `P` = bond's current price
        *   Example: A bond with a face value of $1000, a coupon rate of 5%, and a maturity of 3 years, trading at par (YTM = 5%).
            *   Year 1: $50 / (1.05)^1
            *   Year 2: $50 / (1.05)^2
            *   Year 3: $1050 / (1.05)^3
            *   `MacDur`= (1 \* ($50 / (1.05)^1) + 2 \* ($50 / (1.05)^2) + 3 \* ($1050 / (1.05)^3)) / $1000.00
    *   **Modified Duration (ModDur):** Approximates the percentage change in price of a bond for a 1% change in yield.

        *   Formula: `ModDur = MacDur / (1 + (y/n))` where:
            *   `MacDur` = Macaulay Duration
            *   `y` = yield to maturity
            *   `n` = number of coupon payments per year
            *   For a semi-annual coupon bond, n = 2

        *   Example:  Using MacDur from the above sample, let `n` be 2, since the coupon is payed semi-annually. `ModDur`= 2.86/ (1+ (0.05/2)) = 2.79

*   **Convexity:** Measures the curvature of the price-yield relationship.  It represents the second-order effect of interest rate changes on bond prices.  Higher convexity implies a greater change in duration as yields change.

    *   Formula: `Convexity ≈ (1/P) * [Σ (t^2 + t) * CFt / (1+y)^t] / (1+y)^2` where:

        *   `P` = bond price
        *   `t` = time to cash flow
        *   `CFt` = cash flow at time t
        *   `y` = yield to maturity
    * **Approximation Formula (See Exhibit 4):**

        *   `Convexity approx. ≈ ( (PV-) + (PV+) - (2 x PV0) ) / (ΔYield^2 x PV0)`
        *   Where PV- and PV+ can be obtained using the price formula:
            *   `𝑃𝑉 = ∑(𝐶𝐹𝑡 /(1 + 𝑦)𝑡)`

*   **Portfolio Duration:** Weighted average of the durations of the bonds in the portfolio. The weights are typically based on the market value of each bond in the portfolio.

    *   Formula: `Portfolio Duration = Σ (wi * Di)` where:
        *   `wi` = weight of bond i in the portfolio (market value of bond i / total market value of portfolio)
        *   `Di` = duration of bond i

*   **Portfolio Convexity:** Weighted average of the convexities of the bonds in the portfolio, using the same weights as portfolio duration.

    *   Formula: `Portfolio Convexity = Σ (wi * Ci)` where:
        *   `wi` = weight of bond i in the portfolio
        *   `Ci` = convexity of bond i

## Libraries and Tools

*   **Streamlit:** The primary library for building the web application. It's used to create the user interface, handle user input, and display results.
*   **Pandas:**  Used to store bond data in a structured format (DataFrames) and perform calculations on the data. It can also be used for creating and displaying tables.
*   **NumPy (Optional):**  Useful for numerical calculations, particularly when dealing with arrays and matrices, may be needed for efficient duration and convexity calculations.
*   **Matplotlib/Plotly (Optional):** Used to generate visualizations of the bond portfolio.
    *   If using annotations and tool tips on the interactive charts, both libraries allow a straightforward approach.
