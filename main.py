
from PyQt5.QtWidgets import *
from PyQt5 import uic
import random


class bankApp(QMainWindow):

    def __init__(self):
        super(bankApp, self).__init__()
        uic.loadUi("bankapp.ui", self)
        self.show()

        self.newUserbtn.clicked.connect(lambda: self.bankWin.setCurrentIndex(1))
        self.newUserbtn.clicked.connect(self.newField)
        self.nxtBtn.clicked.connect(lambda: self.bankWin.setCurrentIndex(2))
        self.nxtBtn.clicked.connect(self.rndmacctnum)
        self.nxtBtn.clicked.connect(self.rcdInfo)
        self.vpLine.textChanged.connect(self.fieldchk)
        self.acctCnfmBtn.clicked.connect(lambda: self.bankWin.setCurrentIndex(0))
        self.returningUserbtn.clicked.connect(lambda: self.bankWin.setCurrentIndex(3))
        self.loginBtn.clicked.connect(self.login)
  

        
    def newField(self):
        [getattr(self, widget + "Line").setText("") for widget in ["fn", "ln", "p", "vp"]]
        self.nxtBtn.setEnabled(False)


    def fieldchk(self):
        if all(widget.text().strip() for widget in [self.fnLine,self.lnLine,self.pLine,self.vpLine]) and self.pLine.text()==self.vpLine.text():
            self.nxtBtn.setEnabled(True)

    def rndmacctnum(self):
        rndnum = str(random.randint(10000000, 99999999))
        self.acctNum.setText(rndnum)

    def rcdInfo(self):
        uName = self.fnLine.text()+" "+self.lnLine.text()
        uID= self.idNameLine.text()
        if self.pLine.text() == self.vpLine.text():
            uPass = self.vpLine.text()
        uAcctNum = self.acctNum.text()

        uName = {
            "ID":uID,
            "name":uName,
            "password":uPass,
            "accountnum":uAcctNum,
            "Money": 0
        }

        with open('Users.txt','a') as f:
            f.write(str(uName)+'\n')

    def login(self):
        
        with open('Users.txt','r') as f:
            contents = f.read()
            lines = contents.split("\n")

            for line in lines:
                try:
                    data = eval(line)
            
                except:
                    continue

                if data["ID"] == self.userID.text():
                    if data["password"] == self.acctPass.text():
                        if isinstance(data, dict) and "accountnum" in data:
                            accountnum = data["accountnum"]
                            if accountnum[-4:] == self.fourdAcctNum.text():
                                self.bankWin.setCurrentIndex(4)
                            else:
                                message = QMessageBox()
                                message.setText("invalid account information")
                                message.exec_()

         
                

def main():
    app = QApplication([])
    window = bankApp()
    app.exec_()



if __name__ == '__main__':
    main()