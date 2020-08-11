# Camera Tools

## display.py

Tool for rendering camera frames as fast as possible. This is intended to:

1. Get a more direct measure of how well OpenCV gets data.
2. Bypass ffplay which, by default, has vrey high latency when playing back video. (There are probably buffering settings we should figure out...)

## fps_profile.py

Tool to profile FPS when a number of consumers are pulling as fast as possible.

## sampler.py

Tool which logs time when frames were received when a number of consumers are pulling as fast as possible. (fps_profile.py is probably what you want, but this allows for more sophisiticated data analysis, if needed.)
