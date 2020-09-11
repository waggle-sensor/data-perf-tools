# Stress Test Report

## Overview

This is a summary of the major stats about timing between consecutive image pushes.

All times differences are measured as "seconds off from the expected 1/min
interval". For example, two images received at 10:31:05 and 10:32:07 will
be presented as a time difference of +2 seconds. Negative values are allowed
if an image arrives earlier than expected.

Each summary contains two items:

* General stats including number of images, mean, std of the time between pushes.
* Top 20 largest times between pushes intended to help understand the worst case.

## Results

The results are very promising. The push timing seems to be unaffected in a
significant way by the consumers stress testing the video endpoint. Most timing
differences with within a few seconds of the expected 1/min push.

Images have also been manually checked and no errors were found.

Exactly _one_ out of the >1200 time gaps was 1 minute larger than expected and may have
been caused by a failed FTP upload. Because this could have been caused by many
factors and is a single example, it's hard to attribute this to the stress test
alone. (Note that our test upload did not include any retry mechanism but this
would have likely eliminated this example.)

Finally, to be fully transparent, the Stardot's date was incorrectly set to a time
in 2019. This does not affect the analysis we did since it only depends on difference
in timestamps, however, we have still included summaries based on both the receiver
timestamp _and_ the Stardot timestamp.

## Data

The raw CSV data is provided [here](data.csv).


### Time diffs based on receiver_ts

#### General stats (diff seconds)
```
count    1229.000000
mean        0.048007
std         2.349053
min        -8.000000
25%        -1.000000
50%         0.000000
75%         1.000000
max        58.000000
Name: receiver_ts, dtype: float64
```

#### Top 20 largest time diffs (diff seconds)

```
349     58.0
836      5.0
464      5.0
275      5.0
123      4.0
855      4.0
945      4.0
764      4.0
246      4.0
951      4.0
1191     4.0
157      4.0
823      4.0
503      4.0
1102     4.0
126      4.0
1009     4.0
525      4.0
300      4.0
363      4.0
Name: receiver_ts, dtype: float64
```

### Time diffs based on stardot_ts

#### General stats (diff seconds)
```
count    1229.000000
mean        0.048820
std         2.173102
min        -6.000000
25%        -1.000000
50%         0.000000
75%         1.000000
max        59.000000
Name: stardot_ts, dtype: float64
```

#### Top 20 largest time diffs (diff seconds)

```
349     59.0
363      5.0
77       4.0
157      4.0
823      4.0
690      4.0
875      4.0
177      3.0
883      3.0
1194     3.0
346      3.0
731      3.0
259      3.0
1141     3.0
1045     3.0
980      3.0
573      3.0
836      3.0
811      3.0
196      3.0
Name: stardot_ts, dtype: float64
```

