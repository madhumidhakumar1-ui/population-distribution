import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
import numpy as np

# ── Simulated World Bank-style population dataset ──────────────────────────
np.random.seed(42)

age_groups = ['0-4', '5-9', '10-14', '15-19', '20-24', '25-29',
              '30-34', '35-39', '40-44', '45-49', '50-54', '55-59',
              '60-64', '65-69', '70-74', '75-79', '80+']

# Approximate population (millions)
male_pop   = [340, 330, 320, 315, 310, 295, 280, 265, 245, 225, 205, 175, 140, 105, 75, 45, 30]
female_pop = [325, 315, 305, 300, 298, 285, 272, 260, 242, 222, 204, 178, 148, 116, 90, 60, 48]

df_age = pd.DataFrame({
    'Age Group': age_groups,
    'Male': male_pop,
    'Female': female_pop
})

df_age['Total'] = df_age['Male'] + df_age['Female']

# Gender distribution
df_gender = pd.DataFrame({
    'Gender': ['Male', 'Female'],
    'Population (millions)': [4000, 3960]
})

# ── Figure setup ───────────────────────────────────────────────────────────
fig = plt.figure(figsize=(18, 14), facecolor='#0f0c29')
fig.suptitle('World Population Distribution',
             fontsize=24, fontweight='bold',
             color='white', y=0.97)

DARK_BG  = '#1a1740'
GRID_CLR = '#2d2a5e'
MALE_CLR = '#4fc3f7'
FEM_CLR  = '#f48fb1'
TOT_CLR  = '#a78bfa'
TEXT_CLR = 'white'

def style_ax(ax, title):
    ax.set_facecolor(DARK_BG)
    ax.tick_params(colors=TEXT_CLR, labelsize=10)
    ax.set_title(title, color=TEXT_CLR, fontsize=14, fontweight='bold', pad=12)
    ax.set_xlabel(ax.get_xlabel(), color=TEXT_CLR)
    ax.set_ylabel(ax.get_ylabel(), color=TEXT_CLR)
    ax.grid(axis='y', color=GRID_CLR, linestyle='--', alpha=0.5)
    for spine in ax.spines.values():
        spine.set_color(GRID_CLR)

# ── Plot 1: Grouped Bar Chart ──────────────────────────────────────────────
ax1 = fig.add_subplot(2, 2, (1, 2))

x = np.arange(len(age_groups))
w = 0.35

ax1.bar(x - w/2, df_age['Male'], w, color=MALE_CLR, label='Male', alpha=0.88)
ax1.bar(x + w/2, df_age['Female'], w, color=FEM_CLR, label='Female', alpha=0.88)

ax1.set_xticks(x)
ax1.set_xticklabels(age_groups, rotation=30, ha='right')
ax1.set_xlabel('Age Group')
ax1.set_ylabel('Population (millions)')
ax1.legend(facecolor=DARK_BG, edgecolor=GRID_CLR, labelcolor=TEXT_CLR)
style_ax(ax1, 'Population by Age Group and Gender')

# ── Plot 2: Gender Distribution ────────────────────────────────────────────
ax2 = fig.add_subplot(2, 2, 3)

bars = ax2.bar(df_gender['Gender'],
               df_gender['Population (millions)'],
               color=[MALE_CLR, FEM_CLR],
               width=0.5, alpha=0.88,
               edgecolor=DARK_BG, linewidth=1.5)

for bar, val in zip(bars, df_gender['Population (millions)']):
    ax2.text(bar.get_x() + bar.get_width()/2,
             bar.get_height() + 30,
             f'{val}M',
             ha='center', color=TEXT_CLR, fontweight='bold')

ax2.set_xlabel('Gender')
ax2.set_ylabel('Population (millions)')
ax2.set_ylim(0, 4600)
style_ax(ax2, 'Gender Distribution')

# ── Plot 3: Age Histogram (FIXED MEMORY ISSUE) ─────────────────────────────
ax3 = fig.add_subplot(2, 2, 4)

ages_expanded = np.concatenate([
    np.random.uniform(i * 5, i * 5 + 5, int(total * 2))  # reduced multiplier
    for i, total in enumerate(df_age['Total'])
])

ax3.hist(ages_expanded,
          bins=30,
          color=TOT_CLR,
          alpha=0.85,
          edgecolor=DARK_BG)

ax3.set_xlabel('Age (years)')
ax3.set_ylabel('Frequency')
style_ax(ax3, 'Age Distribution Histogram')

# ── Footer ────────────────────────────────────────────────────────────────
fig.text(0.5, 0.01,
         'Data: Simulated World Bank Population Dataset | Internship Task 01',
         ha='center', color='#8888aa', fontsize=9)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# ── SAVE FILE (WINDOWS SAFE) ───────────────────────────────────────────────
output_path = 'task1_population_distribution.png'
plt.savefig(output_path,
            dpi=150,
            bbox_inches='tight',
            facecolor=fig.get_facecolor())

print(f"Saved successfully as: {output_path}")

plt.show()
