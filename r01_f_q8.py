#!/usr/bin/env python3
# r01_f_q8.py : 基本情報技術者試験 令和元年度秋 午後問題 問8

######################################################
## グローバル値
######################################################
Text = "AACBBAACABABAB"  # 対象文字列１(一致パターンあり)
#Text = "AACBBAACABACAB" # 対象文字列２(一致パターンなし)
Pat  = "ACABAB"         # 検索文字列１
#Pat = "AC[BA]A[ABC]A"   # 検索文字列２(正規表現版)  ※不一致パターン（設問記載はこちら。）
#Pat = "AC[BA]B[ABC]B"    # 検索文字列３(正規表現版) ※一致パターン
#Pat = "AC[B[AB]AC]A"     # 検索文字列４ #設問3-i 

Mask = {'A':0b1,'B':0b1,'C':0b1,'D':0b1,'E':0b1,
        'F':0b1,'G':0b1,'H':0b1,'I':0b1,'J':0b1,
        'K':0b1,'L':0b1,'M':0b1,'N':0b1,'O':0b1,
        'P':0b1,'Q':0b1,'R':0b1,'S':0b1,'T':0b1,
        'U':0b1,'V':0b1,'W':0b1,'X':0b1,'Y':0b1,
        'Z':0b1}          # Mask(変数生成用)

PatLen:int
BIT_OPE_OFFSET = 1        #pythonのリスト添え字開始が０により、問題意図とずれるため、苦肉の策でオフセットをとる


######################################################
## プログラム１
######################################################
def GenerateBitMask(Pat, Mask):

    PatLen = len(Pat)   #Patの文字数

    for key in Mask:
        #初期化
        Mask[key] =  0b0 #設問1 b

    for i in range(PatLen):
        Pat[i]
        if Pat[i] in Mask:
            #"1B"を(i-1)ビットだけ論理左シフトした値とのビット毎論理和
            #苦肉の策でオフセットの+1を添える
            Mask[Pat[i]] = Mask[Pat[i]] | (0b1<<(i - 1 + BIT_OPE_OFFSET))  #設問1-c
            bin(Mask[Pat[i]])

    return PatLen


######################################################
## プログラム２
######################################################
def BitapMatch(Text, Pat):
    Goal = 0b0
    Status = 0b0

    TextLen = len(Text)
    PatLen = GenerateBitMask(Pat, Mask)
#    PatLen = GenerateBitMaskRegex(Pat, Mask)

    Status = 0b0
    Goal = 0b1<<(PatLen-1)
    
    for i in range(TextLen):
        Status = Status<<1 | 0b1 #設問2 α
        bin(Status)
        Status = Status & Mask[Text[i]] #設問2 β
        bin(Status)

        if (Status & Goal) != 0b0:
            return (i - PatLen + 1)
     
    return -1


######################################################
## プログラム３
######################################################
def GenerateBitMaskRegex(Pat, Mask):

    OriginalPatLen = len(Pat) #Patの文字数
    PatLen = 0
    Mode = 0

    for key in Mask:
        #初期化
        Mask[key] = 0b0 #設問3-b

    for i in range(OriginalPatLen):
        if Pat[i] == "[":
            Mode = 1
            PatLen = PatLen + 1
            continue

        elif Pat[i] == "]":
            Mode = 0
            continue

        if Mode == 0:
            PatLen = PatLen + 1

        #"1B"を(PatLen - 1)ビットだけ論理左シフトした値とMask[Index(Pat[i])]のビット毎論理和
        Mask[Pat[i]] = Mask[Pat[i]] | (0b1<<(PatLen - 1))
        bin(Mask[Pat[i]])

    return PatLen  #設問3-h



######################################################
## 実行（関数呼び出し箇所）
######################################################
#GenerateBitMask(Pat, Mask)
#GenerateBitMaskRegex(Pat, Mask)
BitapMatch(Text, Pat)


    
