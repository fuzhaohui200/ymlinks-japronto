# from jinja2 import Template

# A view can read HTML from a file
def index(request):
    with open('index.html') as html_file:
        return request.Response(text=html_file.read(), mime_type='text/html')


# A view could also return a raw HTML string
def example(request):
    return request.Response(text='<h1>Some HTML!</h1>', mime_type='text/html')


# A view could also return a rendered jinja2 template
# def jinja(request):
#     template = Template('<h1>Hello {{ name }}!</h1>')
#     return request.Response(text=template.render(name='World'),
#                             mime_type='text/html')