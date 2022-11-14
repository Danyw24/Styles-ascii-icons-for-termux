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
    BLACK   = '\033[30m'
    RED     = '\033[31m'
    GREEN   = '\033[32m'
    YELLOW  = '\033[33m'
    BLUE    = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN    = '\033[36m'
    WHITE   = '\033[37m'
    RESET   = '\033[39m'

class bg:
    BLACK   = '\033[40m'
    RED     = '\033[41m'
    GREEN   = '\033[42m'
    YELLOW  = '\033[43m'
    BLUE    = '\033[44m'
    MAGENTA = '\033[45m'
    CYAN    = '\033[46m'
    WHITE   = '\033[47m'
    RESET   = '\033[49m'

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

except Exception:
    if Exception == KeyError:
        print(icons.success,"Thanks for using my tool!")

    elif Exception == ModuleNotFoundError:
        print(icons.error,"An error has ocurred with dependences, Please, verify your modules with \033[34mpip freeze");
        

def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyaddr(hostname)
    return hostname, ip_address

def animation_1():
    hostname, ip = get_ip_address()
    img_num = random.randint(0,len(images))
    os.system("clear")
    print(ascii_images.bomb)
    with alive_progress.alive_bar(100, dual_line=True,  title='Loading') as bar:
        for c in range(100):
            sleep(0.05)
            bar()
    os.system("clear")
    print(f"{bg.GREEN} Host: {hostname} address: {ip[2]} {bg.RESET}")
        



if __name__ == "__main__":
    animation_1()
    
    