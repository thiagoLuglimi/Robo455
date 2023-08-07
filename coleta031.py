import pyautogui
import time
import os
from datetime import datetime


def processoBusca():
    print("Coleta de Dados 455 iniciada com Sucesso!!!")
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
     #Fecha Lembrete
    busca = 0
    cont = 0
    while busca == 0:
        cont = cont + 1   
        print("procurando Barra de Endereco  ",cont)
        if cont == 15:
            busca = 1
            inicio()  
            
        else:    
            if(pyautogui.locateOnScreen('barraEndereco1.png')):
                print("----> Barra de Endereco Clicado na tentativa de numero: ",cont)
                busca = 1   
    pyautogui.click('barraEndereco1.png')
    pyautogui.write('https://sistema.ssw.inf.br')
    time.sleep(0.25)
    pyautogui.press('enter')
    
    busca = 0
    cont = 0
    time.sleep(4)
    pyautogui.hotkey("ctrl", "-")
    pyautogui.hotkey("ctrl", "-")
    pyautogui.hotkey("ctrl", "-")
    pyautogui.hotkey("ctrl", "-")
    pyautogui.press('up')
    pyautogui.press('up')
    pyautogui.write('rvi')
    pyautogui.press('shift')
    time.sleep(1)
    pyautogui.write('22677644584')
    pyautogui.press('shift')
    time.sleep(1)
    pyautogui.write('maquina',0.25)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.press('shift')
    pyautogui.write('maquina')
    time.sleep(2)
    pyautogui.hotkey("shift", "+")
    pyautogui.press('enter')
    time.sleep(5) 
    pyautogui.write('031')
    busca = 0
    cont = 0
    
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
    
    pyautogui.write(inicial)
    pyautogui.write(fim)
    time.sleep(3)
    nomeArquivo = now.strftime("ssw-031-%m%Y")

    pyautogui.write(inicial)
    
    pyautogui.write(fim)
    
    time.sleep(3)
    
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    
    pyautogui.write("64")
    
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.write("s")
    time.sleep(2)
    pyautogui.hotkey("shift", "+")
    pyautogui.press('enter')
    
    
    time.sleep(4)
    
    busca = 0
    cont = 0

    while busca == 0:
        cont = cont + 1   
        time.sleep(1)
        print("procurando Baixar:  ",cont)
        if cont == 36:
            inicio()  
        else: 
            if(pyautogui.locateOnScreen('baixar.png')):
                pyautogui.click('baixar.png')
                busca = 1
            else:
                print("procurando Atualizar:  ",cont)
                if cont == 35:
                    inicio()  
                    
                else:  
                    pyautogui.press('enter')
                          
    
   
    time.sleep(2)    
    busca = 0
    cont = 0
    while busca == 0:
        cont = cont + 1   
        time.sleep(1)
        print("abrirCsv Baixar:  ",cont)
        if cont == 36:
            inicio()  
        else: 
            if(pyautogui.locateOnScreen('abrirCsv.png')):
                pyautogui.click('abrirCsv.png')
                busca = 1
            else:
                print("procurando abrirCsv:  ",cont)
                if cont == 35:
                    inicio()  

    
    
    
    
    time.sleep(5)
   
    
    
    time.sleep(60) 
    busca = 0
    cont = 0
    while busca == 0:
        cont = cont + 1   
        print("procurando Nome File:  ",cont)
        if cont == 15:
            busca = 1
            inicio()  
            
        else: 
            time.sleep(1)   
            if(pyautogui.locateOnScreen('nomeFile.png')):
                print("----> Nome file  Clicado na tentativa de numero: ",cont)
                pyautogui.click('nomeFile.png')
                busca = 1
                pyautogui.hotkey("ctrl", "a")
                pyautogui.press('delete')
                pyautogui.write(nomeArquivo)
                time.sleep(1)
                pyautogui.press("right")
                pyautogui.press("tab")
                pyautogui.press("down")
                
                

    busca = 0
    cont = 0
    while busca == 0:
        cont = cont + 1   
        print("procurando excel97:  ",cont)
        if cont == 15:

            inicio()  
        else: 
            if(pyautogui.locateOnScreen('excel97.png')):
                print("----> Excel97  Clicado na tentativa de numero: ",cont)
                pyautogui.click('excel97.png')
                pyautogui.press("enter")
                busca = 1
                
    busca = 0
    cont = 0
    while busca == 0:
        cont = cont + 1   
        print("procurando sim:  ",cont)
        if cont == 15:
            busca = 1
        else:    
            if(pyautogui.locateOnScreen('sim.png')):
                print("----> sim  Clicado na tentativa de numero: ",cont)   
                pyautogui.click('sim.png')
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
            if(pyautogui.locateOnScreen('vs.png')):
                print("----> VS  Clicado na tentativa de numero: ",cont)   
                pyautogui.click('vs.png')
                busca = 1
    contador = 0
    resto = 1800
    while contador < 1800:
        contador = contador + 1

        time.sleep(1)
        print("Tempo restante de Espera: ", round((resto - contador)/60))                     
    inicio()              
           
    
    
def inicio():
  processoBusca()
  print("Coleta coleta")
    

inicio()  