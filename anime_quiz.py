from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QButtonGroup, QPushButton, QLabel, QVBoxLayout, QGroupBox, QHBoxLayout, QRadioButton
#modul
from random import randint, shuffle

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        #all the lines must be given when creating the objek, and will be recorded as properties 
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = []
questions_list.append(Question('The best anime', 'One Piece', 'Jujutsu Kaisen', 'Attack on Titan', 'Demon Slayer'))
questions_list.append(Question('Who is the strongest swordsmen in one piece?', 'Mihawk', 'Zoro', 'Ryuma', 'Rayleigh'))
questions_list.append(Question('The worst anime', 'None of the above', 'Swords Art Online', 'Sailor moon', 'Arifureta'))

app = QApplication([])
#variebelaplikasi
main_win = QWidget()
#jendela
main_win.setWindowTitle('Memory App')
#setting judul
main_win.resize(400, 200)
#ukuran jendela

btn_OK = QPushButton('Answer')
#answer button
lb_Question = QLabel('What is the best anime?')
#pertanyaanmu

RadioGroupBox = QGroupBox('Answer choices')
rbtn_1 = QRadioButton('Jujutsy Kaisen')
rbtn_2 = QRadioButton('One Piece')
rbtn_3 = QRadioButton('Blue Lock')
rbtn_4 = QRadioButton('Haikyuu')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox('Test result')
lb_Result = QLabel('Are you correct or not?')
lb_Correct = QLabel('The answer is...')
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
#question
layout_line2 = QHBoxLayout()
#answer option or test result
layout_line3 = QHBoxLayout()
#'answer' buttton

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter| Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch = 2)
#the button = large
layout_line3.addStretch(1)

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch = 2)
layout_card.addLayout(layout_line2, stretch = 8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch = 1)
layout_card.addStretch(1)
layout_card.setSpacing(5)
#spaces between content

main_win.setLayout(layout_card)
#setting layout ke jendela

def show_result():
    '''Show anwer panel'''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Next question')

def show_question():
    '''show question panel'''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Answer')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False) 
    rbtn_2.setChecked(False) 
    rbtn_3.setChecked(False) 
    rbtn_4.setChecked(False) 
    RadioGroup.setExclusive(True)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q : Question):
    '''the fuction writes the value of the question and answers into the corresponding widgets while distributing the answer options randomly'''
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    '''show result - put the written text into "result" and show the corresponding panel'''
    lb_Result.setText(res)
    show_result()

def check_answer():
    '''if an answer option was selected, check and show answer panel'''
    main_win.total += 1
    if answers[0].isChecked():
        show_correct('Correct!')
        main_win.score += 1
        print('Statistics\n-Total questions:', main_win.total, '\n-Right answers:', main_win.score)
        print('Rating:', (main_win.score/main_win.total*100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Incorrect!')
            print('Statistics\n-Total questions:', main_win.total, '\n-Right answers:', main_win.score)
            print('Rating:', (main_win.score/main_win.total*100), '%')

def next_question():
    '''Ask the next question in the list'''
    #this function needs a variebel that gives the number of the current question
    #this variebel can be made global, or it can be the property of a "global obejct" (app or window)
    # we will creat the property main_win.cur_question (below)
    main_win.cur_question = main_win.cur_question + 1 #move on to the next question
    if main_win.cur_question >= len(questions_list):
        main_win.cur_question = 0 #if the question list has ended, start over
    q= questions_list[main_win.cur_question] #take a question
    ask(q) # ask it

def click_OK():
    '''This determines whether to show another question or check the answer to this question'''
    if btn_OK.text() == 'Answer':
        check_answer()
    else:
        next_question()

# ask('What is my favorite game?', 'Genshin Impact', 'Roblox', 'Mobile Legends', 'Block Blast')

main_win.cur_question = -1

main_win.score = 0
main_win.total = 0

btn_OK.clicked.connect(click_OK)

main_win.show()
#tampilkan jendelanya
app.exec()
#jalankan aplikasinya