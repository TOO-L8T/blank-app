import streamlit as st

# ✅ Check if secrets are being loaded
if "snowflake" in st.secrets["connections"]:
    st.write("✅ Secrets are being loaded correctly!")
else:
    st.write("❌ Secrets are NOT being loaded!")

# ✅ Extract Snowflake credentials
secrets = st.secrets["connections"]["snowflake"]

# ✅ Connect to Snowflake
conn = st.connection(
    "snowflake",
    type="snowflake",
    account=secrets["account"],
    user=secrets["user"],
    authenticator=secrets["password"],
    role=secrets["role"],
    warehouse=secrets["warehouse"],
    database=secrets["database"],
    schema=secrets["schema"],
)

# ✅ Test a simple query
df = conn.query("SELECT CURRENT_DATABASE(), CURRENT_SCHEMA();")
st.write(df)
