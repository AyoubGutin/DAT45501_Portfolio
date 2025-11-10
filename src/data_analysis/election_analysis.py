# Election Data for the 2016 Election
import numpy as np
import plotly.express as px
from src.utils.df_utils import create_df, df_report, drop_null_rows
from src.utils.file_utils import find_root


# -- Setup --
PROJECT_ROOT = find_root()
file_path = PROJECT_ROOT / "data" / "US-2016-primary.csv"
elections_df = create_df(file_path=file_path, extension="csv")

# -- EDA --
df_report(elections_df)

# -- Cleaning --
elections_df = drop_null_rows(
    elections_df, subset_cols=["state", "county", "candidate", "votes"]
)

# -- MAIN LOGIC --

# Get a list of unique candidates
candidates_list = np.sort(elections_df["candidate"].unique())

for i, candidate in enumerate(candidates_list):
    print(f"{candidate}: {i}")

# Get user input for candidate
chosen_candidate = None
while chosen_candidate is None:
    try:
        choice_idx = int(
            input("\nEnter the number for the candidate you want to analyse: ")
        )
        chosen_candidate = candidates_list[choice_idx]
    except (ValueError, IndexError):
        print("Invalid choice. Please enter a number from the list.")

# Filter dataframe for that chosen candidate
candidate_df = elections_df[elections_df["candidate"] == chosen_candidate].copy()

# Add up votes for each state for all candidates (index = state, value = votes)
state_total_votes = elections_df.groupby("state")["votes"].sum()

# Calculate chosen candidate votes per state
candidate_state_votes = candidate_df.groupby("state")["votes"].sum()

# Get the fraction of candidate/total
vote_fractions_by_state = candidate_state_votes / state_total_votes

# -- PLOT --

# Convert series to dataframe
plot_df = vote_fractions_by_state.reset_index()
plot_df.columns = ["state", "fraction"]

# Interactive Histogram
fig = px.histogram(
    plot_df,
    x="fraction",
    hover_data=["state"],
    nbins=20,
    title=f"Histogram of {chosen_candidate}'s Vote Fraction by State (2016 Election)",
)

fig.update_layout(
    xaxis_title_text="Vote Fraction",
    yaxis_title_text="Number of States (Count)",
    xaxis_tickformat=".0%",
)

fig.show()
