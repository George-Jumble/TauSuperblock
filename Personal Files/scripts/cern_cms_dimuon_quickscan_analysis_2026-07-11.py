import numpy as np
import matplotlib.pyplot as plt
import json

# Load data
with open('/home/workdir/attachments/cern_analysis__cern_analysis__report__07-11-2026_121033.json') as f:
    data = json.load(f)

hist_counts = np.array(data['muon_pt_histogram'])
bin_indices = np.arange(len(hist_counts))

fig, ax = plt.subplots(figsize=(12, 7))

# Bar plot with log y for dynamic range
bars = ax.bar(bin_indices, hist_counts, color='#2ca02c', edgecolor='black', alpha=0.8, width=0.9)

ax.set_yscale('log')
ax.set_xlabel('Muon pT Bin Index (0 = lowest pT bin → 19 = highest)', fontsize=12)
ax.set_ylabel('Number of Muons (log scale)', fontsize=12)
ax.set_title('CMS 2012 DoubleMuParked Dataset\nMuon pT Distribution (First 50,000 Events)\n'
             f"Mean pT ≈ {data['Muon_pt_mean']:.2f} GeV | Max pT = {data['Muon_pt_max']:.1f} GeV | Total Muons = {sum(hist_counts):,}",
             fontsize=13)

# Add stats text box
stats_text = (f"nMuon mean = {data['nMuon_mean']:.3f}\n"
              f"nMuon max = {int(data['nMuon_max'])}\n"
              f"Events processed = {data['entry_stop']:,}\n"
              f"Branches: {', '.join(data['branches_read'])}")
ax.text(0.98, 0.95, stats_text, transform=ax.transAxes, fontsize=10,
        verticalalignment='top', horizontalalignment='right',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

# Highlight first and last bins
ax.annotate(f'First bin: {hist_counts[0]:,} muons\n(low pT)', xy=(0, hist_counts[0]), 
            xytext=(2, hist_counts[0]*3), fontsize=9, arrowprops=dict(arrowstyle='->', color='blue'))
ax.annotate(f'Last bin: {hist_counts[-1]} muons\n(high pT tail)', xy=(19, hist_counts[-1]), 
            xytext=(15, hist_counts[-1]*10), fontsize=9, arrowprops=dict(arrowstyle='->', color='red'))

ax.grid(True, which='both', alpha=0.3)
ax.set_xticks(bin_indices[::2])  # every other tick for clarity

plt.tight_layout()
plt.savefig('/home/workdir/artifacts/personal_files/cern_cms_muon_pt_histogram_2026-07-11.png', dpi=150, bbox_inches='tight')
print("Histogram plot saved successfully!")
