#!/usr/bin/env bash
apt-get --assume-yes update
apt-get --assume-yes upgrade
termux-setup-storage
# Install required pks
pkg --assume-yes install bc jq curl wget vim python
# Python related.
apt-get --assume-yes install python-dev
pip install --upgrade pip
# More on python (this is needed in order to get numpy, scipy, etc.)
curl -L https://its-pointless.github.io/setup-pointless-repo.sh | sh
pkg --assume-yes install scipy
# Get dotenv and requests.
pip install -U python-dotenv
pip install requests==2.3
