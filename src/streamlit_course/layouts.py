import streamlit as st


st.header("5. Layouts")

st.markdown("### Using Columns:")

# Create three columns
col1, col2, col3 = st.columns(3)

with col1:
    st.header("Column 1")
    st.write("This is column 1")
    
with col2:
    st.header("Column 2")
    st.write("This is column 2")
    
with col3:
    st.header("Column 3")
    st.write("This is column 3")


st.write("---")
# Example with expander
st.markdown("### Using Expander:")
with st.expander("Click to expand"):
    st.write("This content is hidden by default!")