from tkinter import *
from translate import Translator
root=Tk()
root.geometry('800x800')
root.config(bg='light green')
root.attributes("-fullscreen",True)
Label(root,text="HEYA! WELCOME TO OUR LANGUAGE TRANSLATOR",font=('times',36),fg='red',bg='light blue').pack(fill="both")
def create():
    from translate import Translator
    win=Tk()
    win.geometry("800x800")
    win.config(bg='light blue')
    win.attributes("-fullscreen",True)
    win.title("Language Translator")
    LanguageChoices = {'Hindi','English','French','German','Spanish'}
    w=Label(win,text="    L  A  N  G  U  A  G  E      T  R  A  N  S  L  A  T  O  R   ",relief='solid',font=('times',26),fg='black',bg='red').pack(fill="both")
    x=Label(win,text="  W E L C O M E    T O    O U R   S O F T W A R E   ",relief='ridge',font=('times',22),fg='red',bg='yellow').place(x=330,y=60)
    InputLanguageChoice=StringVar()
    TranslateLanguageChoice=StringVar()
    
    InputLanguageChoice.set('English')
    TranslateLanguageChoice.set('Hindi')
    
    #### creating of function
    def Translate():
        translator = Translator(from_lang= InputLanguageChoice.get(),to_lang=TranslateLanguageChoice.get())
        Translation = translator.translate(var1.get())
        var2.set(Translation)
        
    #### choice for input language
    InputLanguageChoiceMenu=OptionMenu(win,InputLanguageChoice,*LanguageChoices)
    Label(win,text='Choose a language',font=('times',18)).place(x=0,y=100)
    InputLanguageChoiceMenu.place(x=200,y=100)
    
    ###choice for translated language
    NewLanguageChoiceMenu =OptionMenu(win,TranslateLanguageChoice,*LanguageChoices)
    Label(win,text='Translated language',font=('times',18)).place(x=0,y=340)
    NewLanguageChoiceMenu .place(x=200,y=340)
    
    #####creating entry box
    Label(win,text="ENTER WORDS:-",font=('times',22),fg='red',bg='light green').place(x=150,y=190)
    var1=StringVar()
    entry=Entry(win,width=60,textvariable=var1,font=('times',20,'italic bold')).place(x=400,y=190)
    
    Label(win,text="TRANSLATED:-",font=('times',22),fg='red',bg='light green').place(x=150,y=420)
    var2=StringVar()
    entry=Entry(win,width=60,textvariable=var2,font=('times',20,'italic bold')).place(x=400,y=420)
    
    ### button
    b1=Button(win,text='TRANSLATE',font=('times',18),command=Translate,relief=GROOVE).place(x=100,y=600)
    b2=Button(win,text='CLOSE THE SOFTWARE',font=('times',18),command=win.destroy,relief=GROOVE).place(x=900,y=600)
    win.mainloop()

def show():
    win2=Tk()
    win2.geometry("800x800")
    win2.config(bg='light blue')
    win2.attributes("-fullscreen",True)
    win2.title("CREDITS")
    Label(win2,text='THANKU FOR USING OUR SOFTWARE',font=('times',32)).pack(fill='both')
    Label(win2,text='OUR DESIGNERS',font=('times',32),fg='blue',bg='orange').pack(fill='both')
    Label(win2,text='RISHABH DIMRI',font=('times',32),fg='black',bg='light green').place(x=400,y=150)
    Label(win2,text='MAYANK RAI',font=('times',32),fg='black',bg='light green').place(x=400,y=250)
    Label(win2,text='KESHAV ANAND',font=('times',32),fg='black',bg='light green').place(x=400,y=350)
    Label(win2,text='ANKIT SINGH',font=('times',32),fg='black',bg='light green').place(x=400,y=450)
    Label(win2,text='AMIT KUMAR',font=('times',32),fg='black',bg='light green').place(x=400,y=550)

    ###buttons
    b=Button(win2,text='CLOSE',command=win2.destroy,font=('times',40)).place(x=1000,y=600)

### buttons for outer window
b1=Button(root,text='OPEN',command=create,font=('times',40)).place(x=500,y=200)
b2=Button(root,text='CLOSE',command=root.destroy,font=('times',40)).place(x=500,y=400)
b3=Button(root,text="CREDITS",command=show,font=('times',40)).place(x=500,y=600)

root.mainloop()