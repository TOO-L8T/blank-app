import streamlit as st

st.write("Loaded secrets:", st.secrets)

# ✅ Use the correct connection name from secrets.toml
conn = st.connection("my_example_connection", type="snowflake")

df = conn.query("SELECT * FROM PETS.PUBLIC.MYTABLE;", ttl="10m")

for row in df.itertuples():
    st.write(f"{row.NAME} has a :{row.PET}:")
