import paramiko
from os import environ as env

def worker_handler():
    k = paramiko.RSAKey.from_private_key_file("jai-cloudwatt-fr2.pem")
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    host=env['TESTING_HOST_IP']

    c.connect( hostname = host, username = "cloud", pkey = k )
    print "Connected to " + host

    commands = [
        "hostname",
        "pwd"

        ]
    commands_result = [
        "ubuntu",
        "/home/cloud"

        ]
    for cindex,command in enumerate(commands):
        print "Testing {}".format(command)
        stdin , stdout, stderr = c.exec_command(command)
        command_result =  stdout.read().strip()
        command_expect =  commands_result[cindex]
        if command_result == command_expect: print "OK"
        else: print "Fail => ", command_result, " : ", command_expect
        print stderr.read()

    return
    {
        'message' : "Script execution completed. See Cloudwatch logs for complet                                                                                                                e output"
    }

if __name__ == "__main__":
    worker_handler()
