import pyautogui
import time
from datetime import datetime
import os

def processoBuscar02():

    print("Coleta de dados 031 iniciado com  sucesso")
    os.system("taskkill /f /im chrome.exe")
    os.system("taskkill /f /im Excel.exe")
    os.system("taskkill /f /im msedge.exe")
    time.sleep(1)
    pyautogui.hotkey("win","r")
    pyautogui.write('"C:\Program Files\Google\Chrome\Application\chrome.exe"')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.hotkey("ctrl", "shift", "n")
    time.sleep(4)
    pyautogui.hotkey("win", "up")
    pyautogui.hotkey("win", "up")
    time.sleep(4) 

    busca = 0
    cont = 0
    while busca == 0:
        cont = cont + 1   
        print("procurando Barra de Endereco  ",cont)
        if cont == 15:
            busca = 1
            iniciando()      
       
        else:    
            if(pyautogui.locateOnScreen('C:/Users/SUPORTE TI/Desktop/Robo455/barraNavegacao.png')):
                print("----> Barra de captura Clicado na tentativa de numero: ",cont)
                busca = 1   

    pyautogui.click('C:/Users/SUPORTE TI/Desktop/Robo455/barraNavegacao.png')
    pyautogui.write('https://sistema.ssw.inf.br')
    time.sleep(0.25)
    pyautogui.press('enter')
    
    busca = 0
    cont = 0
    time.sleep(4)

    pyautogui.press('up')
    pyautogui.press('up')
    pyautogui.write('rvi')
    pyautogui.press('shift')
    time.sleep(1)
    pyautogui.write('38102226234')
    pyautogui.press('shift')
    time.sleep(1)
    pyautogui.write('fabio',0.25)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.press('shift')
    pyautogui.write('820425')
    time.sleep(2)
    pyautogui.hotkey("shift", "+")
    pyautogui.press('enter')
    time.sleep(5) 
    pyautogui.write('031')
    busca = 0
    cont = 0

    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')

    
    time.sleep(0.50)
    
    now = datetime.now() # current date and time
    inicial =  now.strftime("01%m") 
    ano =  now.strftime("%Y")
    dia = now.strftime("%d")
    mes = now.strftime("%m")
    ano = str(ano)
    ano = ano.replace("20","")

    inicial = inicial+ano
    fim = dia+mes+ano
    print(inicial)
    print(fim)
    
    nomeArquivo = now.strftime("031-%m%Y")

    pyautogui.write(inicial)
    
    pyautogui.write(fim)
    time.sleep(2)
    pyautogui.write('01')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.write('S')
    time.sleep(2)
    
    
    pyautogui.hotkey("shift", "+")
    time.sleep(1)
    pyautogui.press('enter')
   



    busca = 0
    cont = 0
    while busca == 0:
        cont = cont + 1   
        print("procurando Atualizar:  ",cont)
        if cont == 60:

            iniciando()  
            
        else:    
            if(pyautogui.locateOnScreen('C:/Users/SUPORTE TI/Desktop/Robo455/atualizar031.png')):
                print("----> Atualizar Clicado na tentativa de numero: ",cont)
                pyautogui.click('C:/Users/SUPORTE TI/Desktop/Robo455/atualizar031.png')

                busca = 1  
                 
    time.sleep(1)
    busca = 0
    cont = 0

    while busca == 0:
        cont = cont + 1   
        time.sleep(1)
        print("procurando Baixar:  ",cont)
        if cont == 36:
            iniciando()  
        else: 
            if(pyautogui.locateOnScreen('C:/Users/SUPORTE TI/Desktop/Robo455/baixar031.png')):
                pyautogui.click('C:/Users/SUPORTE TI/Desktop/Robo455/baixar031.png')
                busca = 1
            else:
                print("procurando Atualizar:  ",cont)
                if cont == 35:
                    iniciando()  
                    
                else:    
                   if(pyautogui.locateOnScreen('C:/Users/SUPORTE TI/Desktop/Robo455/atualizar031.png')):
                        print("----> Atualizar Clicado na tentativa de numero: ",cont)
                        pyautogui.click('C:/Users/SUPORTE TI/Desktop/Robo455/atualizar031.png')
                          
  
    busca = 0
    cont = 0
    while busca == 0:
        cont = cont + 1   
        print("procurando csv:  ",cont)
        if cont == 15:
            busca = 1
            iniciando()  
            
        else:    
            if(pyautogui.locateOnScreen('C:/Users/SUPORTE TI/Desktop/Robo455/AbrirCsv031.png')):
                print("----> Abirir Csv Clicado na tentativa de numero: ",cont)
                pyautogui.click('C:/Users/SUPORTE TI/Desktop/Robo455/AbrirCsv031.png')
                busca = 1   
       


    busca = 0
    cont = 0
    while busca == 0:
        cont = cont + 1   
        print("procurando aviso1:  ",cont)
        if cont == 4:
            busca = 1
        else:    
            if(pyautogui.locateOnScreen('C:/Users/SUPORTE TI/Desktop/Robo455/aviso1.png')):
                print("----> Aviso1  Clicado na tentativa de numero: ",cont)
                pyautogui.press("esc")
                time.sleep(1)
                pyautogui.press('esc')
                busca = 1

    
    busca = 0
    cont = 0
    while busca == 0:
        cont = cont + 1   
        print("procurando aba:  ",cont)
        if cont == 30:
            
            iniciando()  
            
        else:    
            if(pyautogui.locateOnScreen('C:/Users/SUPORTE TI/Desktop/Robo455/nomeAba031.png')):
                print("----> nomeAba  Clicado na tentativa de numero: ",cont)
                pyautogui.doubleClick('C:/Users/SUPORTE TI/Desktop/Robo455/nomeAba031.png')
                busca = 1
   
    pyautogui.write('031')
    pyautogui.press("enter")

    busca = 0
    cont = 0
    while busca == 0:
        cont = cont + 1   
        print("procurando Salvar:  ",cont)
        if cont == 15:

            iniciando()  
            
        else:    
            if(pyautogui.locateOnScreen('C:/Users/SUPORTE TI/Desktop/Robo455/salvarExcel.png')):
                print("----> salvarExcel  Clicado na tentativa de numero: ",cont)
                pyautogui.click('C:/Users/SUPORTE TI/Desktop/Robo455/salvarExcel.png')
                busca = 1

                
    busca = 0
    cont = 0
    while busca == 0:
        cont = cont + 1   
        print("procurando aviso:  ",cont)
        if cont == 15:
            busca = 1 
            
        else:    
            if(pyautogui.locateOnScreen('C:/Users/SUPORTE TI/Desktop/Robo455/aviso.png')):
                print("----> aviso  Encontrado na tentativa de numero: ",cont)
                pyautogui.press("esc")
                busca = 1
    time.sleep(0.25)    
    busca = 0
    cont = 0

    while busca == 0:
        cont = cont + 1   
        print("procurando Diretorio:  ",cont)
        if cont == 15:
            iniciando()  
        else:  
            if(pyautogui.locateOnScreen('C:/Users/SUPORTE TI/Desktop/Robo455/diretorio031.png')):
                print("----> Diretorio  Clicado na tentativa de numero: ",cont)
                pyautogui.click('C:/Users/SUPORTE TI/Desktop/Robo455/diretorio031.png')
                busca = 1
    time.sleep(1)   

   
    while busca == 0:
        cont = cont + 1   
        print("procurando aba031:  ",cont)
        if cont == 15:
            iniciando()  
        else:  
            if(pyautogui.locateOnScreen('C:/Users/SUPORTE TI/Desktop/Robo455/Aba031.png')):
                print("----> Diretorio  Clicado na tentativa de numero: ",cont)
                pyautogui.click('C:/Users/SUPORTE TI/Desktop/Robo455/Aba031.png')
                time.sleep(1)
                busca = 1
                pyautogui.write('I:\Meu Drive\bi031\bi031\01')
                time.sleep(1)
                pyautogui.press('enter')
    time.sleep(1)   


    #busca = 0
    #cont = 0
    #while busca == 0:
        #cont = cont + 1   
        #print("procurando Nome File:  ",cont)
        #if cont == 15:
            #busca = 1
           # iniciando()  
            
        #else: 
            # time.sleep(1)   
            # if(pyautogui.locateOnScreen('C:/Users/SUPORTE TI/Desktop/Robo455/nomeFile.png')):
               # print("----> Nome file  Clicado na tentativa de numero: ",cont)
               # pyautogui.click('C:/Users/SUPORTE TI/Desktop/Robo455/nomeFile.png')
               # busca = 1
                #pyautogui.hotkey("ctrl", "a")
                #pyautogui.press('delete')
               # pyautogui.write(nomeArquivo)
                #time.sleep(1)
               # pyautogui.press("right")
               # pyautogui.press("tab")
               # pyautogui.press("down")
                
                

   # busca = 0
   # cont = 0
   # while busca == 0:
    #    cont = cont + 1   
     #   print("procurando excel97:  ",cont)
     #   if cont == 15:

        #    iniciando()  
       # else: 
        #    if(pyautogui.locateOnScreen('C:/Users/SUPORTE TI/Desktop/Robo455/excel97.png')):
        #        print("----> Excel97  Clicado na tentativa de numero: ",cont)
        #        pyautogui.click('C:/Users/SUPORTE TI/Desktop/Robo455/excel97.png')
        #        pyautogui.press("enter")
        #        busca = 1
                
    busca = 0
    cont = 0
    while busca == 0:
        cont = cont + 1   
        print("procurando sim:  ",cont)
        if cont == 15:
            busca = 1
        else:    
            if(pyautogui.locateOnScreen('C:/Users/SUPORTE TI/Desktop/Robo455/sim.png')):
                print("----> sim  Clicado na tentativa de numero: ",cont)   
                pyautogui.click('C:/Users/SUPORTE TI/Desktop/Robo455/sim.png')
                busca = 1 
                
    time.sleep(15)                   
    os.system("taskkill /f /im chrome.exe")
    os.system("taskkill /f /im Excel.exe")
    os.system("taskkill /f /im Edge.exe")
    pyautogui.hotkey("win", "d")    
    busca = 0
    cont = 0
    while busca == 0:
        cont = cont + 1   
        print("procurando VS:  ",cont)
        if cont == 2:
            busca = 1
        else:    
            if(pyautogui.locateOnScreen('C:/Users/SUPORTE TI/Desktop/Robo455/vs.png')):
                print("----> VS  Clicado na tentativa de numero: ",cont)   
                pyautogui.click('C:/Users/SUPORTE TI/Desktop/Robo455/vs.png')
                busca = 1
    contador = 0
    resto = 1800
    while contador < 1800:
        contador = contador + 1

        time.sleep(1)
        print("Tempo restante de Espera: ", round((resto - contador)/60))                     
    iniciando()              
           
    
    
def iniciando():
  processoBuscar02()
  print("Coleta coleta")
    

iniciando()  











    
   