# script for launching vpn with notification
if nmcli c show | grep "\--" # grep exit code check
then nmcli c up vpn ; notify-send "🔮 VPN on" -t 4000 # enable and show notification
else nmcli c down vpn ; notify-send "🟥 VPN off" -t 4000 # disable and show notification
fi