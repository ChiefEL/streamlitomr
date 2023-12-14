import cv2
import numpy as np
import streamlit as st 

def rectContour(contours):
    rectCon = []
    max_area = 0
    for i in contours:
        area = cv2.contourArea(i)
        if area > 30:
            peri = cv2.arcLength(i, True)
            approx = cv2.approxPolyDP(i, 0.02 * peri, True)
            if len(approx) == 4: #4 ise dortgendir
                rectCon.append(i)
    rectCon = sorted(rectCon, key=cv2.contourArea,reverse=True)
    #print(len(rectCon))
    return rectCon

def getCornerPoints(cont):
    peri = cv2.arcLength(cont, True)
    approx = cv2.approxPolyDP(cont, 0.02 * peri, True) #kose degerleri
    return approx


def reorder(myPoints):

    myPoints = myPoints.reshape((4, 2)) #fazla  koseliyi kaldiralim
    #print(myPoints)
    myPointsNew = np.zeros((4, 1, 2), np.int32) 
    add = myPoints.sum(1)
    #print(add)
    #print(np.argmax(add))
    myPointsNew[0] = myPoints[np.argmin(add)]  #[0,0]
    myPointsNew[3] =myPoints[np.argmax(add)]   #[w,h]
    diff = np.diff(myPoints, axis=1)
    myPointsNew[1] =myPoints[np.argmin(diff)]  #[w,0]
    myPointsNew[2] = myPoints[np.argmax(diff)] #[h,0]

    return myPointsNew

#20 questions vertical to divide the numbers / 5 marking areas + 1 place where the number of questions is written
#6 horizatanl bolmek
def splitBoxes(img):
    rows = np.vsplit(img,20) #vertical
    boxes=[]
    for r in rows:
        cols= np.hsplit(r,6) #horizantal
        for box in cols:
            boxes.append(box)
    return boxes

#We used the same function for the student number field
#Delete the above and only this one can be used with the correct values
#The student number field contains 10 markings with numbers 0-9.
#We divide it into 10x10
def split_num(img,vertical, horizantal):
    rows = np.vsplit(img,vertical) #vertical
    boxes=[]
    for r in rows:
        cols= np.hsplit(r,horizantal) #horizantal
        for box in cols:
            boxes.append(box)
    return boxes

#Since there are 3 combined course areas side by side, we divided them into 3 separate areas.
#brings it to a halt
def splitColumn(img):
    column = np.hsplit(img,3)
    
    return column


#score calculation area
#number of questions getting correct answers and student answers
#compares them and codes them as 1/0 in a new list
#1s are added up and the score is calculated.
def grading(answers, num_questions, myAnswers):
    grading = []
    wrong_ans = []

    answer_choices = ["A", "B", "C", "D", "E"]

    for i in range(num_questions):
        if answers[i] == myAnswers[i]:
            grading.append(1)
        else:
            grading.append(0)
            wrong_ans.append(i + 1)
            wrong_ans.append(answer_choices[myAnswers[i] - 1])

    score = (sum(grading) / num_questions) * 100
    return score, wrong_ans

#user responses in pixel values
# saves the reader to the list as index
def user_answers(num_questions,myPixelVal):
    myIndex=[]
    for x in range (0,num_questions):
        arr = myPixelVal[x]
        myIndexVal = np.where(arr == np.amax(arr))
        myIndex.append(myIndexVal[0][0])
    return myIndex
    
#student id by comparing from top to bottom We had to rearrange the rows and columns because the
#checked field would be detected.
#[[1,2,3],[4,5,6],[7,8,9]] ----> [[1,4,7],[2,5,8],[3 ,6,9]]
def id_reorder(myPixelVal):
    duz_liste = []
    for sutun in range(len(myPixelVal[0])):
        for satir in range(len(myPixelVal)):
            duz_liste.append(myPixelVal[satir][sutun])
    yeni_liste = []
    satir = []
    for eleman in duz_liste:
        satir.append(eleman)
        if len(satir) == len(myPixelVal):
            yeni_liste.append(satir)
            satir = []
    return yeni_liste
                
#Which one is marked according to the pixel value of the student number part?
#determination that there is
def id_answers(vertical_num,myPixelVal):
    myIndex=[]
    for x in range (0,vertical_num):
        arr = myPixelVal[x]
        myIndexVal = np.where(arr == np.amax(arr))
        myIndex.append(myIndexVal[0][0])
    return myIndex

def pixelVal(num_questions,choices,box):
    countR=0 #rows
    countC=0 #column
    myPixelVal = np.zeros((num_questions,choices))
    for image in box:
        totalPixels = cv2.countNonZero(image)
        myPixelVal[countR][countC]= totalPixels
        countC += 1
        if (countC==choices):countC=0;countR +=1
    return myPixelVal

#Reading the answer key from the file
def read_answers(dosya_adi):
    with open(dosya_adi, 'r') as f:
        satirlar = f.readlines()

    okunan_veriler = []
    for satir in satirlar:
        sutunlar = satir.split()
        okunan_veriler.append(sutunlar[1])
        
    return okunan_veriler


#numericizing the answers read from the file
def answers2numbers(answers):
    num_answers = []
    for i in answers:
        if i == "a":
            num_answers.append(1)
        elif i == "b":
            num_answers.append(2)
        elif i == "c":
            num_answers.append(3)
        elif i == "d":
            num_answers.append(4)
        elif i == "e":
            num_answers.append(5)
        else:
            print("Oppss Check Txt file")
    return num_answers

   
def image_show(images):
    col1, col2, col3 = st.columns(3)
    with col1:
            st.header("0")
            st.image(images[0],width=200)
    with col2:
            st.header("1")
            st.image(images[1],width=200)
    with col3:
            st.header("2")
            st.image(images[2],width=200)
            
    col4, col5= st.columns(2)
    
    with col4:
            st.header("3")
            st.image(images[4],width=200)
    with col5:
            st.header("4")
            st.image(images[5],width=200)
    col6, col7= st.columns(2)
    with col6:
            st.header("5")
            st.image(images[6],width=200)
    
    with col7:
            st.header("6")
            st.image(images[7],width=200)
    