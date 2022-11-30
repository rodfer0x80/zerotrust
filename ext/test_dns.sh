#!/bin/sh

# should connect to PiHole for DNS resolution
host google.com 10.8.0.1

# should block as this is blacklisted advertisement website
host pagead2.googlesyndication.com

