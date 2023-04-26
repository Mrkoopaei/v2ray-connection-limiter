v2ray-connection-limiter <br><br>
(new and different / if you have V2 please update codes on your server)<br>
with this python script you can specify and ban those V2ray accounts which aren't only connected to one devices. 

It's simple part i could do for the ppl who providing VPN for iranian users so they could selling VPN for more and more users. so 50 50 WIN WIN ! VPN providers getting money to get more Servers and many users Could get VPN as well lol. we should be togheder right ?

so i made something for VLESS and other protocols (vmess seems blocked in iran) which you can detect those accounts which using by more than 1 IP ! this script might has some bugs and it's possible to get more power from CPU SERVER .! so check everything first and put it on background

how it works ? 
it's finding connected IPs to user's Port and if more than specific IP counts are connected , it will disable that account . new file created beside main.py file. then you can run start.py file. this file show you a menu to add your specific limit Users.

it counts those IPs which connecting and downloading data in same time so it doesn't count standbyed and disconnected connections

<b>Install Guide :</b><br>
1 - install python .<br>
2 - pip3 install requests and pip3 install schedule<br>
3 - install netstat (if your server doesn't have it so install it - debian : apt install net-tools)<br>
4 - put it on background => nohup python3 main.py &  (without background process : python3 main.py) it will start when you run Install.sh bash file<br>
5 - you can set telegram bot token + your tlg chat_id for notification as well . it's pretty clear on the code .

All of the above options will be installed by running INSTALL.SH file. before running this bash file you should change its permission to execute on your Linux operatintg system. make sure you run this command --> chmod +x /path/install.sh
<br>
<b><h4>Note: </h4></b><br>
this script will create new DB storing your users V2ray data. that named limiter.db. main.py file will refer to your inner DB then it will detect how many IPs are using from your specific v2ray user.
you can change Limits by adding new user and then define total of connection. (1 means only one device could able to connect but i suggest to set it on 3 it works great then, becuase sometimes switching between mobileData and ADSL gonna make some issues so num 3 is better .)

<b>Note: </b> : in v2 new users will checked automatically

tested on this V2ray: https://seakfind.github.io/2021/10/10/X-UI/
