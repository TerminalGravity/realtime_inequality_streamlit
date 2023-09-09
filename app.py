import streamlit as st

def main():
    st.title("Real-Time Inequality")
    
    # Add a sidebar for navigation
    menu = ["Home", "Data Overview", "Key Findings", "Discussion & Conclusion", "About"]
    choice = st.sidebar.selectbox("Menu", menu)
    
    if choice == "Home":
        home()
    elif choice == "Data Overview":
        data_overview()
    elif choice == "Key Findings":
        key_findings()
    elif choice == "Discussion & Conclusion":
        discussion_conclusion()
    elif choice == "About":
        about()

def home():
    st.subheader("Introduction to Real-Time Inequality")
    
    st.write("""
    This paper constructs high-frequency and timely income distributions for the United States. The authors have developed a methodology that combines information from various high-frequency public data sources—including monthly household and employment surveys, quarterly censuses of employment and wages, and monthly and quarterly national accounts statistics—in a unified framework. This approach allows them to:

    1. Estimate economic growth by income groups, race, and gender consistent with quarterly releases of macroeconomic growth.
    2. Track the distributional impacts of government policies during and after recessions in real-time.

    The methodology was tested and validated by implementing it retrospectively back to 1976. When analyzing the Covid-19 pandemic, the findings were:

    1. All income groups recovered their pre-crisis pretax income level within 20 months from the start of the recession.
    2. The recovery was primarily driven by jobs rather than wage growth.
    3. Real wages saw significant gains at the lower end of the distribution in 2021 and 2022, emphasizing the equalizing effects of tight labor markets.
    4. After considering taxes and cash transfers, real disposable income for the bottom 50% was nearly 20% higher in 2021 than in 2019, but it decreased in 2022 as the welfare state expansion during the pandemic was reversed.

    All estimates are available at [realtimeinequality.org](https://realtimeinequality.org) and are updated with each quarterly release of the national accounts.
    """)

    st.write("Authors: Thomas Blanchet, Gabriel Zucman")


def data_overview():
    st.subheader("Data Overview")
    
    # Overview text
    st.write("""
    The research paper "Real-Time Inequality" harnesses the power of diverse high-frequency public data sources to construct timely income distributions for the United States. The following are the primary data sources utilized:
    """)
    
    # List of data sources
    data_sources = [
        "Monthly household and employment surveys",
        "Quarterly censuses of employment and wages",
        "Monthly and quarterly national accounts statistics"
    ]
    
    for source in data_sources:
        st.write(f"- {source}")
    
    st.write("""
    The integration of these varied data sources into a unified framework provides a comprehensive view of the income distribution landscape. This data-driven approach enables real-time insights into the distributional impacts of government policies, economic growth patterns by income groups, and more.
    """)

def key_findings():
    st.subheader("Key Findings")

    # Point 1
    st.write("""
    The research addresses the gap of having high-frequency and timely distributions of income for the U.S., 
    elevating distributional statistics to the same footing as macroeconomic statistics.
    """)

    # Point 2
    st.write("""
    A novel methodology is proposed to combine information from various high-frequency public data sources, 
    resulting in harmonized monthly micro-files.
    """)

    # Point 3
    st.write("""
    The resulting data can estimate quarterly economic growth by social group in alignment with the official 
    macroeconomic growth release. This allows for the estimation of "distributional output gaps," indicating 
    how income remains below its pre-recession level or trend for various income distribution groups.
    """)

    # Point 4
    st.write("""
    The data also incorporates tax and government transfer variables, making it possible to monitor how losses 
    for different social groups during a crisis are mitigated by stabilization policies.
    """)

    # Point 5
    st.write("""
    The intuition behind the methodology's success is that around 30% of the national income is capital income. 
    Given that wealth is a stock variable, the concentration of the various components of capital income is 
    relatively stable at high frequency.
    """)

    # Point 6
    st.write("""
    The starting point for estimating monthly distributions is the annual distributional national accounts 
    synthetic micro-data from previous research. This data combines IRS tax micro-data, surveys, and national 
    accounts data to construct annual distributions of income and wealth consistent with national accounts aggregates.
    """)

    # Optionally, you can add visualizations or other interactive elements related to the key findings here.

def discussion_conclusion():
    st.subheader("Discussion & Conclusion")
    
    # Key Points
    st.markdown("""
    - The paper offers a comprehensive methodology to analyze real-time inequality, leveraging multiple high-frequency public data sources.
    - The findings provide insights into the dynamics of income inequality during significant economic events like the Covid-19 pandemic and the Great Recession of 2008-2009.
    - During the Covid-19 crisis, there was a noticeable pattern of income growth, with significant gains at the bottom and top of the distribution, in contrast to the middle.
    - The research emphasizes the importance of real-time data in understanding and responding to economic shifts and their distributional impacts.
    """)


def about():
    st.subheader("About the Research Paper")
    st.write("Title: Real-Time Inequality")
    st.write("Authors: Thomas Blanchet, Emmanuel Saez, Gabriel Zucman")
    st.write("NBER Working Paper Series")
    st.write("Working Paper 30229")
    st.write("Published by the National Bureau of Economic Research (NBER)")
    st.write("[Link to the paper](http://www.nber.org/papers/w30229)")

    st.subheader("About the Authors")
    st.write("""
    **Thomas Blanchet**  
    University of California  
    Evans Hall #3880  
    Berkeley, CA 94720  
    United States  
    """)
    
    st.write("""
    **Gabriel Zucman**  
    Department of Economics  
    University of California, Berkeley  
    530 Evans Hall, #3880  
    Berkeley, CA 94720  
    """)

    st.write("""
    **Emmanuel Saez**  
    (Affiliation details not provided in the extracted content)
    """)

if __name__ == "__main__":
    main()
