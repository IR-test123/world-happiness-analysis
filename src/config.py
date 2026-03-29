import sys
from pathlib import Path

sys.path.append(str(Path().resolve().parent))

BASE_DIR = Path("../")
DATA_DIR = BASE_DIR / "data"
RAW_DATA_PATH = DATA_DIR / "raw"
PROCESSED_DATA_PATH = DATA_DIR / "processed"
OUTPUT_FILE_FULL_PATH = PROCESSED_DATA_PATH / "combined_years.csv"

# -------------------------
# Canonical column names
# -------------------------
COL_COUNTRY = "country"
COL_RANK = "rank"
COL_HAPPINESS = "happiness_score"
COL_GDP = "gdp_per_capita"
COL_SOCIAL = "social_support"
COL_HEALTH = "life_expectancy"
COL_FREEDOM = "freedom"
COL_GENEROSITY = "generosity"
COL_CORRUPTION = "corruption"
COL_DYSTOPIA = "dystopia_residual"
COL_FILE_ID = "file_id"
COL_SOURCE_ROW = "source_row_index"

# -------------------------
# Core column groups
# -------------------------
ANALYSIS_COLUMNS = [
    COL_HAPPINESS,
    COL_GDP,
    COL_SOCIAL,
    COL_HEALTH,
    COL_FREEDOM,
    COL_GENEROSITY,
    COL_CORRUPTION,
]

COLUMNS_TO_KEEP = [
    COL_COUNTRY,
    COL_RANK,
    *ANALYSIS_COLUMNS,
    COL_DYSTOPIA,
]

ORIGINAL_DATA_FILE_COLUMNS = [
    COL_SOURCE_ROW,
    COL_FILE_ID,
]



# -------------------------
# Column mapping
# -------------------------
COLUMN_MAPPING = {
    # country
    "country": COL_COUNTRY,
    "country_or_region": COL_COUNTRY,

    # rank
    "happiness_rank": COL_RANK,
    "overall_rank": COL_RANK,

    # score
    "happiness_score": COL_HAPPINESS,
    "score": COL_HAPPINESS,

    # gdp
    "economy_gdp_per_capita": COL_GDP,
    "economy_gdp_per_capita_": COL_GDP,
    "gdp_per_capita": COL_GDP,

    # social
    "family": COL_SOCIAL,
    "social_support": COL_SOCIAL,

    # health
    "health_life_expectancy": COL_HEALTH,
    "healthy_life_expectancy": COL_HEALTH,
    "health_life_expectancy_": COL_HEALTH,
    "healthy_life_expectancy_": COL_HEALTH,

    # freedom
    "freedom": COL_FREEDOM,
    "freedom_to_make_life_choices": COL_FREEDOM,

    # corruption
    "trust_government_corruption": COL_CORRUPTION,
    "perceptions_of_corruption": COL_CORRUPTION,
    "trust_government_corruption_": COL_CORRUPTION,
    "perceptions_of_corruption_": COL_CORRUPTION,

    # generosity
    "generosity": COL_GENEROSITY,

    # dystopia
    "dystopia_residual": COL_DYSTOPIA,
}

COUNTRY_NAME_FIX = {
    'Trinidad': 'Trinidad and Tobago',
    'Hong Kong': 'Hong Kong',
    'Taiwan': 'Taiwan',
}

