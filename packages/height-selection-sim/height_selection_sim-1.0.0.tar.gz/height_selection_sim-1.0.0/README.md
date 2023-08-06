# Human height selection simulator
Simple Python program to simulate the effects of negative selection on a synthetic population of humans.

I needed a way to demonstrate how selection could work and how traits can drift over time without selection, so I made this program. It essentially initializes a random population of males and females using approximately accurate mean and standard deviation for male and female height.

For each generation, each individual is given an age-specific chance to reproduce. Parents are paired randomly. Children have heights influenced up or down from the mean depending on whether the parents are generally taller or shorter than the mean. There are hard-coded ceilings and floors for height that cause death immediately.

The generation, height, sex, and age of each individual is printed to a text file.

After reproduction, death is simulated using age-specific rates. You can specify strength of selection to apply for high or low heights, and what generation to begin applying the selection. The selection strength is multiplied by the age-specific death rate to get an individual's probability of dying. Strengths greater than 1.0 increase the likelihood of death. Strengths > 0.0 and < 1.0 would decrease the risk of death.

## Installation
You can install from PyPI using pip (preferred) or clone from GitHub and manually build. Using a Python virtual environment is highly recommended.

### Standard install
```bash
pip install height_selection_sim
```

### User install
```bash
pip install --user height_selection_sim
```

### GitHub clone
```bash
git clone https://github.com/RobersonLab/height_selection_sim.git
cd height_selection_sim
# checkout highest tagged version
pip install .
```

## Usage

##### Vanilla
Uses default parameters and outputs the height and age of each individual at each generation.
```bash
height_selection_sim
```

##### Extremely verbose output for debugging
```bash
height_selection_sim --loglevel DEBUG
```

##### Different output file name, alter starting population, apply selection after generation 100, run 200 generations, set upper height cutoff for selection, weaker selection
```bash
height_selection_sim --outfile new_out.txt --initial_population 250 --iterations 200 --upper_cutoff 180 --selection_weight 5.0
```
