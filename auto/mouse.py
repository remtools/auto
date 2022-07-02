import pyautogui
import random
import time

class mouse:

    def __init__(self,verbouse=True):
        self.screensize=pyautogui.size();
        self.verbouse=verbouse;
        self.speed=0.5;
        self.location=[0,0]
        self.sleep=1;
        self.box=None;
  
    def debug(self,message):
        if(self.verbouse): print(message);

    def randpos(self):
        return [random.randrange(0,self.screensize[0]),random.randrange(0,self.screensize[1])];
 
    def makemoves(self,n):
        i = 0
        while i < n:
            pos=self.randpos()
            self.debug("Moving to "+str(pos[0])+" "+str(pos[1]))
            pyautogui.moveTo(pos[0],pos[1],self.speed)
            time.sleep(self.sleep);
            i+=1
 
    def moveto(self,x,y,click=False):
        pyautogui.moveTo(x,y,self.speed)
        self.location=[x,y]
        if(click==True):
            self.debug("Click")            
            pyautogui.click()
        
    def getlocation(self,needlefile,wait=0):
        self.debug("Find "+needlefile);
        if(wait>0):
            n=0;
            while(n<wait):  
                try:
                    self.box=pyautogui.locateOnScreen(needlefile)
                except Exception as e:
                    self.debug(e);
                time.sleep(self.sleep)
                n+=1;
            time.sleep(self.sleep);
        else:
            try:
                self.box=pyautogui.locateOnScreen(needlefile)
            except Exception as e:
                self.debug(e)
        if(self.box!=None):
            self.debug("Found at "+str(self.box[0])+" "+str(self.box[1]));
        else:
            self.debug("Did not Find "+needlefile);
        return self.box;
 
    def boxcenter(self,box):
        return [box[0]+int(box[2]/2),box[1]+int(box[3]/2)]
  
    def boxcenterright(self,box):
        return [box[0]+int(box[2]),box[1]+int(box[3]/2)]
        
        
    def findandgo(self,needlefile,click=False,wait=0):
        success=False;
        self.box=self.getlocation(needlefile,wait);
        if(self.box!=None):
            self.pos=self.boxcenter(self.box)
            self.moveto(self.pos[0]+10,self.pos[1],click) # click
            success=True;
        return success
        
        
        
        
        
        