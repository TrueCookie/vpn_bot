#!/bin/bash
# Generates the custom client_script_gen.ovpn
{
cat /etc/openvpn/server/client-common.txt
echo "<ca>"
cat /etc/openvpn/server/easy-rsa/pki/ca.crt
echo "</ca>"
echo "<cert>"
sed -ne '/BEGIN CERTIFICATE/,$ p' /etc/openvpn/server/easy-rsa/pki/issued/"client_script_gen".crt
echo "</cert>"
echo "<key>"
cat /etc/openvpn/server/easy-rsa/pki/private/"client_script_gen".key
echo "</key>"
echo "<tls-crypt>"
sed -ne '/BEGIN OpenVPN Static key/,$ p' /etc/openvpn/server/tc.key
echo "</tls-crypt>"
} > ~/"client_script_gen".ovpn
