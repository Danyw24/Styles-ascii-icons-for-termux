# Author: Danyw24
# 14/11/2022
# Description: intro on termux with style
# In etc/bash.bashrc modify and add python3 ./termux_intro.py

class ascii_images:
    
    bomb = """
                                 . . .                         
                              \|/                          
                            `--+--'                        
                              /|\                          
                             ' | '                         
                               |                           
                               |                           
                           ,--'#`--.                       
                           |#######|                       
                        _.-'#######`-._                    
                     ,-'###############`-.                 
                   ,'#####################`,               
                  /#########################\              
                 |###########################|             
                |#############################|            
                |#############################|            
                |#############################|            
                |#############################|            
                 |###########################|             
                  \#########################/              
                   `.#####################,'               
                     `._###############_,'                 
                        `--..#####..--'

         ______    ___  ____   ___ ___  __ __  __ __ 
        |      T  /  _]|    \ |   T   T|  T  T|  T  T
        |      | /  [_ |  D  )| _   _ ||  |  ||  |  |
        l_j  l_jY    _]|    / |  \_/  ||  |  |l_   _j
          |  |  |   [_ |    \ |   |   ||  :  ||     |
          |  |  |     T|  .  Y|   |   |l     ||  |  |
          l__j  l_____jl__j\_jl___j___j \__,_j|__j__|
                                         
    """
    skull2 =  """
         .... NO! ...                  ... MNO! ...
   ..... MNO!! ...................... MNNOO! ...
 ..... MMNO! ......................... MNNOO!! .
.... MNOONNOO!   MMMMMMMMMMPPPOII!   MNNO!!!! .
 ... !O! NNO! MMMMMMMMMMMMMPPPOOOII!! NO! ....
    ...... ! MMMMMMMMMMMMMPPPPOOOOIII! ! ...
   ........ MMMMMMMMMMMMPPPPPOOOOOOII!! .....
   ........ MMMMMOOOOOOPPPPPPPPOOOOMII! ...  
    ....... MMMMM..    OPPMMP    .,OMI! ....
     ...... MMMM::   o.,OPMP,.o   ::I!! ...
         .... NNM:::.,,OOPM!P,.::::!! ....
          .. MMNNNNNOOOOPMO!!IIPPO!!O! .....
         ... MMMMMNNNNOO:!!:!!IPPPPOO! ....
           .. MMMMMNNOOMMNNIIIPPPOO!! ......
          ...... MMMONNMMNNNIIIOO!..........
       ....... MN MOMMMNNNIIIIIO! OO ..........
    ......... MNO! IiiiiiiiiiiiI OOOO ...........
  ...... NNN.MNO! . O!!!!!!!!!O . OONO NO! ........
   .... MNNNNNO! ...OOOOOOOOOOO .  MMNNON!........
   ...... MNNNNO! .. PPPPPPPPP .. MMNON!........
      ...... OO! ................. ON! .......
         ................................


    """


class icons:
    success = "\033[32m[\033[39m√\033[32m]\033[39m"
    error =  "\033[31m[\033[39m!\033[31m]\033[39m"
    ask = "\033[36m[\033[39m?\033[36m]\033[39m"

class fg:
    black="\033[0;30m"
    red="\033[0;31m"
    bred="\033[1;31m"
    green="\033[0;32m"
    bgreen="\033[1;32m"
    yellow="\033[0;33m"
    byellow="\033[1;33m"
    blue="\033[0;34m"
    bblue="\033[1;34m"
    purple="\033[0;35m"
    bpurple="\033[1;35m"
    cyan="\033[0;36m"
    bcyan="\033[1;36m"
    white="\033[0;37m"
    nc="\033[00m"


class style:
    BRIGHT    = '\033[1m'
    DIM       = '\033[2m'
    NORMAL    = '\033[22m'
    RESET_ALL = '\033[0m'

dependences = ["socket","time","os","subprocess","random"]
images = [ascii_images.bomb, ascii_images.skull2]
try:
    import random
    import socket
    import os, subprocess
    from time import sleep
    import alive_progress
    from requests import get

except Exception:
    if Exception == KeyError:
        print(icons.success,"Thanks for using my tool!")

    elif Exception == ModuleNotFoundError:
        print(icons.error,"An error has ocurred with dependences, Please, verify your modules with \033[34mpip freeze");
        


def get_ip_address():
    ip = get('https://api.ipify.org').text
    return ip



def animation_1():
    ip = get_ip_address()
    os.system("clear")
    print(ascii_images.bomb)

    with alive_progress.alive_bar(100, dual_line=True,  title='Loading') as bar:
        for c in range(100):
            sleep(0.05)
            bar()
    os.system("clear")

    #second pard

    print(f"{fg.bgreen} [!] address: {ip} {fg.nc}")
        



if __name__ == "__main__":
    animation_1()
    
    