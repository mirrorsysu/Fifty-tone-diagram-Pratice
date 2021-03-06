from PyQt5.QtWidgets import *
import sys
import random

class ui(QMainWindow):
	def __init__(self):
		super(ui, self).__init__()

		width = 200
		height = 110
		labelSize = 30
		self.cnt = 0    #错误计数
		self.num = -1
		self.words1 = [
			'あ','い','う','え','お',
			'か','き','く','け','こ',
			'さ','し','す','せ','そ',
			'た','ち','つ','て','と',
			'な','に','ぬ','ね','の',
			'は','ひ','ふ','へ','ほ',
			'ま','み','む','め','も',
			'や','ゆ','よ',
			'ら','り','る','れ','ろ',
			'わ','を',
		]
		self.words2 = [
			'ア', 'イ', 'ウ', 'エ', 'オ',
			'カ', 'キ', 'ク', 'ケ', 'コ',
			'サ', 'シ', 'ス', 'セ', 'ソ',
			'タ', 'チ', 'ツ', 'テ', 'ト',
			'ナ', 'ニ', 'ヌ', 'ネ', 'ノ',
			'ハ', 'ヒ', 'フ', 'ヘ', 'ホ',
			'マ', 'ミ', 'ム', 'メ', 'モ',
			'ヤ', 'ユ', 'ヨ',
			'ラ', 'リ', 'ル', 'レ', 'ロ',
			'ワ', 'ヲ'
		]
		self.tones = [
			'a', 'i', 'u', 'e', 'o',
			'ka', 'ki', 'ku', 'ke', 'ko',
			'sa', 'shi', 'su', 'se', 'so',
			'ta', 'chi', 'tsu', 'te', 'to',
			'na', 'ni', 'nu', 'ne', 'no',
			'ha', 'hi', 'fu', 'he', 'ho',
			'ma', 'mi', 'mu', 'me', 'mo',
			'ya', 'yu', 'yo',
			'ra', 'ri', 'ru', 're', 'ro',
			'wa', 'wo',
		]
		self.setGeometry(200, 200, width, height)

		self.labelD = QLabel(self)  #说明label
		self.labelE = QLabel(self)  #显示label
		self.labelR = QLabel(self)  #正确label
		self.inputT = QLineEdit(self)   #输入框
		self.radio1 = QRadioButton(self)
		self.radio2 = QRadioButton(self)

		self.labelD.setText("假名:")
		self.labelE.setText("回车")
		self.radio1.setText('平假名')
		self.radio2.setText('片假名')
		self.radio1.setChecked(1)
		self.labelD.resize(labelSize, labelSize)
		self.labelE.resize(labelSize, labelSize)
		self.labelR.resize(labelSize, labelSize)
		self.inputT.resize(labelSize * 2, labelSize)

		self.labelD.move(10, 10)
		self.labelE.move(10 + labelSize * 1.5, 10)
		self.radio1.move(10 + labelSize * 4, 10)
		self.radio2.move(10 + labelSize * 4, 30)
		self.inputT.move(10, 10 + labelSize * 2)
		self.labelR.move(20 + labelSize * 2, 10 + labelSize * 2)
	def setWord(self):
		self.num = random.randint(0, len(self.tones) - 1)
		if self.radio1.isChecked():
			self.labelE.setText("<font size=%s>%s</font>" % (15, self.words1[self.num]))
		else:
			self.labelE.setText("<font size=%s>%s</font>" % (15, self.words2[self.num]))
	def onBtnOK(self,):
		if self.inputT.text() == self.tones[self.num]:
			self.cnt = 0
			self.labelR.setText('right')
			self.inputT.setText("")
			self.setWord()
		else:
			self.cnt += 1
			self.labelR.setText('wrong')
			if self.cnt >= 3:
				self.labelR.setText(self.tones[self.num])

	def keyPressEvent(self, event):
		if event.key() == 16777221 or 16777220:
			if self.num == -1:
				self.setWord()
			else :self.onBtnOK()

if __name__ == "__main__":
	app = QApplication(sys.argv);
	ui = ui()
	ui.show()
	sys.exit(app.exec_())




