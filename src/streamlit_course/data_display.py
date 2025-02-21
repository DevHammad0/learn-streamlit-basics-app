import streamlit as st
import pandas as pd #type: ignore
import numpy as np



# Create sample data
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Paris", "Berlin"]
}
st.markdown("### Displaying Data:")

# Display dataframe
st.subheader("DataFrame Display")
st.table(data)


# Display chart
st.subheader("Chart Example")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['Line 1', 'Line 2', 'Line 3']
)
st.line_chart(chart_data)


