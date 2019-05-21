from code_files.read_excel import getReceivers, getLogin, getHeader
import pyperclip



receivers = getReceivers()

for receiver in receivers:
    print(receiver[0])
    mail = receiver[2]
    pyperclip.copy(mail)
    input("mail")
    pyperclip.copy("Nominerad till Utskottsordförande 19/20")
    input("subject")
    contentFile = open("alt_file.txt", "w")
    contentFile.write("hej ")
    contentFile.write(receiver[0])
    contentFile.write(",\n\nDu har blivit nominerad till Utskottsordförande läsåret 19/20.\nDe utskott du blivit nominerad till ordförande för är:\n")
    for i in range(3, len(receiver)):
        if(receiver[i] == ""):
            break;
        contentFile.write(receiver[i])
        contentFile.write("\n")
    contentFile.write("\nVill ni vet mer om vad dessa poster innebär kan du göra det här: https://www.i-portalen.se/article/1107/")
    contentFile.write("\nVill ni fortsätta i Valberedningens process för att bli nominerad till en post ber vi er fylla i denna enkät: https://forms.gle/FLBMW8R1NZQ5d2PG8/ \nSista dag att fylla i denna enkät är fredag 26/4.\n\nMed vänlig hälsning,")
    contentFile.close()
    contentFile = open("alt_file.txt")
    pyperclip.copy(contentFile.read())
    contentFile.close()
    input("content")
