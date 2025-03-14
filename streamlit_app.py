import streamlit as st

# Manually extract secrets
secrets = st.secrets["connections"]["snowflake"]

# Connect using extracted secrets
conn = st.connection(
    "snowflake",
    type="snowflake",
    account=secrets["LLQXEZW-UNB86947"],
    user=secrets["TOOL8T"],
    authenticator=secrets["externalbrowser"],
    role=secrets["ACCOUNTADMIN"],
    warehouse=secrets["STREAMLIT_WH"],
    database=secrets["PETS"],
    schema=secrets["PUBLIC"],
)

df = conn.query("SELECT * FROM PETS.PUBLIC.MYTABLE;", ttl="10m")

for row in df.itertuples():
    st.write(f"{row.NAME} has a :{row.PET}:")
