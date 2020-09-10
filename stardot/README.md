# Stardot Push Performance during Large Number of Pull Requests:

This test checks how the Stardot's push is affected by numerous simultanious heavy parallel pulls. The experiment flow is as follows:

1. *Reproduce NEON Image Acquisition Behavior*: Every minute, the Stardot reads an image _from same device used by the FTP uploader and Phenocam_, timestamps it and does an FTP upload to the receiver.
2. *Log Data*: The receiver run an pure-ftpd server which the Stardot uploads to.
3. *Emulate Sage Nodes*: Stress Machine spins up multiple parallel consumers pulling data from the Stardot's MJPEG endpoint. This data is simply pulled as fast as possible and discarded to stress the camera.
4. *Validation of NEON Image Stream*: The timestamped images will be checked for timing consistency and errors.

## 0. Machine Setup

```txt
+---------+  FTP upload JPEG every min  +------------------+
| Stardot | --------------------------> | Receiver Machine |
+---------+                             +------------------+
    |||
    ||| Multiple parallel
    ||| video pulls.
+----------------+
| Stress Machine |
+----------------+
```

You'll need to know the IP address of your Stardot and receiver machine for this.

## 1. Setup Stardot

First, login into your Stardot.

```sh
telnet STARDOT-IP
```

Next, add the following upload script to `/etc/config/upload-image.sh` and ensure it is executable.

```sh
#!/bin/sh -e

now=`date +%s`

cat <<EOF > /tmp/upload.scr
timeout 30
open RECEIVER-IP
user stardot stardot
passive
ascii
put /var/httpd/ip.html ip.html.tmp
rename ip.html.tmp ip.html
binary
put /dev/video/jpeg0 camera0.jpg.tmp
rename camera0.jpg.tmp "images/$now.jpg"
quit
EOF
```

Now, ensure that `/etc/config/crontab` includes the following line.

```txt
* * * * * admin /etc/config/upload-image.sh
```

Finally, we want to save the config so it persists between boots.

```sh
config save
```

## 2. Setup Receiver

My receiver is running on Ubuntu 20.04. I setup the machine as follows:

1. apt install `pure-ftpd`
2. Create `stardot` user with password `stardot`
3. Ensure `/home/stardot/images` directory exists. (This is the upload destination.)

## 3. Stressing Stardot

We can spin up multiple consumers pulling video data using:

```sh
seq 8 | xargs -n 1 -P 8 bash -c '
while true; do
  echo $(date) pulling
  curl -s http://STARDOT-IP/nph-mjpeg.cgi > /dev/null
  sleep 1
done
'
```

This runs 8 parallel consumers pulling video data as fast as possible. Note that it is only pulling the raw video bytes and not processing the video data in any way. This is because we are primarily interested in how pulling affect the periodic push.
