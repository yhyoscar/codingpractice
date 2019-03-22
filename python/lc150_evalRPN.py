class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        n = len(tokens)
        if n < 3:
            return int(tokens[0])
        else:
            operator = ['+', '-', '*', '/']

            stack  = [ [int(tokens[0])],  [int(tokens[1])] ]
            k = 1
            for i in range(2,n):
                if tokens[i] in operator:
                    if tokens[i] == '+': stack[(k+1)%2][-1] += stack[k].pop()
                    if tokens[i] == '-': stack[(k+1)%2][-1] -= stack[k].pop()
                    if tokens[i] == '*': stack[(k+1)%2][-1] *= stack[k].pop()
                    if tokens[i] == '/': stack[(k+1)%2][-1] = int(stack[(k+1)%2][-1] / stack[k].pop())
                else:
                    stack[(k+1)%2].append(int(tokens[i]))

                k = (k+1) % 2
                #print(i, tokens[i], stack)
        if len(stack[0]) > 0:
            res = stack[0][-1]
        else:
            res = stack[1][-1]
        return res
        

inlist = ["-78","-33","196","+","-19","-","115","+","-","-99","/","-18","8","*","-86","-","-","16","/","26","-14","-","-","47","-","101","-","163","*","143","-","0","-","171","+","120","*","-60","+","156","/","173","/","-24","11","+","21","/","*","44","*","180","70","-40","-","*","86","132","-84","+","*","-","38","/","/","21","28","/","+","83","/","-31","156","-","+","28","/","95","-","120","+","8","*","90","-","-94","*","-73","/","-62","/","93","*","196","-","-59","+","187","-","143","/","-79","-89","+","-"]

#inlist = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
#inlist = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
#inlist = ["4","-2","/","2","-3","-","-"]


s = Solution()
print( s.evalRPN(inlist) )



