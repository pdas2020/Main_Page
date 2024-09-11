import streamlit as st
import pandas as pd
import time
import plotly.express as px
import streamlit.components.v1 as components
import pydeck as pdk

# Set page configuration
st.set_page_config(page_title="AI Project Dashboard", layout="wide")

# sidebar

st.sidebar.link_button(
    label="Home",
    url="https://main.smartaiclub.com/")
st.sidebar.link_button(
    label="Chatbot",
    url="https://openai.smartaiclub.com/")
st.sidebar.link_button(
    label="Stock Analysis",
    url="https://finance.smartaiclub.com/")
st.sidebar.link_button(
    label="Breast Cancer Analysis",
    url="https://research.smartaiclub.com/")
st.sidebar.link_button(
    label="Newsletter Generator",
    url="https://crewai.smartaiclub.com/")
st.sidebar.link_button(
    label="Basketball Player Stats",
    url="https://basketball.smartaiclub.com/")
st.sidebar.link_button(
    label="About Me",
    url="https://ishan.smartaiclub.com/")


# Custom CSS to set the background image and improve readability
# Custom CSS with updated title colors
background_image = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1506748686214-e9df14d4d9d0");
    background-size: cover;
}
[data-testid="stHeader"] {
    background-color: rgba(0,0,0,0);
}

.stApp {
    background-color: rgba(255, 255, 255, 0.85);
}

.stMarkdown, .stDataFrame, .stSelectbox {
    background-color: rgba(255, 255, 255, 0.9);
    padding: 20px;
    border-radius: 10px;
}

h1, h2, h3 {
    color: #1a237e;  /* Dark blue color for better visibility */
    font-weight: bold;
    text-shadow: 1px 1px 2px rgba(255,255,255,0.5);  /* Text shadow for better contrast */
}

p {
    color: #1a237e;  /* Matching dark blue for paragraph text */
    font-weight: bold;
}

.stSelectbox > div > label {
    color: #1a237e;  /* Matching dark blue for selectbox label */
    font-weight: bold;
}
</style>
"""

st.markdown(background_image, unsafe_allow_html=True)
st.title("AI Projects Dashboard")
st.write("Sample Visualization dashboard displaying countrieswise GDP and life expectancy. ")
# Create a chart
df = px.data.gapminder()
fig = px.scatter(df, x="gdpPercap", y="lifeExp", animation_frame="year", 
                    animation_group="country", size="pop", color="continent", 
                    hover_name="country", log_x=True, size_max=55)
st.plotly_chart(fig)



# Create a dataframe with project information
projects = pd.DataFrame({
    "ProjectName": ["Newsletter Generator", "Stock Analyzer", "Chatbot", "Breast Cancer Analysis", "Basketball Player Stats"],
    "Description": [
        "The newsletter-gen Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks",
        "Used yahoo finance api to analyze stock prices using convolutional neural networks",
        "An AI-powered conversational agent",
        "Analyze breast cancer data using machine learning algorithms",
        "Provides insights into players career records using machine learning algorithms"
    ],
    "Technologies": ["CrewAI, Langchain", "yfinance, Pandas", "OpenAI, Streamlit", "scikit_learn, numpy,pandas","matplotlib,numpy, Pandas"],
    "Status": ["In Progress", "Completed", "Completed", "Completed","Completed"]
})

# Define a function to generate URLs based on status
def get_status_url(ProjectName):
    if ProjectName == "Newsletter Generator":
        return "https://crewai.smartaiclub.com/"
    elif ProjectName == "Chatbot":
        return "https://openai.smartaiclub.com/"
    elif ProjectName == "Stock Analyzer":
        return "https://finance.smartaiclub.com/"
    elif ProjectName == "Basketball Player Stats":
        return "https://basketball.smartaiclub.com/"
    elif ProjectName == "Breast Cancer Analysis":
        return "https://research.smartaiclub.com/"
    else:
        return "https://main.smartaiclub.com/"

# Add a new column with hyperlinks
projects['Project Link'] = projects['ProjectName'].apply(lambda x: f'<a href="{get_status_url(x)}" target="_blank">{x}</a>')

# Display projects in a table
st.header("Project Overview")
# Display the DataFrame
st.write(projects.to_html(escape=False, index=False), unsafe_allow_html=True)

# Project details section
st.header("Project Details")
selected_project = st.selectbox("Select a project for more details:", projects["ProjectName"])

if selected_project:
    project = projects[projects["ProjectName"] == selected_project].iloc[0]
    st.subheader(project["ProjectName"])
    st.write(f"**Description:** {project['Description']}")
    st.write(f"**Technologies:** {project['Technologies']}")
    st.write(f"**Status:** {project['Status']}")
    
# Skills section
st.header("Skills")
skills = ["Python", "Machine Learning", "Deep Learning", "Natural Language Processing", "Computer Vision","GenAI", "CrewAI", "OpenAI", "Streamlit"]
st.write(", ".join(skills))

# Map section
st.header("My Location")

# Create two columns
col1, col2 = st.columns([1, 2])

with col1:
    # Coordinates for Raleigh, NC
    raleigh_lat, raleigh_lon = 35.7796, -78.6382

    # Create a DataFrame with Raleigh's coordinates
    df = pd.DataFrame({
        'lat': [raleigh_lat],
        'lon': [raleigh_lon]
    })

    # Display the map
    st.pydeck_chart(pdk.Deck(
        map_style='mapbox://styles/mapbox/light-v9',
        initial_view_state=pdk.ViewState(
            latitude=raleigh_lat,
            longitude=raleigh_lon,
            zoom=11,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                'ScatterplotLayer',
                data=df,
                get_position='[lon, lat]',
                get_color='[200, 30, 0, 160]',
                get_radius=500,
            ),
        ],
    ))
with col2:
    # Contact information
    st.header("Contact Information")
    st.write("Email: ishand2015@gmail.com")
    st.write("LinkedIn: [Your LinkedIn Profile](https://www.linkedin.com/in/ishan-das-63600731a/)")
    st.write("GitHub: [Your GitHub Profile](https://github.com/WildingMender19)")
    st.write("© 2024 Ishan Das. All rights reserved.")
