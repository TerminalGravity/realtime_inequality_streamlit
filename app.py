import streamlit as st
import pandas as pd

# Load the NIPA personal income distribution dataset
personal_income_data = pd.read_csv("personal_income_processed.csv", index_col=0)
income_categories = personal_income_data.columns.dropna().tolist()

def introduce_paper():
    st.subheader("NBER Working Paper: Real-Time Inequality")
    st.write("""
    The working paper titled "Real-Time Inequality" is authored by Thomas Blanchet, Emmanuel Saez, and Gabriel Zucman.
    
    The research focuses on constructing high-frequency and timely income distributions for the United States. The authors have developed a methodology to combine information from various high-frequency public data sources, including monthly household and employment surveys, quarterly censuses of employment and wages, and monthly and quarterly national accounts statistics.
    
    The aim is to provide an up-to-date understanding of income distribution disparities across different segments of the population.
    """)
    st.write("[Read the full NBER Working Paper](http://www.nber.org/papers/w30229)")
    st.write("[Visit the supplementary website](https://realtimeinequality.org)")

def overall_income_growth():
    st.subheader("Overall Personal Income Growth Over the Years")
    personal_income = personal_income_data["Personal income"]
    st.line_chart(personal_income, use_container_width=True)
    
def top_components_contribution():
    st.subheader("Contribution of Top Income Components Over the Years")
    top_components = personal_income_data.drop(columns=["Personal income"]).sum().nlargest(5).index
    st.line_chart(personal_income_data[top_components], use_container_width=True)
    
def growth_fluctuations():
    st.subheader("Steady Growth with Fluctuations")
    personal_income = personal_income_data["Personal income"]
    st.line_chart(personal_income, use_container_width=True)
    
def dominant_components():
    st.subheader("Dominant Income Components")
    dominant_components_corrected = ["    Compensation of employees", "    Wages and salaries"]
    st.line_chart(personal_income_data[dominant_components_corrected], use_container_width=True)


def interactive_data_exploration():
    st.subheader("Interactive Data Exploration")
    visualization_options = [
        "Overall Personal Income Growth Over the Years",
        "Contribution of Top Income Components Over the Years",
        "Steady Growth with Fluctuations",
        "Dominant Income Components"
    ]
    selected_visualization = st.selectbox("Select a visualization:", visualization_options)
    
    if selected_visualization == visualization_options[0]:
        overall_income_growth()
    elif selected_visualization == visualization_options[1]:
        top_components_contribution()
    elif selected_visualization == visualization_options[2]:
        growth_fluctuations()
    elif selected_visualization == visualization_options[3]:
        dominant_components()

    st.subheader("Interactive Data Exploration")
    st.write("Explore the NIPA personal income distribution over the years.")
    
    # Dropdown selector for income categories
    selected_category = st.selectbox("Select an income category:", income_categories)
    
    # Extract data for the selected category
    category_data = personal_income_data[[selected_category]]
    
    # Display an interactive line chart
    st.line_chart(category_data, use_container_width=True, height=400)

def discussion_and_implications():
    st.subheader("Discussion & Implications")
    st.write("""
    Based on the NIPA personal income distribution dataset and the methodology presented in the NBER paper, we observe several key implications:
    
    1. **Income Disparities**: The data showcases significant income disparities across different segments of the population. This has broader socio-economic implications and can influence policy decisions.
    2. **Timely Insights**: The high-frequency nature of the data provides timely insights, which are crucial during economic downturns or upheavals.
    3. **Policy Recommendations**: Governments and policymakers can leverage these findings to design more inclusive economic policies and interventions.
    
    The dataset and the findings from the NBER paper provide a foundation for understanding the dynamics of income distribution in real-time.
    """)

def conclusion():
    st.subheader("Conclusion")
    st.write("""
    The NBER Working Paper "Real-Time Inequality" sheds light on the importance of understanding income distributions in a timely manner. With the combination of various high-frequency public data sources, the authors have presented a methodology that offers real-time insights into income disparities. Such research not only enriches academic discourse but also has tangible implications for policy design and socio-economic interventions.
    """)

def about_authors():
    st.subheader("About the Authors")
    st.write("""
    **Thomas Blanchet**: A renowned economist with a focus on income and wealth distribution methodologies. He has contributed extensively to the discourse on economic disparities and their implications.
    
    **Emmanuel Saez**: An expert in the field of income inequality, Saez's research has been pivotal in shaping economic policies and understanding the dynamics of wealth distribution.
    
    **Gabriel Zucman**: Known for his work on tax havens and the distribution of global wealth, Zucman's insights have been instrumental in the global discourse on economic policies and wealth disparities.
    
    Together, these authors have collaborated on various research projects, contributing significantly to the understanding of income and wealth distributions.
    """)

# Main function to navigate the app
def main():
    st.title("Real-Time Inequality")
    menu = ["Introduction", "Interactive Data Exploration", "Discussion & Implications", "Conclusion", "About the Authors"]
    choice = st.sidebar.selectbox("Choose a section", menu)

    if choice == "Introduction":
        introduce_paper()
    elif choice == "Interactive Data Exploration":
        interactive_data_exploration()
    elif choice == "Discussion & Implications":
        discussion_and_implications()
    elif choice == "Conclusion":
        conclusion()
    elif choice == "About the Authors":
        about_authors()

# Run the main function to start the app
main()
