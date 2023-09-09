import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np

def main():
    st.title("Real-Time Inequality")

    # Use buttons for navigation to make it feel more like a presentation
    menu = ["Introduction", "Interactive Timeline", "Data Dive", "Visual Insights", "Discussion & Implications", "Q&A", "Conclusion", "About the Authors"]
    choice = st.sidebar.radio("Navigate", menu)

    # Functions for each section
    if choice == "Introduction":
        introduction()
    elif choice == "Interactive Timeline":
        interactive_timeline()
    elif choice == "Data Dive":
        data_dive()
    elif choice == "Visual Insights":
        visual_insights()
    elif choice == "Discussion & Implications":
        discussion_implications()
    elif choice == "Q&A":
        qa_section()
    elif choice == "Conclusion":
        conclusion()
    elif choice == "About the Authors":
        about_authors()

def load_dataset(file_name: str) -> pd.DataFrame:
    """Load dataset from the specified file name."""
    return pd.read_csv('personal_income - introduction function.csv')

def create_visualization(data: pd.DataFrame) -> go.Figure:
    """Create an interactive stacked area chart based on the dataset."""
    
    # Filter and transpose the data
    categories = [
        "    Compensation of employees",
        "        Wages and salaries",
        "    Proprietors' income with inventory valuation and capital consumption adjustments"
    ]
    filtered_data = data[data.iloc[:, 0].isin(categories)]
    transposed_data = filtered_data.set_index(filtered_data.columns[0]).T
    
    # Define milestones for annotations
    milestones = {
        "2007": "Start of Great Recession",
        "2009": "End of Great Recession",
        "2020": "COVID-19 Pandemic",
        "2021": "Vaccine Rollout & Economic Challenges"
    }
    
    # Create the figure
    fig = go.Figure()

    # Add data for each category
    for category in categories:
        fig.add_trace(go.Scatter(
            x=transposed_data.index,
            y=transposed_data[category].replace(',', '', regex=True).astype(float),
            mode='lines',
            stackgroup='one',
            name=category
        ))

    # Add annotations for milestones
    annotations = []
    for year, event in milestones.items():
        annotations.append(
            dict(
                x=year,
                y=np.max(transposed_data.replace(',', '', regex=True).astype(float).sum(axis=1)),
                xref="x",
                yref="y",
                text=event,
                showarrow=True,
                arrowhead=4,
                ax=0,
                ay=-40
            )
        )

    # Update figure layout
    fig.update_layout(
        title='Composition of Personal Income Over Time',
        xaxis_title='Year',
        yaxis_title='Amount ($ in billions)',
        annotations=annotations,
        plot_bgcolor='white',
        xaxis_showgrid=True,
        yaxis_showgrid=True,
        xaxis_gridcolor='lightgray',
        yaxis_gridcolor='lightgray'
    )
    
    return fig


def introduction():
    st.subheader("Introduction to Real-Time Inequality")

    # Extracted content from the paper's introduction
    st.write("""
    "Real-Time Inequality" presents a new methodology offering timely and high-frequency estimates of income distribution in the U.S. This method integrates various public data sources into a unified framework, with retrospective validation back to 1976.
    """)

    st.write("""
    The significance of real-time analysis in income distribution is paramount. By tracking the distributional impacts of government policies in real-time, we gain insights for data-informed policy decisions.
    """)

    # Load the dataset (NIPA data)
    data = load_dataset("personal_income - introduction function.csv")

    # Create a visualization based on the dataset
    fig = create_visualization(data)

    # Display the visualization
    st.plotly_chart(fig)

# Placeholder functions for other sections
def interactive_timeline():
    pass

def data_dive():
    pass

def visual_insights():
    pass

def discussion_implications():
    pass

def qa_section():
    pass

def conclusion():
    pass

def about_authors():
    pass

if __name__ == "__main__":
    main()
