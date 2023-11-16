#!/bin/bash
# $1 - client Id
cd /etc/openvpn/server/easy-rsa/
./easyrsa --batch --days=3650 build-client-full "$1" nopass