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


### Time diffs based on receiver_ts

#### General stats (diff seconds)
```
count    1227.000000
mean        0.048085
std         2.350968
min        -8.000000
25%        -1.000000
50%         0.000000
75%         1.000000
max        58.000000
Name: receiver_ts, dtype: float64
```

#### Top 20 largest time diffs (diff seconds)

```
348     58.0
834      5.0
462      5.0
275      5.0
123      4.0
853      4.0
943      4.0
762      4.0
246      4.0
949      4.0
1189     4.0
157      4.0
821      4.0
501      4.0
1100     4.0
126      4.0
1007     4.0
523      4.0
299      4.0
362      4.0
Name: receiver_ts, dtype: float64
```

### Time diffs based on stardot_ts

#### General stats (diff seconds)
```
count    1227.000000
mean        0.049715
std         2.174666
min        -6.000000
25%        -1.000000
50%         0.000000
75%         1.000000
max        59.000000
Name: stardot_ts, dtype: float64
```

#### Top 20 largest time diffs (diff seconds)

```
348     59.0
362      5.0
77       4.0
157      4.0
821      4.0
688      4.0
873      4.0
177      3.0
881      3.0
1192     3.0
345      3.0
729      3.0
259      3.0
1139     3.0
1043     3.0
978      3.0
571      3.0
834      3.0
809      3.0
196      3.0
Name: stardot_ts, dtype: float64
```

