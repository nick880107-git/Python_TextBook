import random

def gamestart():                        #產生題目的函式
    string=""                           #題目使用字串做為資料型態，方便後面做答案的比較
    for _ in range(4):                  #用迴圈產生4個0~9的整數
        num=random.randint(0,9)
        string+=str(num)                #強制型別轉換成字串，並用字串加法把四個數字串起來，存在string裡面
    return string                       #回傳string，也就是題目

def check(guess,answer):                #檢查答案是否正確的函式，參數為使用者猜的答案(guess)&正確答案(answer)
    cow=bull=0                          #宣告bull(A)跟cow(B)的值為0
    if len(guess)>4:                    #先檢查guess是不是四個數字，如果不是，列印錯誤訊息
        print("長度不正確!")
        return bull,cow                 #回傳0A0B，下面的程式碼就不執行了

    d_secret={}                         #宣告一個字典(dict)，用來表示正確答案中，每個數字的個數
    for i in answer:                    #利用for迴圈檢查正確答案中的每一個數字(參考Day2 P37)
        if i in d_secret.keys():        #如果i這個數字是字典中的key，那他的值就加一
            d_secret[i] += 1
        else:                           #如果不是，就把他加進字典中，並且設他的值為1
            d_secret[i] = 1
                                        #範例：如果正確答案是9987，在for迴圈中會依序檢查每個位置的數字，箭頭所指處即為i，{}表示目前字典內的資料變化
                                        #                  ↑     {"9":1}                (一開始字典裡沒有"9"，所以把他加入字典)
                                        #                   ↑    {"9":2}                (字典裡有"9"，所以把他的值加一，表示有2個9)
                                        #                    ↑   {"9":2,"8":1}          (字典裡沒有"8"，加入字典)
                                        #                     ↑  {"9":2,"8":1,"7":1}    (字典裡沒有"7"，加入字典)

    d_guess={}                          #宣告一個字典(dict)，用來表示使用者猜的答案中，每個數字的個數
    for i in range(len(guess)):         #因為還要比較數字的"位置"，所以這裡我們用for i in range，len(guess)表示guess的長度，也就是4
        value=guess[i]                  #用value儲存每個猜測的數字
        if value in d_secret.keys():    #比較這個數字有沒有在正確答案的字典中(使用者猜的數字有沒有在正確答案中)
            if d_secret[value]>0 :      #如果有(也就是在正確答案的字典中，那個key的值不為0)
                if answer[i]==guess[i]: #比較一下位置是不是一樣的，如果是cow(A)就加一，同時把正確答案字典中的值減一
                    bull+=1
                    d_secret[value]-=1
                else:                   #如果位置不一樣，就把它存進d_guess，代表那些數字正確，但位置錯誤的數字個數
                    if value in d_guess.keys():
                        d_guess[value]+=1
                    else:
                        d_guess[value]=1
    for k in d_guess.keys():            #最後透過迴圈檢查兩個字典剩下的東西
        if d_secret[k]>0:               #如果正確答案字典中的key有在猜測答案字典裡面且大於0
            cow+=min(d_secret[k],d_guess[k])    #計算兩者間的最小個數，累加進cow(B)裡面

    return bull,cow                     #最後回傳結果

                                        #範例：延續前面的正確答案，假設使用者輸入9998，在for迴圈中會檢查每個位置的值，箭頭所指處即為i
                                        #                                    ↑      i=0，此時value=9，9在正確答案中有出現，而且值不為0
                                        #                                           比較正確答案跟猜測答案字串中的第0個位置，都是9
                                        #                                           => A=1,d_secret={"9":1,"8":1,"7":1}
                                        #                                     ↑     i=1，此時value=9，9在正確答案中有出現，而且值不為0
                                        #                                           比較正確答案跟猜測答案字串中的第1個位置，都是9
                                        #                                           => A=2,d_secret={"9":0,"8":1,"7":1}
                                        #                                      ↑    i=2，此時value=9，9在正確答案中有出現，但值為0(表示正確答案沒有那麼多個9)
                                        #                                           => A=2,d_secret={"9":0,"8":1,"7":1},d_guess={"9":1}
                                        #                                       ↑   i=3，此時value=8，8在正確答案中有出現，而且值不為0
                                        #                                           比較正確答案跟猜測答案字串中的第3個位置，不相同(正確答案第三個位置是7，猜測答案是8)
                                        #                                           => A=2,d_secret={"9":0,"8":1,"7":1},d_guess={"9":1,"8":1}
                                        #
                                        #                                           最後透過迴圈一一檢查d_guess跟d_secret剩下的東西
                                        #                                           d_guess 9有1個，但d_secret 已經沒有9了，代表使用者猜了一個無效的數字(值和位置都不對，既不是A也不是B)
                                        #                                           d_guess 8有1個，d_secret 8有1個，取兩者最小值
                                        #                                           => B=1，代表使用者猜的數字是正確的，只是位置錯誤
                                        #                                           return 2A1B

target=gamestart()                      #呼叫函式產生題目
#print(target)
A=B=0                                   #初始化A跟B的個數
while A!=4:                             #while迴圈，還沒猜中答案前遊戲會持續下去
    number=input("請輸入四位數:")        #輸入四位數
    A,B=check(number,target)            #呼叫函式檢查答案，並取回函式回傳的A、B個數
    print("{}A{}B".format(A,B))         #使用格式化的方式印出A、B個數({}表示是一個變數，值則為.format中對應的位置)
                                        #例如，第一個{}，對應的變數即為.format的第一個參數，也就是A
                                        #這段程式碼也等同於print(A,"A",B,"B")


print("遊戲結束")                       #跳出迴圈時，遊戲結束
