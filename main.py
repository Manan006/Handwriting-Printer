from PIL import Image
from Enter import inpt
import numpy as np
background = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\BACKGROUND.png")
spacing = 1
number=0
class_helper=" "
def transparent(img):
    img = img.convert("RGBA")
    datas = img.getdata()

    newData = []
    for item in datas:
        opacity=item[3]
        #print ("transparent: ",item)
        if opacity<50:
            newData.append((color1, color2, color3, opacity))
        elif item[0]<75 and item[1]<75 and item[2]<75:
            newData.append((color1, color2, color3, opacity))
        else:newData.append(item)

    img.putdata(newData)
    return img

def breadth_(val,breath):
    w, h = val.size
#    breath+=w
    #print (breath)
    return w




def breaker(text):
    #text=text.upper()
    text=list(str(text))
    broke=[]
    for i in range(len(text)):
        broke.append(text[i])
    broke.append(class_helper)
    return broke

length = 5
length_no=0

counter=0
def worder(text):
    #counter=0
    reg=[0]
    number=len(text)
    number-=1
    #print ("worder starts")
    for i in enumerate(text):
        print ("text: ",text)
        if i[1] in ' !#$(),."-@[]^`{}~+=:<?>;/*':
            #print ("i: ",i)
            #print("c: ",counter)
            #print("item: ",i[0])
            counter= i[0]
            counter+=1
            #word=text[counter:i[0]]
            print ("counter: ",counter)
            print ("number: ",i[1],"i: ",i[0])
            reg.append(counter)
        #elif number==i[0]:
        #    counter= number
        #    print ("number was = 0")
        #    counter+=1
        #    reg.append(counter)
    if len(reg)%2==1:
            no=i[0]+1
            reg.append(no)

            #print(word)
            #print ("==============================================")
    return reg


while True:
    inp=inpt()
    color1=inp[0]
    color2=inp[1]
    color3=inp[2]
    color1=str(color1)
    color2=str(color2)
    color3=str(color3)
    #print (color1,color2,color2)
    color1=color1.zfill(3)
    color2=color2.zfill(3)
    color3=color3.zfill(3)
    color1=int(color1)
    color2=int(color2)
    color3=int(color3)
    #print (color1,color2,color3)
    inp=inp[3]
    #print (inp)
    inp=breaker(inp)
    #print (inp)
    breath=5

    reg = worder(inp)
    print (inp)
    print("reg: ", reg)
    word_no=0.0
    print ("reg length: ",len(reg))
    if len(reg)>2:
        word_no=len(reg)-2
    else:
        word_no=1
    #if len(reg)%2==1:
    #    word_no+=1
    word_no=int(word_no)
    print ("word_no: ",word_no)
    if word_no>1:
        word_no+=1
    for L in range(word_no):
        if len(reg)>1:
            word = reg[0:2]
            print ("Worder: ",word)
        else :print("len<0")
        #print ("reg before: ",reg)
        #print ("reg[1]: ",reg[1])
        if len(reg)>1:
            reg.remove(reg[0])
        #print ("reg after: ",reg)
        #print (word)
        if len(word)>1:
            worded=inp[word[0]:word[1]]
        print ("Worded: ",worded)

        #print ("Word: ",worded)
        pre_breath=0
        for key in worded:
            if key == "A":
                Aal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\A.png")
                Aal = Aal.resize((round(Aal.size[0] * 0.090), round(Aal.size[1] * 0.090)))
                pre_breath+=breadth_(Aal,pre_breath)
                pre_breath+=spacing
            elif key == "B":
                Bal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\B.png")
                Bal = Bal.resize((round(Bal.size[0] * 0.090), round(Bal.size[1] * 0.090)))
                pre_breath+=breadth_(Bal,pre_breath)
                pre_breath+=spacing
            elif key == "C":
                Cal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\C.png")
                Cal = Cal.resize((round(Cal.size[0] * 0.090), round(Cal.size[1] * 0.090)))
                pre_breath+=breadth_(Cal,pre_breath)
                pre_breath+=spacing
            elif key == "D":
                Dal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\D.png")
                Dal = Dal.resize((round(Dal.size[0] * 0.090), round(Dal.size[1] * 0.090)))
                pre_breath+=breadth_(Dal,pre_breath)
                pre_breath+=spacing
            elif key == "E":
                Eal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\E.png")
                Eal = Eal.resize((round(Eal.size[0] * 0.090), round(Eal.size[1] * 0.090)))
                pre_breath+=breadth_(Eal,pre_breath)
                pre_breath+=spacing
            elif key == "F":
                Fal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\F.png")
                Fal = Fal.resize((round(Fal.size[0] * 0.090), round(Fal.size[1] * 0.090)))
                pre_breath+=breadth_(Fal,pre_breath)
                pre_breath+=spacing
            elif key == "G":
                Gal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\G.png")
                Gal = Gal.resize((round(Gal.size[0] * 0.090), round(Gal.size[1] * 0.090)))
                pre_breath+=breadth_(Gal,pre_breath)
                pre_breath+=spacing
            elif key == "H":
                Hal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\H.png")
                Hal = Hal.resize((round(Hal.size[0] * 0.090), round(Hal.size[1] * 0.090)))
                pre_breath+=breadth_(Hal,pre_breath)
                pre_breath+=spacing
            elif key == "I":
                Ial = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\I.png")
                Ial = Ial.resize((round(Ial.size[0] * 0.090), round(Ial.size[1] * 0.090)))
                pre_breath+=breadth_(Ial,pre_breath)
                pre_breath+=spacing
            elif key == "J":
                Jal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\J.png")
                Jal = Jal.resize((round(Jal.size[0] * 0.090), round(Jal.size[1] * 0.090)))
                pre_breath+=breadth_(Jal,pre_breath)
                pre_breath+=spacing
            elif key == "K":
                Kal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\K.png")
                Kal = Kal.resize((round(Kal.size[0] * 0.090), round(Kal.size[1] * 0.090)))
                pre_breath+=breadth_(Kal,pre_breath)
                pre_breath+=spacing
            elif key == "L":
                Lal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\L.png")
                Lal = Lal.resize((round(Lal.size[0] * 0.090), round(Lal.size[1] * 0.090)))
                pre_breath+=breadth_(Lal,pre_breath)
                pre_breath+=spacing
            elif key == "M":
                Mal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\M.png")
                Mal = Mal.resize((round(Mal.size[0] * 0.090), round(Mal.size[1] * 0.090)))
                pre_breath+=breadth_(Mal,pre_breath)
                pre_breath+=spacing
            elif key == "N":
                Nal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\\N.png")
                Nal = Nal.resize((round(Nal.size[0] * 0.090), round(Nal.size[1] * 0.090)))
                pre_breath+=breadth_(Nal,pre_breath)
                pre_breath+=spacing
            elif key == "O":
                Oal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\O.png")
                Oal = Oal.resize((round(Oal.size[0] * 0.090), round(Oal.size[1] * 0.090)))
                pre_breath+=breadth_(Oal,pre_breath)
                pre_breath+=spacing
            elif key == "P":
                Pal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\P.png")
                Pal = Pal.resize((round(Pal.size[0] * 0.090), round(Pal.size[1] * 0.090)))
                pre_breath+=breadth_(Pal,pre_breath)
                pre_breath+=spacing
            elif key == "Q":
                Qal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\Q.png")
                Qal = Qal.resize((round(Qal.size[0] * 0.090), round(Qal.size[1] * 0.090)))
                pre_breath+=breadth_(Qal,pre_breath)
                pre_breath+=spacing
            elif key == "R":
                Ral = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\R.png")
                Ral = Ral.resize((round(Ral.size[0] * 0.090), round(Ral.size[1] * 0.090)))
                pre_breath+=breadth_(Ral,pre_breath)
                pre_breath+=spacing
            elif key == "S":
                Sal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\S.png")
                Sal = Sal.resize((round(Sal.size[0] * 0.090), round(Sal.size[1] * 0.090)))
                pre_breath+=breadth_(Sal,pre_breath)
                pre_breath+=spacing
            elif key == "T":
                Tal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\T.png")
                Tal = Tal.resize((round(Tal.size[0] * 0.090), round(Tal.size[1] * 0.090)))
                pre_breath+=breadth_(Tal,pre_breath)
                pre_breath+=spacing
            elif key == "U":
                Ual = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\U.png")
                Ual = Ual.resize((round(Ual.size[0] * 0.090), round(Ual.size[1] * 0.090)))
                pre_breath+=breadth_(Ual,pre_breath)
                pre_breath+=spacing
            elif key == "V":
                Val = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\V.png")
                Val = Val.resize((round(Val.size[0] * 0.090), round(Val.size[1] * 0.090)))
                pre_breath+=breadth_(Val,pre_breath)
                pre_breath+=spacing
            elif key == "W":
                Wal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\W.png")
                Wal = Wal.resize((round(Wal.size[0] * 0.090), round(Wal.size[1] * 0.090)))
                pre_breath+=breadth_(Wal,pre_breath)
                pre_breath+=spacing
            elif key == "X":
                Xal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\X.png")
                Xal = Xal.resize((round(Xal.size[0] * 0.090), round(Xal.size[1] * 0.090)))
                pre_breath+=breadth_(Xal,pre_breath)
                pre_breath+=spacing
            elif key == "Y":
                Yal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\Y.png")
                Yal = Yal.resize((round(Yal.size[0] * 0.090), round(Yal.size[1] * 0.090)))
                pre_breath+=breadth_(Yal,pre_breath)
                pre_breath+=spacing
            elif key == "Z":
                Zal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\Z.png")
                Zal = Zal.resize((round(Zal.size[0] * 0.090), round(Zal.size[1] * 0.090)))
                pre_breath+=breadth_(Zal,pre_breath)
                pre_breath+=spacing
            elif key == " ":
                pre_breath+=4
                pre_breath+=spacing
            elif key == "0":
                zero = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\0.png")
                zero = zero.resize((round(zero.size[0] * 0.090), round(zero.size[1] * 0.090)))
                pre_breath+=breadth_(zero,pre_breath)
                pre_breath+=spacing
            elif key == "1":
                one = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\1.png")
                one = one.resize((round(one.size[0] * 0.090), round(one.size[1] * 0.090)))
                pre_breath+=breadth_(one,pre_breath)
                pre_breath+=spacing
            elif key == "2":
                two = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\2.png")
                two = two.resize((round(two.size[0] * 0.090), round(two.size[1] * 0.090)))
                pre_breath+=breadth_(two,pre_breath)
                pre_breath+=spacing
            elif key == "3":
                three = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\3.png")
                three = three.resize((round(three.size[0] * 0.090), round(three.size[1] * 0.090)))
                pre_breath+=breadth_(three,pre_breath)
                pre_breath+=spacing
            elif key == "4":
                four = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\4.png")
                four = four.resize((round(four.size[0] * 0.090), round(four.size[1] * 0.090)))
                pre_breath+=breadth_(four,pre_breath)
                pre_breath+=spacing
            elif key == "5":
                five = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\5.png")
                five = five.resize((round(five.size[0] * 0.090), round(five.size[1] * 0.090)))
                pre_breath+=breadth_(five,pre_breath)
                pre_breath+=spacing
            elif key == "6":
                six = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\6.png")
                six = six.resize((round(six.size[0] * 0.090), round(six.size[1] * 0.090)))
                pre_breath+=breadth_(six,pre_breath)
                pre_breath+=spacing
            elif key == "7":
                seven = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\7.png")
                seven = seven.resize((round(seven.size[0] * 0.090), round(seven.size[1] * 0.090)))
                pre_breath+=breadth_(seven,pre_breath)
                pre_breath+=spacing
            elif key == "8":
                eight = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\8.png")
                eight = eight.resize((round(eight.size[0] * 0.090), round(eight.size[1] * 0.090)))
                pre_breath+=breadth_(eight,pre_breath)
                pre_breath+=spacing
            elif key == "9":
                nine = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\9.png")
                nine = nine.resize((round(nine.size[0] * 0.090), round(nine.size[1] * 0.090)))
                pre_breath+=breadth_(nine,pre_breath)
                pre_breath+=spacing
            elif key == "!":
                exclaim = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\!.png")
                exclaim = exclaim.resize((round(exclaim.size[0] * 0.090), round(exclaim.size[1] * 0.090)))
                pre_breath+=breadth_(exclaim,pre_breath)
                pre_breath+=spacing
            elif key == "#":
                hashtag = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\#.png")
                hashtag = hashtag.resize((round(hashtag.size[0] * 0.090), round(hashtag.size[1] * 0.090)))
                pre_breath+=breadth_(hashtag,pre_breath)
                pre_breath+=spacing
            elif key == "$":
                dollar = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\$.png")
                dollar = dollar.resize((round(dollar.size[0] * 0.090), round(dollar.size[1] * 0.090)))
                pre_breath+=breadth_(dollar,pre_breath)
                pre_breath+=spacing
            elif key == "(":
                bracket1_open = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\(.png")
                bracket1_open = bracket1_open.resize((round(bracket1_open.size[0] * 0.090), round(bracket1_open.size[1] * 0.090)))
                pre_breath+=breadth_(bracket1_open,pre_breath)
                pre_breath+=spacing

            elif key == ")":
                bracket1_close = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\).png")
                bracket1_close = bracket1_close.resize((round(bracket1_close.size[0] * 0.090), round(bracket1_close.size[1] * 0.090)))
                pre_breath+=breadth_(bracket1_close,pre_breath)
                pre_breath+=spacing
            elif key == ",":
                comma = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\,.png")
                comma = comma.resize((round(comma.size[0] * 0.090), round(comma.size[1] * 0.090)))
                pre_breath+=breadth_(comma,pre_breath)
                pre_breath+=spacing
            elif key == ".":
                dot = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\..png")
                dot = dot.resize((round(dot.size[0] * 0.090), round(dot.size[1] * 0.090)))
                pre_breath+=breadth_(dot,pre_breath)
                pre_breath+=spacing
            elif key == "'":
                apostophy = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\'.png")
                apostophy = apostophy.resize((round(apostophy.size[0] * 0.090), round(apostophy.size[1] * 0.090)))
                pre_breath+=breadth_(apostophy,pre_breath)
                pre_breath+=spacing
            elif key == "-":
                minus = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\-.png")
                minus = minus.resize((round(minus.size[0] * 0.090), round(minus.size[1] * 0.090)))
                pre_breath+=breadth_(minus,pre_breath)
                pre_breath+=spacing
            elif key == "@":
                AtTheRate = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\@.png")
                AtTheRate = AtTheRate.resize((round(AtTheRate.size[0] * 0.090), round(AtTheRate.size[1] * 0.090)))
                pre_breath+=breadth_(AtTheRate,pre_breath)
                pre_breath+=spacing
            elif key == "[":
                bracket2_open = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\[.png")
                bracket2_open = bracket2_open.resize((round(bracket2_open.size[0] * 0.090), round(bracket2_open.size[1] * 0.090)))
                pre_breath+=breadth_(bracket2_open,pre_breath)
                pre_breath+=spacing
            elif key == "]":
                bracket2_close = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\].png")
                bracket2_close = bracket2_close.resize((round(bracket2_close.size[0] * 0.090), round(bracket2_close.size[1] * 0.090)))
                pre_breath+=breadth_(bracket2_close,pre_breath)
                pre_breath+=spacing
            elif key == "^":
                up = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\^.png")
                up = up.resize((round(up.size[0] * 0.090), round(up.size[1] * 0.090)))
                pre_breath+=breadth_(up,pre_breath)
                pre_breath+=spacing
            elif key == "`":
                idk1 = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\`.png")
                idk1 = idk1.resize((round(idk1.size[0] * 0.090), round(idk1.size[1] * 0.090)))
                pre_breath+=breadth_(idk1,pre_breath)
                pre_breath+=spacing
            elif key == "{":
                bracket3_open = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\{.png")
                bracket3_open = bracket3_open.resize((round(bracket3_open.size[0] * 0.090), round(bracket3_open.size[1] * 0.090)))
                pre_breath+=breadth_(bracket3_open,pre_breath)
                pre_breath+=spacing
            elif key == "}":
                bracket3_close = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\}.png")
                bracket3_close = bracket3_close.resize((round(bracket3_close.size[0] * 0.090), round(bracket3_close.size[1] * 0.090)))
                pre_breath+=breadth_(bracket3_close,pre_breath)
                pre_breath+=spacing
            elif key == "~":
                idk2 = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\~.png")
                idk2 = idk2.resize((round(idk2.size[0] * 0.090), round(idk2.size[1] * 0.090)))
                pre_breath+=breadth_(idk2,pre_breath)
                pre_breath+=spacing
            elif key == "+":
                plus = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\+.png")
                plus = plus.resize((round(plus.size[0] * 0.090), round(plus.size[1] * 0.090)))
                pre_breath+=breadth_(plus,pre_breath)
                pre_breath+=spacing
            elif key == "=":
                EqualsTo = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\=.png")
                EqualsTo = EqualsTo.resize((round(EqualsTo.size[0] * 0.090), round(EqualsTo.size[1] * 0.090)))
                pre_breath+=breadth_(EqualsTo,pre_breath)
                pre_breath+=spacing
            elif key == ";":
                colon = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\colon.png")
                colon = colon.resize((round(colon.size[0] * 0.090), round(colon.size[1] * 0.090)))
                pre_breath+=breadth_(colon,pre_breath)
                pre_breath+=spacing
            elif key == '"':
                inverted_commas = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\inverted-commas.png")
                inverted_commas = inverted_commas.resize((round(inverted_commas.size[0] * 0.090), round(inverted_commas.size[1] * 0.090)))
                pre_breath+=breadth_(inverted_commas,pre_breath)
                pre_breath+=spacing
            elif key == "<":
                left_comparator = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\left_comparator.png")
                left_comparator = left_comparator.resize((round(left_comparator.size[0] * 0.090), round(left_comparator.size[1] * 0.090)))
                pre_breath+=breadth_(left_comparator,pre_breath)
                pre_breath+=spacing
            elif key == "?":
                question_mark = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\question mark.png")
                question_mark = question_mark.resize((round(question_mark.size[0] * 0.090), round(question_mark.size[1] * 0.090)))
                pre_breath+=breadth_(question_mark,pre_breath)
                pre_breath+=spacing
            elif key == ">":
                right_comparator = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\right_comparator.png")
                right_comparator = right_comparator.resize((round(right_comparator.size[0] * 0.090), round(right_comparator.size[1] * 0.090)))
                pre_breath+=breadth_(right_comparator,pre_breath)
                pre_breath+=spacing
            elif key == ":":
                semi_colon = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\semi-colon.png")
                semi_colon = semi_colon.resize((round(semi_colon.size[0] * 0.090), round(semi_colon.size[1] * 0.090)))
                pre_breath += breadth_(semi_colon, pre_breath)
                pre_breath += spacing
            elif key == "/":
                slash = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\slash.png")
                slash = slash.resize((round(slash.size[0] * 0.090), round(slash.size[1] * 0.090)))
                pre_breath+=breadth_(slash,pre_breath)
                pre_breath+=spacing
            elif key == "*":
                star = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\star.png")
                star = transparent(star)
                pre_breath+=breadth_(star,pre_breath)
                pre_breath+=spacing


            elif key == "a":
                aal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\lowercase\A.png")
                aal = aal.resize((round(aal.size[0] * 0.090), round(aal.size[1] * 0.090)))
                pre_breath+=breadth_(aal,pre_breath)
                pre_breath+=spacing
            elif key == "b":
                bal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\lowercase\B.png")
                bal = bal.resize((round(bal.size[0] * 0.090), round(bal.size[1] * 0.090)))
                pre_breath+=breadth_(bal,pre_breath)
                pre_breath+=spacing
            elif key == "c":
                cal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\lowercase\C.png")
                cal = cal.resize((round(cal.size[0] * 0.090), round(cal.size[1] * 0.090)))
                pre_breath+=breadth_(cal,pre_breath)
                pre_breath+=spacing
            elif key == "d":
                dal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\lowercase\D.png")
                dal = dal.resize((round(dal.size[0] * 0.090), round(dal.size[1] * 0.090)))
                pre_breath+=breadth_(dal,pre_breath)
                pre_breath+=spacing
            elif key == "e":
                eal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\lowercase\E.png")
                eal = eal.resize((round(eal.size[0] * 0.090), round(eal.size[1] * 0.090)))
                pre_breath+=breadth_(eal,pre_breath)
                pre_breath+=spacing
            elif key == "f":
                Fal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\lowercase\F.png")
                Fal = Fal.resize((round(Fal.size[0] * 0.090), round(Fal.size[1] * 0.090)))
                pre_breath+=breadth_(Fal,pre_breath)
                pre_breath+=spacing
            elif key == "g":
                Gal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\lowercase\G.png")
                Gal = Gal.resize((round(Gal.size[0] * 0.090), round(Gal.size[1] * 0.090)))
                pre_breath+=breadth_(Gal,pre_breath)
                pre_breath+=spacing
            elif key == "h":
                Hal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\lowercase\H.png")
                Hal = Hal.resize((round(Hal.size[0] * 0.090), round(Hal.size[1] * 0.090)))
                pre_breath+=breadth_(Hal,pre_breath)
                pre_breath+=spacing
            elif key == "i":
                Ial = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\lowercase\I.png")
                Ial = Ial.resize((round(Ial.size[0] * 0.090), round(Ial.size[1] * 0.090)))
                pre_breath+=breadth_(Ial,pre_breath)
                pre_breath+=spacing
            elif key == "j":
                Jal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\lowercase\J.png")
                Jal = Jal.resize((round(Jal.size[0] * 0.090), round(Jal.size[1] * 0.090)))
                pre_breath+=breadth_(Jal,pre_breath)
                pre_breath+=spacing
            elif key == "k":
                Kal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\lowercase\K.png")
                Kal = Kal.resize((round(Kal.size[0] * 0.090), round(Kal.size[1] * 0.090)))
                pre_breath+=breadth_(Kal,pre_breath)
                pre_breath+=spacing
            elif key == "l":
                Lal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\lowercase\L.png")
                Lal = Lal.resize((round(Lal.size[0] * 0.090), round(Lal.size[1] * 0.090)))
                pre_breath+=breadth_(Lal,pre_breath)
                pre_breath+=spacing
            elif key == "m":
                Mal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\lowercase\M.png")
                Mal = Mal.resize((round(Mal.size[0] * 0.090), round(Mal.size[1] * 0.090)))
                pre_breath+=breadth_(Mal,pre_breath)
                pre_breath+=spacing
            elif key == "n":
                Nal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\lowercase\N.png")
                Nal = Nal.resize((round(Nal.size[0] * 0.090), round(Nal.size[1] * 0.090)))
                pre_breath+=breadth_(Nal,pre_breath)
                pre_breath+=spacing
            elif key == "o":
                Oal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\lowercase\O.png")
                Oal = Oal.resize((round(Oal.size[0] * 0.090), round(Oal.size[1] * 0.090)))
                pre_breath+=breadth_(Oal,pre_breath)
                pre_breath+=spacing
            elif key == "p":
                Pal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\lowercase\P.png")
                Pal = Pal.resize((round(Pal.size[0] * 0.090), round(Pal.size[1] * 0.090)))
                pre_breath+=breadth_(Pal,pre_breath)
                pre_breath+=spacing
            elif key == "q":
                Qal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\lowercase\Q.png")
                Qal = Qal.resize((round(Qal.size[0] * 0.090), round(Qal.size[1] * 0.090)))
                pre_breath+=breadth_(Qal,pre_breath)
                pre_breath+=spacing
            elif key == "r":
                Ral = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\lowercase\R.png")
                Ral = Ral.resize((round(Ral.size[0] * 0.090), round(Ral.size[1] * 0.090)))
                pre_breath+=breadth_(Ral,pre_breath)
                pre_breath+=spacing
            elif key == "s":
                Sal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\lowercase\S.png")
                Sal = Sal.resize((round(Sal.size[0] * 0.090), round(Sal.size[1] * 0.090)))
                pre_breath+=breadth_(Sal,pre_breath)
                pre_breath+=spacing
            elif key == "t":
                Tal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\lowercase\T.png")
                Tal = Tal.resize((round(Tal.size[0] * 0.090), round(Tal.size[1] * 0.090)))
                pre_breath+=breadth_(Tal,pre_breath)
                pre_breath+=spacing
            elif key == "u":
                Ual = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\lowercase\U.png")
                Ual = Ual.resize((round(Ual.size[0] * 0.090), round(Ual.size[1] * 0.090)))
                pre_breath+=breadth_(Ual,pre_breath)
                pre_breath+=spacing
            elif key == "v":
                Val = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\lowercase\V.png")
                Val = Val.resize((round(Val.size[0] * 0.090), round(Val.size[1] * 0.090)))
                pre_breath+=breadth_(Val,pre_breath)
                pre_breath+=spacing
            elif key == "w":
                Wal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\lowercase\W.png")
                Wal = Wal.resize((round(Wal.size[0] * 0.090), round(Wal.size[1] * 0.090)))
                pre_breath+=breadth_(Wal,pre_breath)
                pre_breath+=spacing
            elif key == "x":
                Xal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\lowercase\X.png")
                Xal = Xal.resize((round(Xal.size[0] * 0.090), round(Xal.size[1] * 0.090)))
                pre_breath+=breadth_(Xal,pre_breath)
                pre_breath+=spacing
            elif key == "y":
                Yal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\lowercase\Y.png")
                Yal = Yal.resize((round(Yal.size[0] * 0.090), round(Yal.size[1] * 0.090)))
                pre_breath+=breadth_(Yal,pre_breath)
                pre_breath+=spacing
            elif key == "z":
                Zal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\lowercase\Z.png")
                Zal = Zal.resize((round(Zal.size[0] * 0.090), round(Zal.size[1] * 0.090)))
                pre_breath+=breadth_(Zal,pre_breath)
                pre_breath+=spacing

        #print (pre_breath)



        for c in enumerate(worded):
            #print("b:",breath)
            total=breath+pre_breath
            if total > 219:
                length_no += 1
                breath = 5
            while breath>215:
                breath=5
                length_no+=1
            pre_breath=0
            #print("l_no before:", length_no)
            length_no = length_no * 13
            #print("l_no after:", length_no)
            #print("l before:",length)
            length+=length_no
            #print("l after:",length)
            length_no = 0
            no=c[0]
            key = c[1]
            #reg=worder(inp)
            #print ("reg: ",reg[0])
            #word=reg[0:1]
            #word[0]=word[0]-1
            #word[1]=word[1]-1
            #reg.pop(0)












            if key == "A":
                Aal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\A.png")
                Aal = Aal.resize((round(Aal.size[0] * 0.090), round(Aal.size[1] * 0.090)))
                Aal = transparent(Aal)
                background.paste(Aal, (breath, length), Aal)
                breath+=breadth_(Aal,breath)
                breath+=spacing
            elif key == "B":
                Bal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\B.png")
                Bal = Bal.resize((round(Bal.size[0] * 0.090), round(Bal.size[1] * 0.090)))
                Bal = transparent(Bal)
                background.paste(Bal, (breath, length), Bal)
                breath+=breadth_(Bal,breath)
                breath+=spacing
            elif key == "C":
                Cal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\C.png")
                Cal = Cal.resize((round(Cal.size[0] * 0.090), round(Cal.size[1] * 0.090)))
                Cal = transparent(Cal)
                background.paste(Cal, (breath, length), Cal)
                breath+=breadth_(Cal,breath)
                breath+=spacing
            elif key == "D":
                Dal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\D.png")
                Dal = Dal.resize((round(Dal.size[0] * 0.090), round(Dal.size[1] * 0.090)))
                Dal = transparent(Dal)
                background.paste(Dal, (breath, length), Dal)
                breath+=breadth_(Dal,breath)
                breath+=spacing
            elif key == "E":
                Eal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\E.png")
                Eal = Eal.resize((round(Eal.size[0] * 0.090), round(Eal.size[1] * 0.090)))
                Eal = transparent(Eal)
                background.paste(Eal, (breath, length), Eal)
                breath+=breadth_(Eal,breath)
                breath+=spacing
            elif key == "F":
                Fal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\F.png")
                Fal = Fal.resize((round(Fal.size[0] * 0.090), round(Fal.size[1] * 0.090)))
                Fal = transparent(Fal)
                background.paste(Fal, (breath, length), Fal)
                breath+=breadth_(Fal,breath)
                breath+=spacing
            elif key == "G":
                Gal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\G.png")
                Gal = Gal.resize((round(Gal.size[0] * 0.090), round(Gal.size[1] * 0.090)))
                Gal = transparent(Gal)
                background.paste(Gal, (breath, length), Gal)
                breath+=breadth_(Gal,breath)
                breath+=spacing
            elif key == "H":
                Hal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\H.png")
                Hal = Hal.resize((round(Hal.size[0] * 0.090), round(Hal.size[1] * 0.090)))
                Hal = transparent(Hal)
                background.paste(Hal, (breath, length), Hal)
                breath+=breadth_(Hal,breath)
                breath+=spacing
            elif key == "I":
                Ial = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\I.png")
                Ial = Ial.resize((round(Ial.size[0] * 0.090), round(Ial.size[1] * 0.090)))
                Ial = transparent(Ial)
                background.paste(Ial, (breath, length), Ial)
                breath+=breadth_(Ial,breath)
                breath+=spacing
            elif key == "J":
                Jal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\J.png")
                Jal = Jal.resize((round(Jal.size[0] * 0.090), round(Jal.size[1] * 0.090)))
                Jal = transparent(Jal)
                background.paste(Jal, (breath, length), Jal)
                breath+=breadth_(Jal,breath)
                breath+=spacing
            elif key == "K":
                Kal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\K.png")
                Kal = Kal.resize((round(Kal.size[0] * 0.090), round(Kal.size[1] * 0.090)))
                Kal = transparent(Kal)
                background.paste(Kal, (breath, length), Kal)
                breath+=breadth_(Kal,breath)
                breath+=spacing
            elif key == "L":
                Lal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\L.png")
                Lal = Lal.resize((round(Lal.size[0] * 0.090), round(Lal.size[1] * 0.090)))
                Lal = transparent(Lal)
                background.paste(Lal, (breath, length), Lal)
                breath+=breadth_(Lal,breath)
                breath+=spacing
            elif key == "M":
                Mal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\M.png")
                Mal = Mal.resize((round(Mal.size[0] * 0.090), round(Mal.size[1] * 0.090)))
                Mal = transparent(Mal)
                background.paste(Mal, (breath, length), Mal)
                breath+=breadth_(Mal,breath)
                breath+=spacing
            elif key == "N":
                Nal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\\N.png")
                Nal = Nal.resize((round(Nal.size[0] * 0.090), round(Nal.size[1] * 0.090)))
                Nal = transparent(Nal)
                background.paste(Nal, (breath, length), Nal)
                breath+=breadth_(Nal,breath)
                breath+=spacing
            elif key == "O":
                Oal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\O.png")
                Oal = Oal.resize((round(Oal.size[0] * 0.090), round(Oal.size[1] * 0.090)))
                Oal = transparent(Oal)
                background.paste(Oal, (breath, length), Oal)
                breath+=breadth_(Oal,breath)
                breath+=spacing
            elif key == "P":
                Pal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\P.png")
                Pal = Pal.resize((round(Pal.size[0] * 0.090), round(Pal.size[1] * 0.090)))
                Pal = transparent(Pal)
                background.paste(Pal, (breath, length), Pal)
                breath+=breadth_(Pal,breath)
                breath+=spacing
            elif key == "Q":
                Qal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\Q.png")
                Qal = Qal.resize((round(Qal.size[0] * 0.090), round(Qal.size[1] * 0.090)))
                Qal = transparent(Qal)
                background.paste(Qal, (breath, length), Qal)
                breath+=breadth_(Qal,breath)
                breath+=spacing
            elif key == "R":
                Ral = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\R.png")
                Ral = Ral.resize((round(Ral.size[0] * 0.090), round(Ral.size[1] * 0.090)))
                Ral = transparent(Ral)
                background.paste(Ral, (breath, length), Ral)
                breath+=breadth_(Ral,breath)
                breath+=spacing
            elif key == "S":
                Sal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\S.png")
                Sal = Sal.resize((round(Sal.size[0] * 0.090), round(Sal.size[1] * 0.090)))
                Sal = transparent(Sal)
                background.paste(Sal, (breath, length), Sal)
                breath+=breadth_(Sal,breath)
                breath+=spacing
            elif key == "T":
                Tal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\T.png")
                Tal = Tal.resize((round(Tal.size[0] * 0.090), round(Tal.size[1] * 0.090)))
                Tal = transparent(Tal)
                background.paste(Tal, (breath, length), Tal)
                breath+=breadth_(Tal,breath)
                breath+=spacing
            elif key == "U":
                Ual = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\U.png")
                Ual = Ual.resize((round(Ual.size[0] * 0.090), round(Ual.size[1] * 0.090)))
                Ual = transparent(Ual)
                background.paste(Ual, (breath, length), Ual)
                breath+=breadth_(Ual,breath)
                breath+=spacing
            elif key == "V":
                Val = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\V.png")
                Val = Val.resize((round(Val.size[0] * 0.090), round(Val.size[1] * 0.090)))
                Val = transparent(Val)
                background.paste(Val, (breath, length), Val)
                breath+=breadth_(Val,breath)
                breath+=spacing
            elif key == "W":
                Wal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\W.png")
                Wal = Wal.resize((round(Wal.size[0] * 0.090), round(Wal.size[1] * 0.090)))
                Wal = transparent(Wal)
                background.paste(Wal, (breath, length), Wal)
                breath+=breadth_(Wal,breath)
                breath+=spacing
            elif key == "X":
                Xal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\X.png")
                Xal = Xal.resize((round(Xal.size[0] * 0.090), round(Xal.size[1] * 0.090)))
                Xal = transparent(Xal)
                background.paste(Xal, (breath, length), Xal)
                breath+=breadth_(Xal,breath)
                breath+=spacing
            elif key == "Y":
                Yal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\Y.png")
                Yal = Yal.resize((round(Yal.size[0] * 0.090), round(Yal.size[1] * 0.090)))
                Yal = transparent(Yal)
                background.paste(Yal, (breath, length), Yal)
                breath+=breadth_(Yal,breath)
                breath+=spacing
            elif key == "Z":
                Zal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\Z.png")
                Zal = Zal.resize((round(Zal.size[0] * 0.090), round(Zal.size[1] * 0.090)))
                Zal = transparent(Zal)
                background.paste(Zal, (breath, length), Zal)
                breath+=breadth_(Zal,breath)
                breath+=spacing
            elif key == " ":
                breath+=5
            elif key == "0":
                zero = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\0.png")
                zero = zero.resize((round(zero.size[0] * 0.090), round(zero.size[1] * 0.090)))
                zero = transparent(zero)
                background.paste(zero, (breath, length), zero)
                breath+=breadth_(zero,breath)
                breath+=spacing
            elif key == "1":
                one = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\1.png")
                one = one.resize((round(one.size[0] * 0.090), round(one.size[1] * 0.090)))
                one = transparent(one)
                background.paste(one, (breath, length), one)
                breath+=breadth_(one,breath)
                breath+=spacing
            elif key == "2":
                two = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\2.png")
                two = two.resize((round(two.size[0] * 0.090), round(two.size[1] * 0.090)))
                two = transparent(two)
                background.paste(two, (breath, length), two)
                breath+=breadth_(two,breath)
                breath+=spacing
            elif key == "3":
                three = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\3.png")
                three = three.resize((round(three.size[0] * 0.090), round(three.size[1] * 0.090)))
                three = transparent(three)
                background.paste(three, (breath, length), three)
                breath+=breadth_(three,breath)
                breath+=spacing
            elif key == "4":
                four = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\4.png")
                four = four.resize((round(four.size[0] * 0.090), round(four.size[1] * 0.090)))
                four = transparent(four)
                background.paste(four, (breath, length), four)
                breath+=breadth_(four,breath)
                breath+=spacing
            elif key == "5":
                five = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\5.png")
                five = five.resize((round(five.size[0] * 0.090), round(five.size[1] * 0.090)))
                five = transparent(five)
                background.paste(five, (breath, length), five)
                breath+=breadth_(five,breath)
                breath+=spacing
            elif key == "6":
                six = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\6.png")
                six = six.resize((round(six.size[0] * 0.090), round(six.size[1] * 0.090)))
                six = transparent(six)
                background.paste(six, (breath, length), six)
                breath+=breadth_(six,breath)
                breath+=spacing
            elif key == "7":
                seven = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\7.png")
                seven = seven.resize((round(seven.size[0] * 0.090), round(seven.size[1] * 0.090)))
                seven = transparent(seven)
                background.paste(seven, (breath, length), seven)
                breath+=breadth_(seven,breath)
                breath+=spacing
            elif key == "8":
                eight = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\8.png")
                eight = eight.resize((round(eight.size[0] * 0.090), round(eight.size[1] * 0.090)))
                eight = transparent(eight)
                background.paste(eight, (breath, length), eight)
                breath+=breadth_(eight,breath)
                breath+=spacing
            elif key == "9":
                nine = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\9.png")
                nine = nine.resize((round(nine.size[0] * 0.090), round(nine.size[1] * 0.090)))
                nine = transparent(nine)
                background.paste(nine, (breath, length), nine)
                breath+=breadth_(nine,breath)
                breath+=spacing
            elif key == "!":
                exclaim = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\!.png")
                exclaim = exclaim.resize((round(exclaim.size[0] * 0.090), round(exclaim.size[1] * 0.090)))
                exclaim = transparent(exclaim)
                background.paste(exclaim, (breath, length), exclaim)
                breath+=breadth_(exclaim,breath)
                breath+=spacing
            elif key == "#":
                hashtag = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\#.png")
                hashtag = hashtag.resize((round(hashtag.size[0] * 0.090), round(hashtag.size[1] * 0.090)))
                hashtag         = transparent(hashtag)
                background.paste(hashtag, (breath, length), hashtag)
                breath+=breadth_(hashtag,breath)
                breath+=spacing
            elif key == "$":
                dollar = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\$.png")
                dollar = dollar.resize((round(dollar.size[0] * 0.090), round(dollar.size[1] * 0.090)))
                dollar = transparent(dollar)
                background.paste(dollar, (breath, length), dollar)
                breath+=breadth_(dollar,breath)
                breath+=spacing
            elif key == "(":
                bracket1_open = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\(.png")
                bracket1_open = bracket1_open.resize((round(bracket1_open.size[0] * 0.090), round(bracket1_open.size[1] * 0.090)))
                bracket1_open = transparent(bracket1_open)
                background.paste(bracket1_open, (breath, length), bracket1_open)
                breath+=breadth_(bracket1_open,breath)
                breath+=spacing

            elif key == ")":
                bracket1_close = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\).png")
                bracket1_close = bracket1_close.resize((round(bracket1_close.size[0] * 0.090), round(bracket1_close.size[1] * 0.090)))
                bracket1_close = transparent(bracket1_close)
                background.paste(bracket1_close, (breath, length), bracket1_close)
                breath+=breadth_(bracket1_close,breath)
                breath+=spacing
            elif key == ",":
                comma = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\,.png")
                comma = comma.resize((round(comma.size[0] * 0.090), round(comma.size[1] * 0.090)))
                comma = transparent(comma)
                background.paste(comma, (breath, length), comma)
                breath+=breadth_(comma,breath)
                breath+=spacing
            elif key == ".":
                dot = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\..png")
                dot = dot.resize((round(dot.size[0] * 0.090), round(dot.size[1] * 0.090)))
                dot = transparent(dot)
                background.paste(dot, (breath, length), dot)
                breath+=breadth_(dot,breath)
                breath+=spacing
            elif key == "'":
                apostophy = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\'.png")
                apostophy = apostophy.resize((round(apostophy.size[0] * 0.090), round(apostophy.size[1] * 0.090)))
                apostophy = transparent(apostophy)
                background.paste(apostophy, (breath, length), apostophy)
                breath+=breadth_(apostophy,breath)
                breath+=spacing
            elif key == "-":
                minus = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\-.png")
                minus = minus.resize((round(minus.size[0] * 0.090), round(minus.size[1] * 0.090)))
                minus = transparent(minus)
                background.paste(minus, (breath, length), minus)
                breath+=breadth_(minus,breath)
                breath+=spacing
            elif key == "@":
                AtTheRate = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\@.png")
                AtTheRate = AtTheRate.resize((round(AtTheRate.size[0] * 0.090), round(AtTheRate.size[1] * 0.090)))
                AtTheRate = transparent(AtTheRate)
                background.paste(AtTheRate, (breath, length), AtTheRate)
                breath+=breadth_(AtTheRate,breath)
                breath+=spacing
            elif key == "[":
                bracket2_open = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\[.png")
                bracket2_open = bracket2_open.resize((round(bracket2_open.size[0] * 0.090), round(bracket2_open.size[1] * 0.090)))
                bracket2_open = transparent(bracket2_open)
                background.paste(bracket2_open, (breath, length), bracket2_open)
                breath+=breadth_(bracket2_open,breath)
                breath+=spacing
            elif key == "]":
                bracket2_close = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\].png")
                bracket2_close = bracket2_close.resize((round(bracket2_close.size[0] * 0.090), round(bracket2_close.size[1] * 0.090)))
                bracket2_close = transparent(bracket2_close)
                background.paste(bracket2_close, (breath, length), bracket2_close)
                breath+=breadth_(bracket2_close,breath)
                breath+=spacing
            elif key == "^":
                up = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\^.png")
                up = up.resize((round(up.size[0] * 0.090), round(up.size[1] * 0.090)))
                up = transparent(up)
                background.paste(up, (breath, length), up)
                breath+=breadth_(up,breath)
                breath+=spacing
            elif key == "`":
                idk1 = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\`.png")
                idk1 = idk1.resize((round(idk1.size[0] * 0.090), round(idk1.size[1] * 0.090)))
                idk1 = transparent(idk1)
                background.paste(idk1, (breath, length), idk1)
                breath+=breadth_(idk1,breath)
                breath+=spacing
            elif key == "{":
                bracket3_open = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\{.png")
                bracket3_open = bracket3_open.resize((round(bracket3_open.size[0] * 0.090), round(bracket3_open.size[1] * 0.090)))
                bracket3_open = transparent(bracket3_open)
                background.paste(bracket3_open, (breath, length), bracket3_open)
                breath+=breadth_(bracket3_open,breath)
                breath+=spacing
            elif key == "}":
                bracket3_close = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\}.png")
                bracket3_close = bracket3_close.resize((round(bracket3_close.size[0] * 0.090), round(bracket3_close.size[1] * 0.090)))
                bracket3_close = transparent(bracket3_close)
                background.paste(bracket3_close, (breath, length), bracket3_close)
                breath+=breadth_(bracket3_close,breath)
                breath+=spacing
            elif key == "~":
                idk2 = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\~.png")
                idk2 = idk2.resize((round(idk2.size[0] * 0.090), round(idk2.size[1] * 0.090)))
                idk2 = transparent(idk2)
                background.paste(idk2, (breath, length), idk2)
                breath+=breadth_(idk2,breath)
                breath+=spacing
            elif key == "+":
                plus = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\+.png")
                plus = plus.resize((round(plus.size[0] * 0.090), round(plus.size[1] * 0.090)))
                plus = transparent(plus)
                background.paste(plus, (breath, length), plus)
                breath+=breadth_(plus,breath)
                breath+=spacing
            elif key == "=":
                EqualsTo = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\=.png")
                EqualsTo = EqualsTo.resize((round(EqualsTo.size[0] * 0.090), round(EqualsTo.size[1] * 0.090)))
                EqualsTo = transparent(EqualsTo)
                background.paste(EqualsTo, (breath, length), EqualsTo)
                breath+=breadth_(EqualsTo,breath)
                breath+=spacing
            elif key == ";":
                colon = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\colon.png")
                colon = colon.resize((round(colon.size[0] * 0.090), round(colon.size[1] * 0.090)))
                colon = transparent(colon)
                background.paste(colon, (breath, length), colon)
                breath+=breadth_(colon,breath)
                breath+=spacing
            elif key == '"':
                inverted_commas = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\inverted-commas.png")
                inverted_commas = inverted_commas.resize((round(inverted_commas.size[0] * 0.090), round(inverted_commas.size[1] * 0.090)))
                inverted_commas = transparent(inverted_commas)
                background.paste(inverted_commas, (breath, length), inverted_commas)
                breath+=breadth_(inverted_commas,breath)
                breath+=spacing
            elif key == "<":
                left_comparator = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\left_comparator.png")
                left_comparator = left_comparator.resize((round(left_comparator.size[0] * 0.090), round(left_comparator.size[1] * 0.090)))
                left_comparator = transparent(left_comparator)
                background.paste(left_comparator, (breath, length), left_comparator)
                breath+=breadth_(left_comparator,breath)
                breath+=spacing
            elif key == "?":
                question_mark = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\question mark.png")
                question_mark = question_mark.resize((round(question_mark.size[0] * 0.090), round(question_mark.size[1] * 0.090)))
                question_mark = transparent(question_mark)
                background.paste(question_mark, (breath, length), question_mark)
                breath+=breadth_(question_mark,breath)
                breath+=spacing
            elif key == ">":
                right_comparator = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\right_comparator.png")
                right_comparator = right_comparator.resize((round(right_comparator.size[0] * 0.090), round(right_comparator.size[1] * 0.090)))
                right_comparator = transparent(right_comparator)
                background.paste(right_comparator, (breath, length), right_comparator)
                breath+=breadth_(right_comparator,breath)
                breath+=spacing
            elif key == ":":
                semi_colon = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\semi-colon.png")
                semi_colon = semi_colon.resize((round(semi_colon.size[0] * 0.090), round(semi_colon.size[1] * 0.090)))
                semi_colon = transparent(semi_colon)
                background.paste(semi_colon, (breath, length), semi_colon)
                breath += breadth_(semi_colon, breath)
                breath += spacing
            elif key == "/":
                slash = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\slash.png")
                slash = slash.resize((round(slash.size[0] * 0.090), round(slash.size[1] * 0.090)))
                slash = transparent(slash)
                background.paste(slash, (breath, length), slash)
                breath+=breadth_(slash,breath)
                breath+=spacing
            elif key == "*":
                star = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\star.png")
                star = star.resize((round(star.size[0] * 0.090), round(star.size[1] * 0.090)))
                star = transparent(star)
                background.paste(star, (breath, length), star)
                breath+=breadth_(star,breath)
                breath+=spacing


            elif key == "a":
                aal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\lowercase\A.png")
                aal = aal.resize((round(aal.size[0] * 0.090), round(aal.size[1] * 0.090)))
                aal = transparent(aal)
                background.paste(aal, (breath, length), aal)
                breath+=breadth_(aal,breath)
                breath+=spacing
            elif key == "b":
                bal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\lowercase\B.png")
                bal = bal.resize((round(bal.size[0] * 0.090), round(bal.size[1] * 0.090)))
                bal = transparent(bal)
                background.paste(bal, (breath, length), bal)
                breath+=breadth_(bal,breath)
                breath+=spacing
            elif key == "c":
                cal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\lowercase\C.png")
                cal = cal.resize((round(cal.size[0] * 0.090), round(cal.size[1] * 0.090)))
                cal = transparent(cal)
                background.paste(cal, (breath, length),cal)
                breath+=breadth_(cal,breath)
                breath+=spacing
            elif key == "d":
                dal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\lowercase\D.png")
                dal = dal.resize((round(dal.size[0] * 0.090), round(dal.size[1] * 0.090)))
                dal = transparent(dal)
                background.paste(dal, (breath, length), dal)
                breath+=breadth_(dal,breath)
                breath+=spacing
            elif key == "e":
                eal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\lowercase\E.png")
                eal = eal.resize((round(eal.size[0] * 0.090), round(eal.size[1] * 0.090)))
                eal = transparent(eal)
                background.paste(eal, (breath, length), eal)
                breath+=breadth_(eal,breath)
                breath+=spacing
            elif key == "f":
                Fal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\lowercase\F.png")
                Fal = Fal.resize((round(Fal.size[0] * 0.090), round(Fal.size[1] * 0.090)))
                Fal = transparent(Fal)
                background.paste(Fal, (breath, length), Fal)
                breath+=breadth_(Fal,breath)
                breath+=spacing
            elif key == "g":
                Gal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\lowercase\G.png")
                Gal = Gal.resize((round(Gal.size[0] * 0.090), round(Gal.size[1] * 0.090)))
                Gal = transparent(Gal)
                background.paste(Gal, (breath, length), Gal)
                breath+=breadth_(Gal,breath)
                breath+=spacing
            elif key == "h":
                Hal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\lowercase\H.png")
                Hal = Hal.resize((round(Hal.size[0] * 0.090), round(Hal.size[1] * 0.090)))
                Hal = transparent(Hal)
                background.paste(Hal, (breath, length), Hal)
                breath+=breadth_(Hal,breath)
                breath+=spacing
            elif key == "i":
                Ial = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\lowercase\I.png")
                Ial = Ial.resize((round(Ial.size[0] * 0.090), round(Ial.size[1] * 0.090)))
                Ial = transparent(Ial)
                background.paste(Ial, (breath, length), Ial)
                breath+=breadth_(Ial,breath)
                breath+=spacing
            elif key == "j":
                Jal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\lowercase\J.png")
                Jal = Jal.resize((round(Jal.size[0] * 0.090), round(Jal.size[1] * 0.090)))
                Jal = transparent(Jal)
                background.paste(Jal, (breath, length), Jal)
                breath+=breadth_(Jal,breath)
                breath+=spacing
            elif key == "k":
                Kal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\lowercase\K.png")
                Kal = Kal.resize((round(Kal.size[0] * 0.090), round(Kal.size[1] * 0.090)))
                Kal = transparent(Kal)
                background.paste(Kal, (breath, length), Kal)
                breath+=breadth_(Kal,breath)
                breath+=spacing
            elif key == "l":
                Lal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\lowercase\L.png")
                Lal = Lal.resize((round(Lal.size[0] * 0.090), round(Lal.size[1] * 0.090)))
                Lal = transparent(Lal)
                background.paste(Lal, (breath, length), Lal)
                breath+=breadth_(Lal,breath)
                breath+=spacing
            elif key == "m":
                Mal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\lowercase\M.png")
                Mal = Mal.resize((round(Mal.size[0] * 0.090), round(Mal.size[1] * 0.090)))
                Mal = transparent(Mal)
                background.paste(Mal, (breath, length), Mal)
                breath+=breadth_(Mal,breath)
                breath+=spacing
            elif key == "n":
                Nal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\lowercase\N.png")
                Nal = Nal.resize((round(Nal.size[0] * 0.090), round(Nal.size[1] * 0.090)))
                Nal = transparent(Nal)
                background.paste(Nal, (breath, length), Nal)
                breath+=breadth_(Nal,breath)
                breath+=spacing
            elif key == "o":
                Oal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\lowercase\O.png")
                Oal = Oal.resize((round(Oal.size[0] * 0.090), round(Oal.size[1] * 0.090)))
                Oal = transparent(Oal)
                background.paste(Oal, (breath, length), Oal)
                breath+=breadth_(Oal,breath)
                breath+=spacing
            elif key == "p":
                Pal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\lowercase\P.png")
                Pal = Pal.resize((round(Pal.size[0] * 0.090), round(Pal.size[1] * 0.090)))
                Pal = transparent(Pal)
                background.paste(Pal, (breath, length), Pal)
                breath+=breadth_(Pal,breath)
                breath+=spacing
            elif key == "q":
                Qal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\lowercase\Q.png")
                Qal = Qal.resize((round(Qal.size[0] * 0.090), round(Qal.size[1] * 0.090)))
                Qal = transparent(Qal)
                background.paste(Qal, (breath, length), Qal)
                breath+=breadth_(Qal,breath)
                breath+=spacing
            elif key == "r":
                Ral = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\lowercase\R.png")
                Ral = Ral.resize((round(Ral.size[0] * 0.090), round(Ral.size[1] * 0.090)))
                Ral = transparent(Ral)
                background.paste(Ral, (breath, length), Ral)
                breath+=breadth_(Ral,breath)
                breath+=spacing
            elif key == "s":
                Sal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\lowercase\S.png")
                Sal = Sal.resize((round(Sal.size[0] * 0.090), round(Sal.size[1] * 0.090)))
                Sal = transparent(Sal)
                background.paste(Sal, (breath, length), Sal)
                breath+=breadth_(Sal,breath)
                breath+=spacing
            elif key == "t":
                Tal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\lowercase\T.png")
                Tal = Tal.resize((round(Tal.size[0] * 0.090), round(Tal.size[1] * 0.090)))
                Tal = transparent(Tal)
                background.paste(Tal, (breath, length), Tal)
                breath+=breadth_(Tal,breath)
                breath+=spacing
            elif key == "u":
                Ual = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\lowercase\U.png")
                Ual = Ual.resize((round(Ual.size[0] * 0.090), round(Ual.size[1] * 0.090)))
                Ual = transparent(Ual)
                background.paste(Ual, (breath, length), Ual)
                breath+=breadth_(Ual,breath)
                breath+=spacing
            elif key == "v":
                Val = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\lowercase\V.png")
                Val = Val.resize((round(Val.size[0] * 0.090), round(Val.size[1] * 0.090)))
                Val = transparent(Val)
                background.paste(Val, (breath, length), Val)
                breath+=breadth_(Val,breath)
                breath+=spacing
            elif key == "w":
                Wal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\lowercase\W.png")
                Wal = Wal.resize((round(Wal.size[0] * 0.090), round(Wal.size[1] * 0.090)))
                Wal = transparent(Wal)
                background.paste(Wal, (breath, length), Wal)
                breath+=breadth_(Wal,breath)
                breath+=spacing
            elif key == "x":
                Xal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\lowercase\X.png")
                Xal = Xal.resize((round(Xal.size[0] * 0.090), round(Xal.size[1] * 0.090)))
                Xal = transparent(Xal)
                background.paste(Xal, (breath, length), Xal)
                breath+=breadth_(Xal,breath)
                breath+=spacing
            elif key == "y":
                Yal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\lowercase\Y.png")
                Yal = Yal.resize((round(Yal.size[0] * 0.090), round(Yal.size[1] * 0.090)))
                Yal = transparent(Yal)
                background.paste(Yal, (breath, length), Yal)
                breath+=breadth_(Yal,breath)
                breath+=spacing
            elif key == "z":
                Zal = Image.open(r"C:\Users\home\PycharmProjects\Alphabets\lowercase\Z.png")
                Zal = Zal.resize((round(Zal.size[0] * 0.090), round(Zal.size[1] * 0.090)))
                Zal = transparent(Zal)
                background.paste(Zal, (breath, length), Zal)
                breath+=breadth_(Zal,breath)
                breath+=spacing




            #number=len(inp)
            #number-=1
            #if number==c[0]:
            #    length_no+=1
                #print (breath)
    length_no+=1
    breath=5
    background.save(r'C:\Users\home\PycharmProjects\Alphabets\Test.png',"PNG")