
import getpass
import json
import paramiko

def run_commands(userName, userPass, machine, flow):
    port = 22
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(machine, port, userName, userPass)
    stdin, stdout, stderr = client.exec_command(';'.join(flow))
    exit_status = stdout.channel.recv_exit_status()
    lines = stdout.read().decode('ascii')
    return lines
    client.close()

def get_credentials():
    global userName 
    global userPass
    userName = labuser
    userPass = Hab12345

    #print("Enter credentials")
    #userName = input("Username: ")
    #userPass = getpass.getpass()
    #print('\n')


def run_on_list():
    global x
    global flow
    x=""

    flow = ['echo host_name', 'hostname', 'echo os_ver', 'cat /etc/os-release | grep PRETTY_NAME ', 'echo kernel_ver', 'uname -r', 'echo os_type', 'uname -s']
    
    dic = from_json_file_to_dic()
    for key in dic:
        machine = dic.get[host_name]
        x += run_commands(userName, userPass, machine, flow)
    return x

def from_json_file_to_dic():
# Opening JSON file
    with open('C:\\Users\\ozadaka\\source\\repos\\QuickCM\\jsonModel.json') as json_file:
        data = json.load(json_file)
    return data

def dump_to_json_file(dic):
    json_dic = json.dumps(dic, indent = 4)
    jsonFile = open('jsonModel.json', 'w')
    jsonFile.write(json_dic)
    jsonFile.close()


#function to get the string and trasfer it to a list
def split_string(str):
    host_list = str.split('\n')
    host_list.pop()
    return host_list

def list_to_dictionary(host_list):
  
    n = len(host_list)
    res = []
    for i in range(0, n, len(flow)):
        dict={}
        for x in range(0, len(flow), 2):
            dict[host_list[i+x]]= host_list[i+x+1]
        res.append(dict)
    dump_to_json_file(res)



if __name__ == '__main__':
    get_credentials()
    list_to_dictionary(split_string(run_on_list()))


