<b>V2RAY Connection Limiter</b> <br>
(new and different / if you have V2 Engine panel please update codes on your server)<br>
with this python script you can specify and ban those V2ray accounts which aren't only connected to one devices. 


## running this script beside X-UI management panel
It's simple part i could do for the ppl who providing VPN for iranian users so they could selling VPN for more and more users. so 50 50 WIN WIN ! VPN providers getting money to get more Servers and many users Could get VPN as well.

so i made something for VLESS and other protocols (vmess seems blocked in iran) which you can detect those accounts which using by more than 1 IP ! this script might has some bugs and it's possible to get more power from CPU SERVER .! so check everything first and put it on background



## how it works?
it's finding connected IPs to user's Port and if more than specific IP counts are connected , it will disable that account . new file created beside main.py file. then you can run start.py file. this file show you a menu to add your specific limit Users.

it counts those IPs which connecting and downloading data in same time so it doesn't count standbyed and disconnected connections


## Guideline :
Easy Install, Copy and Paste below code to install script on your Linux os:
  ```
  bash <(curl -Ls https://raw.githubusercontent.com/Mrkoopaei/v2ray-connection-limiter/main/install.sh)
  ```
First of all you need to update and upgrade your Ubuntu Linux OS.
  On Ubuntu (need to be root user):
  ```
  sudo apt-get update & apt-get upgrade
  ```
1 - install python.
  ```
  sudo apt-get install python
  ```
2 - install pip3 then install requests, psutil and schedule packages on python<br>
  ```
  sudo apt-get install pip
  sudo pip install requests
  sudo pip install --upgrade schedule
  sudo pip install psutil
  ```
3 - install netstat (if your server doesn't have it so install it )<br>
  ```
  sudo apt-get install net-tools
  ```
4 - after install above tools you should run <b>start.py</b> file. start.py file will run main.py file automatically on background.<br>

  ```
  chmod +x start.py
  python start.py
  ```
  you can see main.py background process by running below command (it will show you all processes which started with python process name):
  ```
  sudo ps -aux | grep python
  ```
  
5 - you can set telegram bot token + your tlg chat_id for notification as well . it's pretty clear on the code .

All of the above options will be installed by running <b>INSTALL.SH</b> file. before running this bash file you should change its permission to execute on your Linux operatintg system. make sure you run this command before execute:
  ```
  chmod +x install.sh
  bash install.sh
  ```
 Or
 Altogether you can copy and past run commands :
  ```
apt-get update && apt-get upgrade
apt-get install python
apt-get install pip
pip install --upgrade schedule
pip install --root-user-action=ignore requests
pip install --root-user-action=ignore psutil
python3 start.py
  ```
 Then you should see below MENU:

Please enter your selection:
  1. Add New User to limit
  2. Delete User
  3. Show Limited User List
  4. Show V2RAY User List
  5. View blocking results 

Please select from above:

   > Adding your new V2RAY limit account remark or name by selecting 1 <br>
   > Deleting your limited V2ray account press 2 then Enter <br>
   > To show your inner limited user list press and enter 3 <br>
   > To show your X-UI accounts press and enter 4 <br>
   > Press 5 and Enter to show What happen with entered Users.

### Note: 
This script will create new DB storing your users V2ray data. that named <b>limiter.db</b>. <b>main.py</b> file will refer to your inner DB then it will detect how many IPs are using from your specific v2ray user. <br>
you can change Limits by adding new user and then define total of connection. (1 means only one device could able to connect but i suggest to set it on 3 it works great then, becuase sometimes switching between mobile data and ADSL gonna make some issues so num 3 is better .) <br><br>

New users will checked automatically during 10 minutes. <br>
> tested on this V2ray: https://seakfind.github.io/2021/10/10/X-UI/ <br>
> also tested on MHsanaei panel
