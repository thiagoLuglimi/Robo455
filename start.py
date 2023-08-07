import pyautogui
import time
import os

print("Victor")
# Abrir ssw no navegador 
pyautogui.alert('Atenção!!! o  Processo vai ser iniciado')
i = 0
while i < 1:
    os.system("taskkill /f /im chrome.exe")
    time.sleep(10)
    pyautogui.PAUSE = 0.5
    pyautogui.hotkey("winleft", "r")
    pyautogui.write('https://sistema.ssw.inf.br/bin/ssw0422')
    pyautogui.press('enter')

    time.sleep(2)
    #pyautogui.press('enter')
     ####### Play Relatorio ######
    pyautogui.press('enter')
    pyautogui.hotkey("shift", "+")
    pyautogui.press('enter') 
  
    time.sleep(3)
    pyautogui.write('455')
    time.sleep(2)
    """pyautogui.hotkey("alt", "space", "x")
    time.sleep(5)"""
    """                 
    ## Login 
    #pyautogui.doubleClick(741, 199)
    #pyautogui.write('00401794270')
    #print(pyautogui.position())
    #pyautogui.doubleClick(743, 217)
    #pyautogui.write('victor')
    #pyautogui.doubleClick(742, 234)
    #pyautogui.write('1140595')

    ####### Click PLAY ########
    pyautogui.click(745, 191)
    
    ####### Click Operação ########
    pyautogui.click(190, 141)
    time.sleep(2.0)
    pyautogui.write('455')
    
    
    ####### Limpa Campo ########
    time.sleep(5.0)
    pyautogui.doubleClick(183, 211)
    pyautogui.press('delete')
    pyautogui.doubleClick(253, 211)
    pyautogui.press('delete')
    
    ####### Preenche Emissao ######
    pyautogui.click(176, 194)
    pyautogui.write('280422')
    pyautogui.click(255, 192)
    pyautogui.write('280422')
    
    ####### Tipo de Relatorio ######
    pyautogui.doubleClick(168, 501)
    pyautogui.write('e')
    time.sleep(1)
    pyautogui.doubleClick(167, 513)
    pyautogui.write('a')
    time.sleep(2)
    pyautogui.write('b')
    time.sleep(2)
    pyautogui.write('h')
    
    ####### Play Relatorio ######
    pyautogui.hotkey("shift", "+")
    pyautogui.press('enter')
    
    time.sleep(3)
    
    ### Ir para Fila ###
    pyautogui.click(410, 349)
    
    ### Atualizar Fila ###
    time.sleep(2)
    pyautogui.click(982, 132)
    
    time.sleep(10)
    pyautogui.click(982, 132)
    
    time.sleep(10)
    pyautogui.click(982, 132)
    
    
    time.sleep(20)
    pyautogui.click(982, 132)
    
    time.sleep(20)
    pyautogui.click(982, 132)
    
    time.sleep(20)
    pyautogui.click(982, 132)
    
    time.sleep(2)
    pyautogui.click(982, 132)
    time.sleep(10)
    ### Baixar Relatorio ###
    pyautogui.click(776, 168)
    time.sleep(15)
    
    os.system("taskkill /f /im chrome.exe")
    """
    #time.sleep(2)
    #pyautogui.click(1075, 135)
    #time.sleep(2)
    #pyautogui.click(1075, 135)
    #time.sleep(2)
    #pyautogui.click(1075, 135)
    #time.sleep(2)
    #pyautogui.click(1075, 135)

    #time.sleep(2)
    #pyautogui.click(1075, 135)
    #time.sleep(2)
    #pyautogui.click(1075, 135)
    #time.sleep(2)
    #pyautogui.click(1075, 135)
    #time.sleep(2)
    #pyautogui.click(1075, 135)
    #time.sleep(15)
    #pyautogui.click(1075, 135)

    #time.sleep(1)
    #pyautogui.click(850, 179)
    #time.sleep(3)

    #pyautogui.press('winleft')
    #pyautogui.write('bloco de')
    #pyautogui.press('enter')
    #time.sleep(3)    #pyautogui.write('############################ CONCLUIDO MEU REI!!!!! ####################################')


    #pyautogui.hotkey("ctrl", "t")




    # TECLAS DE ATALHO
    # pyautogui.hotkey("tecla1", "tecla2")

    # PEGA A POSIÇÃO DO MOUSE
    # pyautogui.position() 

    # Fazer login
    # Digitar 455
    
    
    
    
