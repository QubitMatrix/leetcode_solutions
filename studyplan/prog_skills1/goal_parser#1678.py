class Solution:
    def interpret(self, command: str) -> str:
        s=""
        while(command!=""):
            if(command.startswith("G")):
                s+="G"
                command=command.replace("G","",1)
            if(command.startswith("()")):
                s+="o"
                command=command.replace("()","",1)
            if(command.startswith("(al)")):
                s+="al"
                command=command.replace("(al)","",1)
            print(command)
        return s
