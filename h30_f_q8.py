#!/usr/bin/env python3
# h30_f_q8.py : 基本情報技術者試験 平成30年度秋 午後問題 問8

######################################################
## グローバル値
######################################################
#文字型
Operator = [""] * 100
#整数型
OpCnt = 0
Priority = [0] * 100
Value = [0] * 100
#文字型
chr = 0
#整数型
i = 0
ip = 0
nest = 0

## compute()の引数
#文字型
Expression = [""]* 100
#整数型
Explen = 0

##入力値
Expression = "2*(34-(5+67)/8)"
Explen = 15
#Expression = "(+2)*((-3)+(-4))" #設問3 例2
#Explen = 16
#Expression = "+2*(-3+(-4))" #設問3 例3
#Explen = 12
##結果
Answer = 0

######################################################
## プログラム１
######################################################
def compute(Expression, Explen):
    compute_analysis()
    compute_calculation()

    return Value[0]

######################################################
## プログラム２
######################################################
def compute_analysis():
    global Operator
    global OpCnt
    global Value
    global nest
    global Priority
    global Value
    global chr

    for i in range(Explen):
        chr = Expression[i]
        if(('0' <= chr) and (chr <= '9')): ##数字0～9か?
            Value[OpCnt] = 10 * Value[OpCnt] + int(chr)
        elif((chr == '+') or (chr == '-') or (chr == '*') or (chr == '/')):
            Operator[OpCnt] = chr
            if((chr == '+') or (chr == '-')):
                Priority[OpCnt] = nest + 1
            else:
                Priority[OpCnt] = nest + 2
        
            OpCnt = OpCnt + 1
            Value[OpCnt] = 0

        elif(chr == '('):
            nest = nest + 10

        elif(chr == ')'):
            nest = nest - 10
    

######################################################
## プログラム３
######################################################
def compute_calculation():
    global Operator
    global OpCnt
    global Value
    global Priority
    global Value
    global chr
    global ip
    global i

    while (OpCnt > 0):
        ip = 0
        i = 1
        while(i < OpCnt):
            if(Priority[ip] < Priority[i]):
                ip = i
            i += 1

        chr = Operator[ip]

        if(chr == '+'):
            Value[ip] = Value[ip] + Value[ip + 1]
        elif(chr == '-'):
            Value[ip] = Value[ip] - Value[ip + 1]
        elif(chr == '*'):
            Value[ip] = Value[ip] * Value[ip + 1]
        elif(chr == '/'):
            Value[ip] = Value[ip] / Value[ip + 1]

        for i in range(ip + 1, OpCnt, 1):
            Value[i] = Value[i + 1]
            Operator[i - 1] = Operator[i]
            Priority[i - 1] = Priority[i]

        OpCnt = OpCnt -1


######################################################
## 実行（関数呼び出し箇所）
######################################################
Answer = compute(Expression, Explen)
print("Answer:"+ str(Answer))