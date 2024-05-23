class Signal(object):
    def __init__(self):
        self.receivers=[]

    def output(self):
        print(self.receivers)
    def connect(self,receiver):
        self.receivers.append(receiver)
    def send(self):
        for receiver in self.receivers:
            receiver()

def called():
    print("i was called")
def another_called():
    print("i too was called")

s=Signal()
s.connect(called)
s.connect(another_called)

s.output()
s.send()