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
    contentFile.write(",\n\nDu har blivit nominerad till poster inför [skriv vilket möte].\nDe poster du blivit nominerad till är:\n")
    for i in range(5, len(receiver)):
        if(receiver[i] == ""):
            break;
        contentFile.write(receiver[i])
        contentFile.write("\n")
    contentFile.write("\nVill ni fortsätta i Valberedningens process för att bli nominerad till en post ber vi er fylla i denna enkät:")
    contentFile.write("[länk till intervjuenkäten]")
    contentFile.write("\nSista dag att fylla i denna enkät är [datum].\n\nMed vänlig hälsning,")


    ##Do not enter text after here
    contentFile.close()
    contentFile = open("alt_file.txt")
    pyperclip.copy(contentFile.read())
    contentFile.close()
    input("content")
