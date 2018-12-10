#!bin/bash
#TEC DROID
clear

apt install figlet
echo -e "\e[1;36m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\e[1;32m"
figlet ..TEC DROID..
echo -e "\e[1;36m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\e[0m"
sleep 3
#Instalando
echo -e "\e[1;32m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\e[1;31m"
figlet UPDATE
echo -e "\e[1;32m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\e[0m"
sleep 3
apt update && apt upgrade -y

#Descargando complementos
echo -e "\e[1;34m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\e[1;32m"
figlet PYTHON2
echo -e "\e[1;34m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&%%%%%%\e[0m"
sleep 3
pkg install python2
echo -e "\e[1;31mINSTALADO,ESPERE UN MOMENTO...!!\e[0m"
sleep 3

#Instalado
echo -e "\e[1;33m%%%%%%%%%%%%%%%%%\e[1;32m"
figlet GIT
echo -e "\e[1;33m%%%%%%%%%%&%%%%%%\e[0m"
sleep 3
pkg install git
echo -e "\e[1;31mINSTALACION EXITOSA!!!\e[0m"
sleep 3

#Script
git clone https://github.com/jhery625/tec-droid-scan
#Final
echo -e "\e[1;34m%%%%%%%%%%%%%%%%%%%%%%&%%\e[1;31m "
figlet ..FIN..
echo -e "\e[1;34m%%%%%%%%%%%%%%%%%%%%%%%%%\e[0m"
sleep 1
echo -e "\033[1;35mSIGA LOS SIGUIENTES PASOS :\e[0m"
echo -e "\033[1;32m[ 1 ]\033[1;36m (DIGITE)\033[1;33m ==> ls"
echo -e "\033[1;32m[ 2 ]\033[1;31m (DIGITE)\033[1;36m ==> cd tec-droid-scan"
echo -e "\033[1;32m[ 3 ]\033[1;32m (DIGITE)\033[1;34m ==> ls"
echo -e "\033[1;32m[ 1 ]\033[1;35m (DIGITE)\033[1;33m ==> python2 TEC DROID SCANN.py"