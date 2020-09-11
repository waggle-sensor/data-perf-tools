# Stress Test Report

This is a summary of the major stats about timing between consecutive image pushes.

All times differences are measured as "seconds off from the expected 1/min
interval". For example, two images received at 10:31:05 and 10:32:07 will
be presented as a time difference of +2 seconds. Negative values are allowed
if an image arrives earlier than expected.

To be fully transparent, the Stardot's date was incorrectly set to a time in 2019.
Strictly speaking, this does not affect the analysis we're doing, since it only depends
on time between timestamps. However, we have decided to include summaries based on both
the receiver timestamp _and_ the Stardot timestamp.

Each summary contains two items:

* General stats including number of images, mean, std of the time between pushes.
* Top 20 largest times between pushes intended to help understand the worst case.

Collected images are not included here but they have all been manually checked for
errors and none was found.

Finally, exactly _one_ out of the >1200 time gaps was 1 minute larger than expected
and may have been caused by a failed FTP upload. Our test upload did not include
any retry mechanism but this would have likely eliminated this example.

## Time diffs based on receiver_ts

### General stats (diff seconds)
```
count    1211.000000
mean        0.047894
std         2.362101
min        -8.000000
25%        -1.000000
50%         0.000000
75%         1.000000
max        58.000000
Name: receiver_ts, dtype: float64
```

### Top 20 largest time diffs (diff seconds)

```
345     58.0
822      5.0
456      5.0
272      5.0
121      4.0
841      4.0
931      4.0
751      4.0
243      4.0
937      4.0
1174     4.0
154      4.0
809      4.0
495      4.0
1088     4.0
124      4.0
995      4.0
517      4.0
296      4.0
359      4.0
Name: receiver_ts, dtype: float64
```

## Time diffs based on stardot_ts

### General stats (diff seconds)
```
count    1211.000000
mean        0.049546
std         2.183527
min        -6.000000
25%        -1.000000
50%         0.000000
75%         1.000000
max        59.000000
Name: stardot_ts, dtype: float64
```

### Top 20 largest time diffs (diff seconds)

```
345     59.0
359      5.0
75       4.0
154      4.0
809      4.0
678      4.0
861      4.0
174      3.0
869      3.0
1177     3.0
342      3.0
719      3.0
256      3.0
1126     3.0
1031     3.0
966      3.0
565      3.0
822      3.0
798      3.0
193      3.0
Name: stardot_ts, dtype: float64
```

