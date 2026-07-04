import streamlit as st
import subprocess
import os
from PIL import Image

st.set_page_config(
    page_title="World Population Distribution",
    layout="wide"
)

st.title("🌍 World Population Distribution Dashboard")
st.write("This dashboard visualizes the world population distribution by age and gender.")

# Generate the visualization if it doesn't exist
if not os.path.exists("task1_population_distribution.png"):
    subprocess.run(["python", "task1_visualization.py"])

# Display the image
image = Image.open("task1_population_distribution.png")
st.image(image, use_container_width=True)

st.success("Visualization generated successfully!")