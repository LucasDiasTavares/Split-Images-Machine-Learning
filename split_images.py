"""
pip install split-folders
"""

import splitfolders

input_folder = 'images_input'
output_folder = 'images_output'

# Split with a ratio.
# To only split into training and validation set, set a tuple to `ratio`, i.e, `(.8, .2)`.
Train = .7
validation = .2
test = .1
splitfolders.ratio(input_folder, output=output_folder, seed=42, ratio=(Train, validation, test),group_prefix=None)


# Split val/test with a fixed number of items e.g. 100 for each set.
# To only split into training and validation set, use a single number to `fixed`, i.e., `10`.
# enable oversampling of imbalanced datasets, works only with fixed
splitfolders.fixed(input_folder, output=output_folder, seed=42, fixed=(35, 20), oversample=False, group_prefix=None)
