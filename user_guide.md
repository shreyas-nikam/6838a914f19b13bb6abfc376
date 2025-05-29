id: 6838a914f19b13bb6abfc376_user_guide
summary: s User Guide
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# Bond Portfolio Duration & Convexity Analyzer User Guide

This codelab will guide you through using the Bond Portfolio Duration & Convexity Analyzer application. This application is designed to help you understand and analyze the interest rate risk associated with bond portfolios. By inputting bond characteristics, you can calculate key risk metrics and simulate the impact of yield curve shifts on your portfolio. Understanding these concepts is crucial for effective fixed-income portfolio management.

## Understanding Bond Duration and Convexity

Duration and convexity are two key measures of a bond's price sensitivity to changes in interest rates.

*   **Duration:**  Approximates the percentage change in a bond's price for a 1% change in interest rates.  A higher duration implies greater sensitivity to interest rate changes. Specifically, the application calculates both Macaulay Duration and Modified Duration.
*   **Convexity:** Measures the curvature of the price-yield relationship. It provides a more accurate estimate of price changes than duration alone, especially for large interest rate movements.

These concepts are vital for managing interest rate risk in bond portfolios. This application will let you explore the impact of different bond characteristics on portfolio duration and convexity and how they are impacted by changes in the yield curve.

## Navigating the Application

Duration: 00:02

The application consists of three main sections, accessible through the sidebar navigation menu:

1.  **Bond Input:**  Allows you to input the details of individual bonds to be included in your portfolio.
2.  **Portfolio Analysis:**  Analyzes the portfolio based on the bonds you've entered, calculating key metrics and providing visualizations.
3.  **Yield Curve Simulation:**  Simulates the impact of yield curve shifts on your portfolio's value.

## Bond Input Page

Duration: 00:05

This page is where you define the individual bonds in your portfolio.

1.  **Input Bond Details:**  For each bond, enter the following information:
    *   **Bond Name/Identifier:** A unique name for the bond (e.g., "US Treasury Bond 1").
    *   **Maturity (years):** The number of years until the bond matures.
    *   **Yield to Maturity (%):** The total return anticipated on a bond if it is held until it matures.
    *   **Coupon Rate (%):** The annual interest rate paid by the bond.
    *   **Price:** The current market price of the bond.
    *   **Face Value:** The principal amount of the bond that will be repaid at maturity.
    *   **Quantity of Bonds:** The number of bonds you hold in your portfolio.

2.  **Add Bond:**  Click the "Add Bond" button to add the bond to your portfolio. The application will store this information.

3.  **View Bond Data:** A table will display all the bonds you've added, along with their calculated Macaulay Duration, Modified Duration, and Convexity.

<aside class="positive">
Remember to input realistic values for bond characteristics to get meaningful results. Experiment with different values to see how they affect duration and convexity.
</aside>

## Portfolio Analysis Page

Duration: 00:07

This page provides an analysis of your entire bond portfolio, based on the bonds you entered on the "Bond Input" page.

1.  **Portfolio Aggregates:** This section displays key portfolio-level metrics:
    *   **Weighted Average Duration:** The weighted average of the modified durations of all bonds in the portfolio, where the weights are based on the market value of each bond.  This provides an overall measure of the portfolio's sensitivity to interest rate changes.
    *   **Weighted Average Convexity:**  The weighted average of the convexities of all bonds in the portfolio, providing a more refined measure of interest rate risk.

2.  **Bond Contributions:**  This section shows the contribution of each individual bond to the overall portfolio duration and convexity.  This allows you to identify which bonds are contributing the most to the portfolio's interest rate risk. The table displays:
    *   **Contribution to Duration:** Calculated as Weight * Modified Duration.
    *   **Contribution to Convexity:** Calculated as Weight * Convexity.
    *   **Market Value:** The total market value of each bond holding.
    *   **Weight:** The percentage of the portfolio's total market value represented by each bond.

3.  **Visualizations:** This section presents charts to visualize the contribution of each bond to portfolio duration and convexity, making it easier to understand the risk profile of your portfolio.
    *   **Contribution to Portfolio Duration by Bond:** A bar chart showing each bond's contribution to the portfolio's overall duration.
    *   **Contribution to Portfolio Convexity by Bond:** A bar chart showing each bond's contribution to the portfolio's overall convexity.

## Yield Curve Simulation Page

Duration: 00:08

This page allows you to simulate the impact of changes in the yield curve on your portfolio.

1.  **Yield Curve Shift:** Use the slider to simulate a parallel shift in the yield curve. The slider allows you to specify a shift from -5.0% to +5.0%. A positive shift represents an increase in interest rates, while a negative shift represents a decrease.

2.  **Portfolio Aggregates (After Yield Shift):** This section displays the portfolio's weighted average duration and convexity *after* the simulated yield curve shift. Observe how these metrics change in response to the shift.

3.  **Bond Data (After Yield Shift):**  This table displays the updated bond data after the yield curve shift, including the recalculated bond prices ("New Price") and market values ("New Market Value").

4.  **Price Change Visualization:** This section visualizes the change in bond prices as a result of the yield curve shift.
    *   **Bond Price Change After Yield Shift:** A bar chart comparing the original price of each bond to its new price after the yield curve shift.

<aside class="negative">
Keep in mind that this simulation assumes a parallel shift in the yield curve. In reality, yield curve shifts can be more complex.
</aside>

## Analyzing the Results

Duration: 00:03

By using this application, you can:

*   **Understand the interest rate risk of your bond portfolio.**
*   **Identify the bonds that contribute the most to your portfolio's risk.**
*   **Simulate the impact of yield curve changes on your portfolio's value.**
*   **Make informed decisions about portfolio construction and risk management.**

Experiment with different bond combinations and yield curve scenarios to gain a deeper understanding of bond portfolio management principles. This application provides a powerful tool for visualizing and analyzing the complex relationship between interest rates and bond prices.
