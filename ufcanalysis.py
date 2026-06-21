import pandas as pd
import numpy as np
from scipy import stats

df = pd.read_csv("ufceng_revised.csv",
                 sep=",",
                 encoding="utf-8-sig",
                 skipinitialspace=True)
#statistical values
print("="*60)
print("FINISHING_RATE STATISTICS")
print("="*60)
print(df["FINISHING_RATE"].describe())
print()

#elite(25%) fighters according to summary statistics
elite_threshold = df["FINISHING_RATE"].quantile(0.75) #calculate threshold
print(f"Elite threshold (top %25): {elite_threshold}%")

finishers = df[df["FINISHING_RATE"] >= elite_threshold]
print(f"Total elite fighters: {len(finishers)}")
print("Elite Fighters:")
print(finishers[["FIGHTER", "COUNTRY", "TKO_WINS", "TKO_LOSSES", "SUB_WINS", "SUB_LOSSES", "PRIMARY_STYLE", "WIN_RATE",
                 "TOTAL_FIGHTS", "TOTAL_WINS", "TOTAL_LOSSES","DRAW", "RECORD", "AGE", "FINISHING_RATE"]])

 #Top 10% analysis
top_elite = df[df["FINISHING_RATE"] >= df["FINISHING_RATE"].quantile(0.90)]
print(f"Top 10% threshold: {top_elite}%")
print(top_elite[["FIGHTER", "COUNTRY", "TKO_WINS", "TKO_LOSSES", "SUB_WINS", "SUB_LOSSES", "PRIMARY_STYLE", "WIN_RATE",
                 "TOTAL_FIGHTS", "TOTAL_WINS", "TOTAL_LOSSES","DRAW", "RECORD", "AGE", "FINISHING_RATE"]])

#Calculate statistics
total_fighters = len(top_elite)
min_finish_rate = top_elite["FINISHING_RATE"].min()
max_finish_rate = top_elite["FINISHING_RATE"].max()
overall_avg_age = df["AGE"].mean()
average_age = top_elite["AGE"].mean()
average_tko = top_elite["TKO_WINS"].mean()
average_sub = top_elite["SUB_WINS"].mean()

#Results
print("\n" + "="*60)
print("TOP 10% ANALYSIS (NADIR ELIT)")
print("="*60)
print(f"Total Fighters: {total_fighters}")
print(f"Finish Rate Range: {min_finish_rate}% - {max_finish_rate}%")
print(f"Average Age: {average_age:.1f} (Overall: {overall_avg_age:.1f})")
print(f"Average TKO: {average_tko:.1f}")
print(f"Average SUB: {average_sub:.1f}")
print(f"TKO/SUB Ratio: {average_tko/average_sub:.1f}:1")
print("\nPrimary Style Distribution:")
print(top_elite["PRIMARY_STYLE"].value_counts())
print()

#Age difference
t_stat, p_value = stats.ttest_ind(top_elite["AGE"], df["AGE"])
print(f"Age difference t-test: p-value = {p_value:.3f}")

if p_value < 0.05:
    print("Age gap is statistically meaningful")
else:
    print("Age gap is not meaningful")
print()

#Show top elite fighters
print("TOP 10% FIGHTERS:")
print(top_elite[["FIGHTER", "COUNTRY", "TKO_WINS", "TKO_LOSSES", "SUB_WINS", "SUB_LOSSES", "PRIMARY_STYLE", "WIN_RATE",
                 "TOTAL_FIGHTS", "TOTAL_WINS", "TOTAL_LOSSES","DRAW", "RECORD", "AGE", "FINISHING_RATE"]]
      .sort_values("FINISHING_RATE", ascending=False))
print()

# EXPORT FOR POWER BI
print("="*60)
print("EXPORTING RESULTS")
print("="*60)
finishers.to_csv('elite_fighters_top25.csv', index=False)
top_elite.to_csv('top_10_percent.csv', index=False)
print(" elite_fighters_top25.csv exported")

