# Backup Cisco config
# by John Kull 1234
 
# import modules needed and set up ssh connection parameters
import paramiko
import datetime
user = 'admin'
secret = 'bukalapak'
port = 22
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
 
# define variables
time_now  = datetime.datetime.now().strftime('%m_%d_%Y_%H_%M_%S')
infilepath = "/root/tftp"
outfilepath = "/root/tftp"
devicelist = "ip.txt"
 
# open device file
input_file = open( infilepath + devicelist, "r")
iplist = input_file.readlines()
input_file.close()

command = "copy startup-config tftp://192.168.200.102/" + str(ipaddr)+ "-" + time_now

# loop through device list and execute commands
for ip in iplist:
    ipaddr = ip.strip()
    ssh.connect(hostname=ipaddr, username=user, password=secret, port=port)
    stdin, stdout, stderr = ssh.exec_command(command)
    list = stdout.readlines()
    outfile = open(outfilepath + ipaddr + "_" + time_now, "w")
    for char in list:
        outfile.write(char)
    ssh.close()
    outfile.close()