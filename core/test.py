
from terminal import Terminal
from modules_handler import ModHandler

class Test:
    
    commands = [
                
                ":audit.user_files .profile",
                ":file.upload /etc/passwd ./prova/test",
                ":file.check prova/test exists",
                "rm prova/test",
                ":file.check prova/test r",
#                ":audit.user_web_files /var/www http://localhost/",
                ":audit.users",
                ":enum.binaries telnet",
#                ":enum.paths /home/norby/prov",
                 ":system.info auto",
                 
                ]
    
    def run(self, url, password):
        
        for cmd in self.commands:
               
            print '\n=========== Running \'%s\' test\n' % cmd
               
            try:
                
                terminal = Terminal (ModHandler(url, password), True)
                if cmd[0] == terminal.module_char:
                    terminal.run_module_cmd(cmd.split())
                else:
                    terminal.run_line_cmd(cmd)
                    
            except KeyboardInterrupt:
                print '\n[!] Exiting. Bye ^^'