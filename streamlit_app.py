import numpy as np
import altair as alt
import pandas as pd
import streamlit as st
from datetime import time, datetime

st.header('st.slider')

# Example 1

st.subheader('Slider')

# Example 2

age = st.slider('How old are you?', min_value=0,max_value=130)
st.write("I'm", age, "years old")

# Example 3
st.subheader("Range slider")
values = st.slider('Select a range of values', 0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

# Example 4

st.subheader("Range time slider")
appointment = st.slider("Schedule your appointment:",
                        value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)

# Example 5

st.subheader("Datetime slider")
start_time = st.slider("When do you start?",
                       value=datetime(2020, 1, 1, 9, 30),
                       format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)