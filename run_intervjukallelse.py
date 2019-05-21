from read_excel import getReceivers, getLogin, getHeader
import pyperclip



receivers = getReceivers()

for receiver in receivers:
    print(receiver[1])
    mail = receiver[0]
    pyperclip.copy(mail)
    input("mail")
    subject = receiver[2]
    pyperclip.copy(subject)
    input("subject")
    contentFile = open("text_file.txt", "w")


    ##Enter text from here
    contentFile.write("hej ")
    contentFile.write(receiver[0])
    contentFile.write("\n\nVi i Valberedningen vill kalla er till intervju inför [skriv vilket möte].")
    contentFile.write("\n\nVi har bokat följande tid och plats för er intervju:\n")
    contentFile.write(receiver[3])
    contentFile.write("i sal ")
    contentFile.write(receiver[4])
    contentFile.write("\n\nVänligen meddela oss om denna tid passar eller ej.")
    contentFile.write("\nMed vänlig hälsning,")


    ##Do not enter text after here
    contentFile.close()
    contentFile = open("alt_file.txt")
    pyperclip.copy(contentFile.read())
    contentFile.close()
    input("content")
