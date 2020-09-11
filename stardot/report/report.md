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
count    1213.00000
mean        0.04864
std         2.36031
min        -8.00000
25%        -1.00000
50%         0.00000
75%         1.00000
max        58.00000
Name: receiver_ts, dtype: float64
```

### Top 20 largest time diffs (diff seconds)

```
345     58.0
824      5.0
456      5.0
272      5.0
121      4.0
843      4.0
933      4.0
753      4.0
243      4.0
939      4.0
1176     4.0
154      4.0
811      4.0
495      4.0
1090     4.0
124      4.0
997      4.0
517      4.0
296      4.0
359      4.0
Name: receiver_ts, dtype: float64
```

## Time diffs based on stardot_ts

### General stats (diff seconds)
```
count    1213.000000
mean        0.050289
std         2.181896
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
811      4.0
680      4.0
863      4.0
174      3.0
871      3.0
1179     3.0
342      3.0
721      3.0
256      3.0
1128     3.0
1033     3.0
968      3.0
565      3.0
824      3.0
800      3.0
193      3.0
Name: stardot_ts, dtype: float64
```

