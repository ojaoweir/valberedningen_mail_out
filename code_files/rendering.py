from jinja2 import Environment, FileSystemLoader

# Renders a template with the text in Files/email_text.txt, the footer from Files/footer_picture.txt 
# and replaces with the correct variables for the receiver
def generateEmailTemplate(databaseHeader, receiver):
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template("./templates/email_content.html")
    template_variables = {}
    template_variables = {databaseHeader[i]: receiver[i] for i in range(2, len(databaseHeader))}
    return template.render(template_variables)
