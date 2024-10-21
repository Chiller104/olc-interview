class HTMLElement:
    def render(self):
        raise NotImplementedError("Subclasses should implement this!")

class Input(HTMLElement):
    def __init__(self, input_type, placeholder, style=""):
        self.input_type = input_type
        self.placeholder = placeholder
        self.style = style

    def render(self):
        return f"<input type='{self.input_type}' placeholder='{self.placeholder}' style='{self.style}' />"

class Select(HTMLElement):
    def __init__(self, name, options, style=""):
        self.name = name
        self.options = options
        self.style = style

    def render(self):
        options_html = ''.join(f"<option value='{option}'>{option}</option>" for option in self.options)
        return f"<select name='{self.name}' style='{self.style}'>{options_html}</select>"

class Anchor(HTMLElement):
    def __init__(self, href, text, style=""):
        self.href = href
        self.text = text
        self.style = style

    def render(self):
        return f"<a href='{self.href}' style='{self.style}'>{self.text}</a>"

class Image(HTMLElement):
    def __init__(self, src, alt, style=""):
        self.src = src
        self.alt = alt
        self.style = style

    def render(self):
        return f"<img src='{self.src}' alt='{self.alt}' style='{self.style}' />"

class Div(HTMLElement):
    def __init__(self, content, style=""):
        self.content = content
        self.style = style

    def render(self):
        return f"<div style='{self.style}'>{self.content}</div>"

class Form(HTMLElement):
    def __init__(self, action, method, elements):
        self.action = action
        self.method = method
        self.elements = elements

    def render(self):
        elements_html = ''.join(f"<div>{element.render()}</div>" for element in self.elements)
        return f"<form action='{self.action}' method='{self.method}'>{elements_html}</form>"

class CSS:
    @staticmethod
    def generate_css():
        return """
        <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        input {
            border: 1px solid #000;
            padding: 5px;
            margin: 5px 0;
            width: 100%;
        }
        select {
            background-color: #f0f0f0;
            margin: 5px 0;
            width: 100%;
        }
        div {
            width: 40%;
            margin-left: 30%;
            padding: 10px;
            border: 1px solid #ccc;
        }
        a {
            color: blue;
            text-decoration: none;
        }
        img {
            width: 100%;
            height: auto;
        }
        </style>
        """

def create_registration_form():
    elements = [
        Input('text', 'meno'),
        Input('email', 'email'),
        Input('password', 'heslo'),
        Select('gender', ['Muž', 'Žena', 'Iné']),
        Anchor('https://www.olc.cz/', 'Odkaz na našu stránku'),
        Image('company.jpg', 'Firma OCL'),
        Input('submit', 'submit', 'Odoslať')
    ]

    form = Form(action='/submit', method='post', elements=elements)
    
    return f"<html><head>{CSS.generate_css()}</head><body>{form.render()}</body></html>"

def save_form_to_file(filename):
    html_content = create_registration_form()
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(html_content)

if __name__ == "__main__":
    save_form_to_file('form.html')
    print("Formulár bol úspešne uložený do form.html.")