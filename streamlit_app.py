import streamlit as st

st.write("Loaded secrets:", st.secrets)


conn = st.connection("snowflake")


df = conn.query("SELECT * FROM PETS.PUBLIC.mytable;", ttl="10m")


for row in df.itertuples():
    st.write(f"{row.NAME} has a :{row.PET}:")
