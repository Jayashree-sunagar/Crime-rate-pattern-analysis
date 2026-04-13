import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# ---------------------------
# PAGE CONFIG
# ---------------------------
st.set_page_config(page_title="Crime Dashboard", layout="wide")

# ---------------------------
# CUSTOM CSS
# ---------------------------
st.markdown("""
<style>

.main {
    background-color: #0B1F3A;
    color: white;
}

/* Moving Banner */
.marquee {
    width: 100%;
    overflow: hidden;
    white-space: nowrap;
}
.marquee span {
    display: inline-block;
    padding-left: 100%;
    animation: marquee 12s linear infinite;
    color: #00FFFF;
    font-size: 20px;
    font-weight: bold;
}

@keyframes marquee {
    0%   { transform: translateX(0); }
    100% { transform: translateX(-100%); }
}

/* KPI Card Style */
div[data-testid="metric-container"] {
    background-color: #132C4C;
    border-radius: 10px;
    padding: 15px;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.5);
}

</style>
""", unsafe_allow_html=True)

# ---------------------------
# TITLE
# ---------------------------
st.title("🚨 Crime Rate Pattern Analysis")

# ---------------------------
# MOVING SLOGAN
# ---------------------------
st.markdown("""
<div class="marquee">
<span>🚔 Stay Alert • Stay Safe • Data-Driven Crime Monitoring • Predicting Safer Tomorrow 🔮</span>
</div>
""", unsafe_allow_html=True)

# ---------------------------
# LOAD DATA
# ---------------------------
df = pd.read_csv("NCRB_Table_crime_rate.csv")  

# ---------------------------
# SIDEBAR FILTER
# ---------------------------
st.sidebar.header("🔎 Select State")

selected_state = st.sidebar.selectbox(
    "Choose State",
    ["All"] + list(df["State/UT"].unique())
)

# ---------------------------
# FILTER LOGIC
# ---------------------------
if selected_state == "All":
    filtered_df = df
else:
    filtered_df = df[df["State/UT"] == selected_state]

# ---------------------------
# KPI SECTION
# ---------------------------
st.subheader("📊 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("🚔 Total Crimes", int(filtered_df["crime_2022"].sum()))
col2.metric("📊 Avg Crime Rate", round(filtered_df["Rate of Cognizable Crimes (IPC) (2022)"].mean(), 2))
col3.metric("⚖️ Avg Chargesheet", round(filtered_df["Chargesheeting Rate (2022)"].mean(), 2))

# ---------------------------
# LINE GRAPH (ONLY GRAPH)
# ---------------------------
st.subheader("📈 Crime Trend")

years = ["2020", "2021", "2022"]

if selected_state == "All":
    values = [
        df["crime_2020"].sum(),
        df["crime_2021"].sum(),
        df["crime_2022"].sum()
    ]
    color = "#00FFFF"  # Cyan
else:
    row = filtered_df.iloc[0]
    values = [
        row["crime_2020"],
        row["crime_2021"],
        row["crime_2022"]
    ]
    color = "#FFA500"  # Orange

fig, ax = plt.subplots()

ax.plot(years, values, marker='o', linewidth=4, color=color)
ax.set_xlabel("Year")
ax.set_ylabel("Crime Count")

# ✅ Dynamic Title
if selected_state == "All":
    title = "Crime Trend - All States"
else:
    title = f"Crime Trend - {selected_state}"

ax.set_title(title)

st.pyplot(fig)

# ---------------------------
# PREDICTION
# ---------------------------
X = df[['crime_2020', 'crime_2021',
        'Mid-Year Projected Population (in Lakhs) (2022)',
        'Chargesheeting Rate (2022)']]

y = df['crime_2022']

model = LinearRegression()
model.fit(X, y)

input_data = [[
    filtered_df['crime_2020'].mean(),
    filtered_df['crime_2021'].mean(),
    filtered_df['Mid-Year Projected Population (in Lakhs) (2022)'].mean(),
    filtered_df['Chargesheeting Rate (2022)'].mean()
]]

prediction = model.predict(input_data)

st.metric("🔮 Predicted Crime (2023)", int(prediction[0]))
