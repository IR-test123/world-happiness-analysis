import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from config import OUTPUT_FILE_FULL_PATH, ANALYSIS_COLUMNS, COL_COUNTRY, COL_FILE_ID, COL_RANK, COL_HAPPINESS, COL_GDP

# -------------------------
# Load data
# -------------------------
@st.cache_data
def load_data():
    df = pd.read_csv(OUTPUT_FILE_FULL_PATH)
    return df

combined_years_df = load_data()

st.title("🌍 World Happiness Dashboard")

# -------------------------
# Sidebar filters
# -------------------------
st.sidebar.header("Filters")

years = sorted(combined_years_df[COL_FILE_ID].unique())
selected_year = st.sidebar.selectbox("Select Year", years)

# -------------------------
# Filtered data
# -------------------------
df_year = combined_years_df[combined_years_df[COL_FILE_ID] == selected_year]


# -------------------------
# 1. Top Countries Bar Chart
# -------------------------
st.subheader(f"🏆 Top Countries in {selected_year}")

top_n = st.slider("Top N Happiest countries", 20, 50, 10)

top_df = df_year.sort_values(
    by=COL_HAPPINESS,
    ascending=False
).head(top_n)

# -------------------------
# 1a. Top Happiest Countries Bar Chart
# -------------------------

fig1a, ax1a = plt.subplots()
ax1a.barh(top_df[COL_COUNTRY], top_df[COL_HAPPINESS])
ax1a.invert_yaxis()

st.pyplot(fig1a)

# -------------------------
# 1b. Happiest Countries Staked By Factor
# -------------------------

# -------------------------
# Columns to stack
# -------------------------

exclude_cols = [COL_COUNTRY, COL_FILE_ID, COL_RANK, COL_HAPPINESS]

factor_cols = [
    col for col in top_df.select_dtypes(include="number").columns
    if col not in exclude_cols
]

# -------------------------
# Prepare data
# -------------------------
plot_df = top_df[[COL_COUNTRY] + factor_cols].set_index(COL_COUNTRY)

# -------------------------
# Plot stacked horizontal bar
# -------------------------
fig1b, ax1b = plt.subplots(figsize=(10, 6))

plot_df.plot(
    kind="barh",
    stacked=True,
    ax=ax1b
)

ax1b.set_title(f"Top N Happiest Countries By Factor")
ax1b.set_xlabel("Factor Contribution")
ax1b.set_ylabel("Country")
ax1b.invert_yaxis()

# Move the legend so it won't interfere with the data
ax1b.legend(
    title="Factors",
    bbox_to_anchor=(1.02, 1),
    loc="upper left"
)

st.pyplot(fig1b)

# -------------------------
# 2. GDP vs Happiness Scatter
# -------------------------
st.subheader("💰 GDP vs Happiness")

fig2, ax2 = plt.subplots()

ax2.scatter(
    df_year[COL_GDP],
    df_year[COL_HAPPINESS]
)

ax2.set_xlabel("GDP per Capita")
ax2.set_ylabel("Happiness Score")

st.pyplot(fig2)

# -------------------------
# 3. Correlation Heatmap
# -------------------------
st.subheader("🧠 Correlation Between Factors")

corr = df_year[ANALYSIS_COLUMNS].corr()

fig3, ax3 = plt.subplots()
cax = ax3.matshow(corr)

fig3.colorbar(cax)

ax3.set_xticks(range(len(ANALYSIS_COLUMNS)))
ax3.set_yticks(range(len(ANALYSIS_COLUMNS)))

ax3.set_xticklabels(ANALYSIS_COLUMNS, rotation=45)
ax3.set_yticklabels(ANALYSIS_COLUMNS)

st.pyplot(fig3)