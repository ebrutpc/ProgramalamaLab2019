class myClass():
    def __init__(self,myFile=" "):
        f=open(("Text.txt","r"))
        myContent=f.read()
        mySentences=myContent.split(".")
        self.myWords=[]
        for sentence in mySentences:
            Wordss_in_th_Sentence=sentence.split(" ")
            for word_1 in Wordss_in_th_Sentence:
                self.myWords.append(word_1)
        self.my_frequency_1()
        self.write_frequency_1()
        self.my_frequency_2()
        self.write_frequency_2()

def my_frequency_1(self):
    self.frequency_list_1={}
    for word in self.myWords:
        if(word in self.frequency_list_1):
            self.frequency_list_1[word]+=1
        else:
            self.frequency_list_1[word]=1

def my_frequency_2(self):
    self.frequency_list_2={}
    for i in range(len(self.myWords)-1):
        w_1,w_2=self.myWords[i],self.myWords[i+1]
        if((w_1,w_2) in self.frequency_list_2):
            self.frequency_list_2[(w_1,w_2)]+=1
        else:
            self.frequency_list_2[(w_1 , w_2)] =1
def write_frequency(self):
    for w_1 in self.frequency_list_2:
        print(str(w_1)+" "+str(self.frequency_list_2[w_1]))

myClass1=myClass()


def write_frequency(self):
    for word_1 in self.frequency_list_1:
        print(word_1+" "+str(self.frequency_list_1[word_1]))

