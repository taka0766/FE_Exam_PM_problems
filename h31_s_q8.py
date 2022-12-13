#!/usr/bin/env python3
# h31_s_q8.py : 基本情報技術者試験 平成31年度春 午後問題 問8

######################################################
## グローバル値（Huffmanの引数）⇒入力であり出力
######################################################
##1.まずは初期化(すべてを-1で初期化)
size = 0     #節の個数
parent = [-1] * 7 #節の親を表す要素組の要素番号を格納した配列
left   = [-1] * 7   #節の左側の子を表す要素組の要素番号を格納した配列
right  = [-1] * 7  #節の右側の子を表す要素組の要素番号を格納した配列
freq   = [-1] * 7   #節の値を格納した配列

nsize = 0

##2.前提説明の文字列をfreqに設定する
###文字列:AAAABBCDCDDACCAAAAA
###出現回数: A:10個　B:2個 C:4個 D:3個
size = 4     #節の個数
freq = [10, 2 ,4, 3, 0, 0, 0]
node = [0] * 7 #子と親の節を足した数をnode初期値とする

######################################################
## グローバル値（Encodeの引数）
######################################################
k = 1

######################################################
## プログラム１－１
######################################################
#def Huffman(size, parent, left, right, freq):
def Huffman():
    #グローバル変数
    global size
    global parent
    global left
    global right
    global size

    #ローカル変数初期化
    i =0
    j =0

#    SortNode(size, parent, freq, nsize, node)
    SortNode()
    while(nsize >= 2): #設問2 c
        i = node[0] #最も小さい値を持つ要素組の要素番号
        j = node[1] #２番目に小さい値を持つ要素組の要素番号
        left[size] = i
        right[size] = j
        freq[size] = freq[i] + freq[j]  #子の値の合計
        parent[i] = size #子に親の節の要素番号を格納
        parent[j] = size #子に親の節の要素番号を格納
        size = size + 1
#        SortNode(size, parent, freq, nsize, node)
        SortNode()

######################################################
## プログラム１－２
######################################################
#def SortNode(size, parent, freq, nsize, node):
def SortNode():
    #グローバル変数
    global size
    global parent
    global freq
    global nsize
    global node
    #ローカル変数初期化
#    nsize = 0

    for i in range(size):
        if(parent[i] < 0): #設問2 d
            node[nsize] = i
            nsize = nsize + 1
#    Sort(freq, nsize, node)
    Sort()

######################################################
## プログラム１－３
######################################################
#def Sort(freq, nsize, node):
def Sort():
    #グローバル変数
    global freq
    global nsize
    global node

    #ToDO:node配列をfreq配列の値で昇順にソートする
    ##一時的に、freqをkeyにした辞書（連想配列）を作る
    tmp_dict = {freq[i]:node[i] for i in range(nsize)}
    print(tmp_dict)
    ##key（freq）により、辞書を昇順ソート
    sorted_tmp_dict = dict(sorted(tmp_dict.items()))
    print(sorted_tmp_dict)

    #値（node）を取り出して、再格納する
    node = list(sorted_tmp_dict.values())
    print(node)
    
######################################################
## プログラム２
######################################################
#def Encode(k, parent, left):
def Encode():
    #グローバル変数
    global k
    global parent
    global left
    #ローカル変数初期化
    left= []
    if(parent[k] >= 0): #設問3 e
#        Encode(parent[k], parent, left)
        Encode()
        if(left[parent[k]] == k):
            print("0")
        else:
            print("1")

######################################################
## 実行（関数呼び出し箇所）
######################################################
#Huffman(size, parent, left, right, freq)
#Encode(k, parent, left)
Huffman()
Encode()

    
