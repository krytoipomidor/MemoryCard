from random import shuffle
from menu import show_menu
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout,
                             QPushButton, QLabel, QRadioButton, QMessageBox)
from data import *
app = QApplication([])
window = QWidget()
window.resize(600, 500)
window.setWindowTitle('Memory Card')
window.move(100, 100)

main_layout = QVBoxLayout()
v_line = QVBoxLayout()
h_line1 = QHBoxLayout()
h_line2 = QHBoxLayout()

btn_menu = QPushButton('Меню')


question = QLabel()
r_answer_1 = QRadioButton()
r_answer_2 = QRadioButton()
r_answer_3 = QRadioButton()
r_answer_4 = QRadioButton()
def show_question(number):
    data[number]['wrong_answers'].append(data[number]['right_answer'])
    all_answers = data[number]['wrong_answers']
    shuffle(all_answers)
    question.setText(data[number]['question'])
    r_answer_1.setText(all_answers[0])
    r_answer_2.setText(all_answers[3])
    r_answer_3.setText(all_answers[1])
    r_answer_4.setText(all_answers[2])


def show_result(answer):
    global window_result
    window_result = QWidget()
    window_result.resize(200, 200)
    window_result.move(window.x(), window.y())
    v_line = QHBoxLayout()
    l = QLabel()
    a = QLabel(answer)
    r = QLabel()
    v_line.addWidget(l)
    v_line.addWidget(a)
    v_line.addWidget(r)
    window_result.setLayout(v_line)
    window_result.show()

def check_result():
    global number_data
    try:
        if r_answer_1.isChecked() and r_answer_1.text() == data[number_data]['right_answer']:
            show_result('Правильно')
            number_data += 1
            show_question(number_data)
        elif r_answer_2.isChecked() and r_answer_2.text() == data[number_data]['right_answer']:
            show_result('Правильно')
            number_data += 1
            show_question(number_data)
        elif r_answer_3.isChecked() and r_answer_3.text() == data[number_data]['right_answer']:
            show_result('Правильно')
            number_data += 1
            show_question(number_data)
        elif r_answer_4.isChecked() and r_answer_4.text() == data[number_data]['right_answer']:
            show_result('Правильно')
            number_data += 1
            show_question(number_data)
        else:
            show_result('Неправильно')
    except Exception as e:
        print(e)


show_question(number_data)
btn_ok = QPushButton('Відповісти')
btn_ok.clicked.connect(check_result)
btn_menu.clicked.connect(show_menu)
main_layout.addWidget(btn_menu)
main_layout.addWidget(question)

h_line1.addWidget(r_answer_1)
h_line1.addWidget(r_answer_2)
h_line2.addWidget(r_answer_3)
h_line2.addWidget(r_answer_4)

main_layout.addLayout(h_line1)
main_layout.addLayout(h_line2)
main_layout.addWidget(btn_ok)

window.setLayout(main_layout)

window.show()
app.exec_()