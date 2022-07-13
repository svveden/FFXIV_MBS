# FFXIV_MBS
Bot for Final Fantasy XIV market-board scalping

This is a script for finding large percentage differences between the same items listed on the FFXIV marketboard on different worlds within the same Data Center.

In theory, this bot should find large price differences of items between worlds to allow for scalping.

Currently, this runs in console with very few features, but I plan on implementing more features such as:
More world price comparisons, sorting, higher sold items appearing first, etc.

This bot is for comparing items against Ultros' (my home server) marketboard.

As of right now, this bot has the following output:
Item Name
Ultros:  # Gil Quantity: #
Famfrit: # Gil Quantity: #
Exodus:  # Gil Quantity: #
Current Sale Velocity:  #
% #  difference in price between minimum and Ultros

Usage:

Clone and run:

```python3 FFXIV_MBS.py```

in the same folder as the other .json files
