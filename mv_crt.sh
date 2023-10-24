#!/bin/bash

serial=$1
client=$2

crt_dir="/etc/openvpn/server/easy-rsa/pki/issued/"
req_dir="/etc/openvpn/server/easy-rsa/pki/reqs/"
key_dir="/etc/openvpn/server/easy-rsa/pki/private/"

revoked_crt_dir="/etc/openvpn/server/easy-rsa/pki/revoked/certs_by_serial/"
revoked_req_dir="/etc/openvpn/server/easy-rsa/pki/revoked/reqs_by_serial/"
revoked_key_dir="/etc/openvpn/server/easy-rsa/pki/revoked/private_by_serial/"

mv "${revoked_crt_dir}${serial}.crt" "${crt_dir}${client}.crt"
mv "${revoked_req_dir}${serial}.req" "${req_dir}${client}.req"
mv "${revoked_key_dir}${serial}.key" "${key_dir}${client}.key"