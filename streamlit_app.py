import streamlit as st

# ✅ Extract secrets from Streamlit
secrets = st.secrets["connections"]["snowflake"]

# ✅ Connect to Snowflake using password authentication
conn = st.connection(
    "snowflake",
    type="snowflake",
    account=secrets["account"],
    user=secrets["user"],
    password=secrets["password"],  # ✅ Ensure password is used
    role=secrets["role"],
    warehouse=secrets["warehouse"],
    database=secrets["database"],
    schema=secrets["schema"],
)

# ✅ Run a simple test query
df = conn.query("SELECT CURRENT_DATABASE(), CURRENT_SCHEMA();")
st.write(df)
