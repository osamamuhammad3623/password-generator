import random, time, sys
from os import path
from PyQt5.QtWidgets import QApplication , QMainWindow
from PyQt5.uic import loadUiType

FORM_CLASS,_ = loadUiType(path.join(path.dirname("__file__"),"main.ui"))

class my_form(QMainWindow,FORM_CLASS):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.generate_btn.clicked.connect(self.generate)
        self.store_btn.clicked.connect(self.store_in_txt)
        self.clear_btn.clicked.connect(self.clear_all)
        self.show()
        
    def clear_all(self):
        self.check_letters.setChecked(False)
        self.check_num.setChecked(False)
        self.check_syms.setChecked(False)
        self.generated_pass.setText("")
        self.pass_length.setText("")
        self.errors_label.clear()

    def check(self):
        if ((self.check_letters.isChecked() == False) and 
            (self.check_num.isChecked() == False) and 
            (self.check_syms.isChecked() == False)):
            
            self.errors_label.setText('Check at least one!')
            return False
        
        if (len(self.pass_length.toPlainText()) == 0
            or int(self.pass_length.toPlainText()) < 8 ):
            self.errors_label.setText('Enter a valid number!')
            return False

        self.errors_label.clear()
        return True
    
    def generate(self):
        if self.check() == True:
            cap_letters = 'ABCDEFGHIKJLMNOPQRSTVWXYZ'
            small_letters = cap_letters.lower()
            numbers = '0123456789'
            syms = '!.@#$%^&*()_+<>?|\/'
            
            chosen_types = ''
            if self.check_letters.isChecked() == True:
                chosen_types += cap_letters
                chosen_types += small_letters
            if self.check_num.isChecked() == True:
                chosen_types += numbers
            if self.check_syms.isChecked() == True:
                chosen_types += syms
            
            pass_length = int(self.pass_length.toPlainText())
            # to avoid making the password starts with a number or a symbol
            #   we make the first char is a letter, and the rest is totally random!
            #   so, this means every password must start with a letter EVEN IF it's not chosen
            first_char = random.choice(cap_letters + small_letters)
            rest_char = "".join(random.sample(chosen_types,pass_length -1))
            password = first_char + rest_char
            self.generated_pass.setText(password)

    def store_in_txt(self):
        if len(self.generated_pass.toPlainText()) < 8:
            self.errors_label.setText('Generate a valid password first!')
        password = self.generated_pass.toPlainText()
        txt_file = open('saved_pass.txt', 'a')
        txt_file.write(password + '\n')

if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = my_form()
    window.show()
    sys.exit(application.exec_())