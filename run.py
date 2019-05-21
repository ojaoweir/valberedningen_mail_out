from code_files.fill_template import fillTemplate
from code_files.read_excel import getReceivers, getLogin, getHeader
from code_files.send_mail import startServer,sendMail,closeServer
from code_files.rendering import generateEmailTemplate

# Step 1: Reading the text for the mail, styling it as a simple HTML
fillTemplate()

# Step 2: Reading the excel file
databaseHeader = getHeader()
receivers = getReceivers()

# Step 3: Connect to the mail server
login = getLogin()
server = startServer(login)

# Step 4: Send the email to all
for receiver in receivers:
    # Step 4.1: Generate the template with filled in values
    template = generateEmailTemplate(databaseHeader,receiver)
    # Step4.2 : Send the template
    sendMail(template,receiver[1],login[0],receiver[0],server)
    # Step4.3 : Repeat

# Step 5: Close Server
closeServer(server)

# Step 6: Close application
