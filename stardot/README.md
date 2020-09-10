# Stardot Tools

## Push with Stressed Pull Test

One of the tests we was checking how the Stardot's push was affected by numerous heavy parallel pulls.

### 0. Machine Setup

```txt
+---------+  Push JPEG every 30s  +------------------+
| Stardot | --------------------> | Receiver Machine |
+---------+                       +------------------+
```

You'll need to know the IP address of your Stardot and receiver machine for this.

The experiment flow is as follows:

1. The Stardot reads image _from same device used by the FTP uploader_ and sends to receiver.
2. The receiver saves a timestamped image.
3. The timestamped images can be checked for timing consistency and errors.

### 1. Setup Stardot

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

chmod +x /etc/config/send-image.sh
EOF
```

Finally, add this line to `/etc/config/start` so it can run at start up.

```sh
/etc/config/send-image.sh &
```

### 2. Setup Receiver

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

### 3. Stressing Stardot

We can spin up multiple consumers pulling video data using:

```sh
seq 8 | xargs -n 1 -P 8 bash -c 'curl -s http://stardot-ip/nph-mjpeg.cgi > /dev/null'
```

This runs 8 parallel consumers pulling video data as fast as possible. Note that it is only pulling the raw video bytes and not processing the video data in any way. This is because we are primarily interested in how pulling affect the periodic push.
