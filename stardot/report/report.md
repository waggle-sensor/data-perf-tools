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
count    1220.000000
mean        0.047541
std         2.356504
min        -8.000000
25%        -1.000000
50%         0.000000
75%         1.000000
max        58.000000
Name: receiver_ts, dtype: float64
```

### Top 20 largest time diffs (diff seconds)

```
346     58.0
829      5.0
459      5.0
273      5.0
121      4.0
848      4.0
938      4.0
757      4.0
244      4.0
944      4.0
1183     4.0
155      4.0
816      4.0
498      4.0
1095     4.0
124      4.0
1002     4.0
520      4.0
297      4.0
360      4.0
Name: receiver_ts, dtype: float64
```

## Time diffs based on stardot_ts

### General stats (diff seconds)
```
count    1220.000000
mean        0.048361
std         2.179806
min        -6.000000
25%        -1.000000
50%         0.000000
75%         1.000000
max        59.000000
Name: stardot_ts, dtype: float64
```

### Top 20 largest time diffs (diff seconds)

```
346     59.0
360      5.0
75       4.0
155      4.0
816      4.0
684      4.0
868      4.0
175      3.0
876      3.0
1186     3.0
343      3.0
725      3.0
257      3.0
1133     3.0
1038     3.0
973      3.0
568      3.0
829      3.0
804      3.0
194      3.0
Name: stardot_ts, dtype: float64
```

