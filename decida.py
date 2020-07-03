import random
import time

 
class DecidaPorMim:
    def __init__(self):
        self.resposta = ["Vamos nessa Garotão", "Demorou!", "Nem de graça","Arrocha!", "É um brincante!!","Só vai se tiver grana","Com certeza"]

    def InicioPrograma(self):
        print("Vamos inciar o programa, caso queira sair é só digitar \"N\"")
        self.FazerPergunta()


    def FazerPergunta(self):
        self.respostaOne = input("Digite sua pergunta: ")
        self.respostaOne = self.respostaOne.upper()

        if self.respostaOne == "N": 
            print("Saindo do programa")

        elif self.respostaOne == "S":
            print("pensando...")
            time.sleep(2)
            print("Resposta: ",random.choice(self.resposta))
            self.respostaRepet = input("Voce gostaria de fazer outra pergunta? (S/N)")
            self.respostaRepet = self.respostaRepet.upper()

            if self.respostaRepet == "S":
                self.FazerPergunta()
            elif self.respostaRepet == "N":  
                print("Fechando programa")  
            else:
                print("O sistema só permite apenas a inserção de S ou N")
                self.FazerPergunta()

        else:
            print("O sistema só permite apenas a inserção de S ou N")
            self.FazerPergunta()


DecidaPorMim().InicioPrograma()
