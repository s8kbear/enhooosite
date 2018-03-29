from django.shortcuts import render, HttpResponse
from enhoooapp.models import House, Facility
# from django.template import Context, Template

# Create your views here.

def first_try(request):
    # brookstudio = House(name='Brookstudio', location='Selly Oak', postcode='B29 6BD')
    # html_string = '''
    #     <html>
    #         <head>
    #             <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.2.4/semantic.css" media="screen" title="no title" charset="utf-8">
    #         </head>
    #         <body>
    #         <h1 class="ui center aligned icon header">
    #             <i class="hand spock icon"></i>
    #             You are now at, {{ brookstudio.name }}
    #             It is located at {{ brookstudio.location }}
    #             The postcode is {{ brookstudio.postcode }}
    #         </h1>
    #         </body>
    #     </html>
    # '''
    # t = Template(html_string)
    # c = Context({'brookstudio': brookstudio})
    # web_page = t.render(c)
    # return HttpResponse(web_page)

def index(request):
    context = {}
    facility_list = Facility.objects.all()
    context['facility_list'] = facility_list
    index_page = render(request, 'web2.html', context)
    return index_page
