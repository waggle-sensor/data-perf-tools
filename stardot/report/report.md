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

A small number (<0.08%) have shown time gaps 1 minute larger than expected and may have
been caused by a failed FTP upload. Because this could have been caused by many
factors and is such a small number of examples, it's hard to attribute this to
the stress test alone. (Note that our test upload did not include any retry mechanism
but this would have likely eliminated this example.)

Finally, to be fully transparent, the Stardot's date was incorrectly set to a time
in 2019. This does not affect the analysis we did since it only depends on difference
in timestamps, however, we have still included summaries based on both the receiver
timestamp _and_ the Stardot timestamp.

## Data

The raw CSV data is provided [here](data.csv).


### Time diffs based on receiver_ts

#### General stats (diff seconds)
```
count    6843.000000
mean        0.040918
std         2.691226
min       -14.000000
50%         0.000000
90%         3.000000
99%         6.000000
99.9%      11.000000
max        58.000000
```

#### Top 20 largest time diffs (diff seconds)

```
 58.0
 54.0
 54.0
 52.0
 52.0
 13.0
 11.0
 11.0
 10.0
 10.0
 10.0
  9.0
  9.0
  9.0
  9.0
  9.0
  9.0
  9.0
  9.0
  8.0
```

### Time diffs based on stardot_ts

#### General stats (diff seconds)
```
count    6843.000000
mean        0.043987
std         2.232397
min       -11.000000
50%         0.000000
90%         2.000000
99%         4.000000
99.9%       7.158000
max        60.000000
```

#### Top 20 largest time diffs (diff seconds)

```
 60.0
 59.0
 59.0
 58.0
 57.0
 10.0
  8.0
  7.0
  6.0
  6.0
  6.0
  6.0
  5.0
  5.0
  5.0
  5.0
  5.0
  5.0
  5.0
  5.0
```

