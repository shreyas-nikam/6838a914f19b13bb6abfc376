
# Bond Portfolio Duration & Convexity Analyzer

This Streamlit application allows users to analyze and compare the interest rate risk of different bond portfolios. 
Users can input bond characteristics, view key risk metrics, and understand the impact of individual bonds on the overall portfolio's risk profile.

## Instructions

1.  Install Docker.
2.  Clone this repository.
3.  Build the Docker image: `docker build -t bond-portfolio-analyzer .`
4.  Run the Docker container: `docker run -p 8501:8501 bond-portfolio-analyzer`
5.  Open your browser and go to `http://localhost:8501`.

## Usage

1.  Navigate to the "Bond Input" page to add bonds to the portfolio.
2.  Enter the bond details and click "Add Bond".
3.  Navigate to the "Portfolio Analysis" page to view the portfolio aggregates and bond contributions.
4.  Navigate to the "Yield Curve Simulation" page to simulate a parallel shift in the yield curve and see the impact on bond prices and portfolio aggregates.

## License

© 2025 QuantUniversity. All Rights Reserved.
