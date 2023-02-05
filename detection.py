import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTextEdit, QVBoxLayout, QPushButton ,QTextEdit
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')

class TokenizerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.text1_input = QTextEdit(self)
        self.text2_input = QTextEdit(self)
        self.tokenize_button = QPushButton("Benzerliği Hesapla", self)
        self.tokenize_button.clicked.connect(self.function)
        self.output_label = QLabel("", self)
        self.text1_input.setFixedHeight(250)
        self.text2_input.setFixedHeight(250)
        self.output_label.setFixedHeight(30)
        self.output_label.setFixedWidth(200)
        
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Kod 1:"))
        layout.addWidget(self.text1_input)
        layout.addWidget(QLabel("Kod 2:"))
        layout.addWidget(self.text2_input)
        layout.addWidget(self.tokenize_button)
        layout.addWidget(QLabel("Benzerlik Durumu:"))
        layout.addWidget(self.output_label)
        
        
        self.setLayout(layout)
        self.setWindowTitle("Benzerlik Ölçer")
   
    def tokenize(self, text1):
        return word_tokenize(text1)
        
        

    # jaccard benzerliği yöntemi ile tokenleştirilmiş kodların benzerlinin hesaplanması  
    def jaccard_similarity(self,codeTokens1, codeTokens2):
        intersection = set(codeTokens1).intersection(set(codeTokens2))
        union = set(codeTokens1).union(set(codeTokens2))
        # eğer kodlar boşsa 0 a bölünme hatası olmaması için ve uyarı vermek için 2 döndürülür
        if codeTokens1 == [] or codeTokens2 == []:
            return "boş kod"
        similatiry = len(intersection)/len(union)
        return similatiry

    # benzerlik oranının bulanık mantık ile değerlendirilmesi
    def fuzzy_logic(self,similarity_value):

        if similarity_value == "boş kod":
            return "Lütfen Kodları Giriniz"
        elif similarity_value >= 0.9:
           return "Aynı Kodlar"
        elif similarity_value >= 0.8:
                 return "Çok Çok Benzer Kodlar"
        elif similarity_value >= 0.7:
                 return "Çok Benzer Kodlar"
        elif similarity_value >= 0.6:
                return "Benzer Kodlar"
        elif similarity_value >= 0.5:
                return "Benzer Kodlar"
        elif similarity_value >= 0.4:
                return "Az Benzer Kodlar"
        
        else:
                return "Benzerlik Yok" + "  " +str(similarity_value)
    # butona basıldığında çalışacak fonksiyon
    def function(self):
        text1 = self.text1_input.toPlainText()
        text2 = self.text2_input.toPlainText()
        tokens1 = self.tokenize(text1)
        tokens2 = self.tokenize(text2)
        self.output_label.setText(self.fuzzy_logic(self.jaccard_similarity(tokens1,tokens2)))
    
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = TokenizerApp()
    ex.setGeometry(100, 100, 700, 500)
    ex.show()
    sys.exit(app.exec_())
