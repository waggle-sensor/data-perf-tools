# Stardot Push Under Stress

_Although timing was very consistent in this test, a small number of images were received as blank. Because of this, this trial has been paused on we are trying an FTP based upload._

This test checks how the Stardot's push is affected by numerous simultanious heavy parallel pulls. The experiment flow is as follows:

1. Every 30s, the Stardot reads image _from same device used by the FTP uploader and Phenocam_ and sends to receiver.
2. The receiver saves timestamped images as they are received.
3. The receiver (or another machine on the network) spins up multiple parallel consumers pulling data from the Stardot's MJPEG endpoint. This data is simply pulled as fast as possible and discarded to stress the camera.
4. The timestamped images will be checked for timing consistency and errors.

## 0. Machine Setup

```txt
+---------+  Push JPEG every 30s  +------------------+
| Stardot | --------------------> | Receiver Machine |
+---------+                       +------------------+
    |||
    ||| Multiple parallel
    ||| video pulls.
+----------------+
| Stress Machine |
| (or receiver)  |
+----------------+
```

You'll need to know the IP address of your Stardot and receiver machine for this.

## 1. Setup Stardot

First, login into your Stardot.

```sh
telnet stardot-ip
```

Next, add the send image script.

```sh
cat <<EOF > /etc/config/send-image.sh
#!/bin/sh

while true; do
  cat /dev/video/jpeg0 | nc receiver-ip 10000
  sleep 30
done
EOF

chmod +x /etc/config/send-image.sh
```

Now, add this line to `/etc/config/start` so it can run at start up.

```sh
/etc/config/send-image.sh &
```

Finally, we want to save the config so it persists between boots.

```sh
config save
```

## 2. Setup Receiver

The receiver listens for incoming images and saves them.

Save the following script to `listen-for-images.sh` and chmod +x it.

```sh
#!/bin/sh

mkdir -p images

while true; do
  if nc -l 10000 > image.jpg; then
    name=images/"$(date +%s).jpg"
    mv image.jpg "$name"
    echo "added $name"
  fi
done
```

Running `./listen-for-images.sh` will start the listener and write each image received to `images/TIMESTAMP.jpg`.

## 3. Stressing Stardot

We can spin up multiple consumers pulling video data using:

```sh
seq 8 | xargs -n 1 -P 8 bash -c '
while true; do
  echo $(date) pulling
  curl -s http://stardot-ip/nph-mjpeg.cgi > /dev/null
  sleep 1
done
'
```

This runs 8 parallel consumers pulling video data as fast as possible. Note that it is only pulling the raw video bytes and not processing the video data in any way. This is because we are primarily interested in how pulling affect the periodic push.
