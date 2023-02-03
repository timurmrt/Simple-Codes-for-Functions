print("""
******* MORS ALHABET TRANSLATOR ******
    -- 1. Mors to Latin Translator --
    -- 2. Latin to Mors Translator --
    -- Please Press "Q" to Quit --
""")
sözlük= {"A":".-","B":"-...","C":"-.-.","D":"-..", "E":".", "F":"..-.", "G":"--.", "H":"....", "I":"..","J":".---",
         "K":"-.-", "L":".-..", "M":"--","N":"-.", "O":"---", "P":".--.", "Q":"--.-", "R":".-.", "S":"...", "T":"-",
         "U":"..-", "V":"...-", "W":".--", "X":"-..-", "Y":"-.--", "Z":"--.."}

sözlükmors= {".-":"A", "-...":"B", "-.-.":"C", "-..":"D", ".":"E", "..-.":"F", "--.":"G", "....":"H", "..":"I",
             ".---":"J","-.-":"K", ".-..":"L", "--":"M", "-.":"N", "---":"O", ".--.":"P", "--.-":"Q",
             ".-.":"R", "...":"S", "-":"T", "..-":"U", "...-":"V", ".--":"W", "-..-":"X", "-.--":"Y","--..":"Z"}


while True:
    translator = input("Please Select the Operation (1 or 2) : ")
    if translator.lower()=="q" :
        print("Process is being terminating...")
        break
    elif translator=="2":
        çeviri=[]
        print("PLEASE USE CAPITAL LETTERS!!")
        word=(input("Please enter the word you want to translate :"))
        word=list(word)
        for i in word:
            çeviri.append(sözlük[i])
        print(çeviri)


    elif translator=="1":
        çeviri=[]
        print("Enter the Mors Codes without Any Space")
        morsçeviri= []
        while True :
            mors = input(" Please Enter Your Mors Codes and press T To Decphyer: ")
            if mors.lower()=="t":
                print(morsçeviri)

            else:
                print(sözlükmors[mors])
                sözlükmors[mors]=str(sözlükmors[mors])
                morsçeviri.append(sözlükmors[mors])











