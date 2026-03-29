import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from config import OUTPUT_FILE_FULL_PATH, COL_COUNTRY, COL_FILE_ID, COL_RANK, COL_HAPPINESS

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

countries = sorted(combined_years_df[COL_COUNTRY].unique())
selected_countries = st.sidebar.multiselect(
    "Select Countries (for trends)",
    countries,
    default=["Israel", "United States"]
)

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
fig2, ax2 = plt.subplots(figsize=(10, 6))

plot_df.plot(
    kind="barh",
    stacked=True,
    ax=ax2
)

ax2.set_title(f"Top N Happiest Countries By Factor")
ax2.set_xlabel("Factor Contribution")
ax2.set_ylabel("Country")
ax2.invert_yaxis()

# Move the legend so it won't interfere with the data
ax2.legend(
    title="Factors",
    bbox_to_anchor=(1.02, 1),
    loc="upper left"
)

st.pyplot(fig2)

# -------------------------
# 2. Happiness Trend Over Time
# -------------------------
# st.subheader("📈 Happiness Trend Over Time")
#
# trend_df = combined_years_df[
#     combined_years_df["country"].isin(selected_countries)
# ]
#
# fig2, ax2 = plt.subplots()
#
# for country in selected_countries:
#     country_df = trend_df[trend_df["country"] == country]
#     ax2.plot(
#         country_df["file_id"],
#         country_df["happiness_score"],
#         label=country
#     )
#
# ax2.legend()
# ax2.set_xlabel("Year")
# ax2.set_ylabel("Happiness Score")
#
# st.pyplot(fig2)

# -------------------------
# 3. GDP vs Happiness Scatter
# -------------------------
st.subheader("💰 GDP vs Happiness")

fig3, ax3 = plt.subplots()

ax3.scatter(
    df_year["gdp_per_capita"],
    df_year["happiness_score"]
)

ax3.set_xlabel("GDP per Capita")
ax3.set_ylabel("Happiness Score")

st.pyplot(fig3)

# -------------------------
# 4. Correlation Heatmap
# -------------------------
st.subheader("🧠 Correlation Between Factors")

corr_cols = [
    "happiness_score",
    "gdp_per_capita",
    "social_support",
    "life_expectancy",
    "freedom",
    "generosity",
    "corruption"
]

corr = df_year[corr_cols].corr()

fig4, ax4 = plt.subplots()
cax = ax4.matshow(corr)

fig4.colorbar(cax)

ax4.set_xticks(range(len(corr_cols)))
ax4.set_yticks(range(len(corr_cols)))

ax4.set_xticklabels(corr_cols, rotation=45)
ax4.set_yticklabels(corr_cols)

st.pyplot(fig4)