# Reads from files to create a template of for the mail
# This takes the text from 4 different files and combines them to make a HMTL template that can be rendered
def fillTemplate():
    emailTemplateFile = open("templates/email_content.html", "w")
    emailHTMLFile = open("templates/template_start.html")
    emailTemplateFile.write(emailHTMLFile.read())
    emailHTMLFile.close()

    printText(emailTemplateFile)

    emailHTMLFile = open("templates/template_end.html")
    emailTemplateFile.write(emailHTMLFile.read())
    emailHTMLFile.close()
    emailTemplateFile.close()

# Makes sure that there are new_line where it should be
def printText(emailTemplateFile):
    emailContentFile = open("Files/email_text.txt")
    text = emailContentFile.read()

    for c in text:
        if c == "\n":
            emailTemplateFile.write("<br>")
        else:
            emailTemplateFile.write(c)

    emailContentFile.close()
