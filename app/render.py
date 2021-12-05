from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template, render_to_string

import os
from os.path import basename
import pdfkit
from django.template import loader
import os
from io import BytesIO



class Render:

    @staticmethod
    def render(path: str, data):
        
        template = get_template(path)
        html = template.render({"name": data.name,"email":data.email,"id":data.id})
        io = BytesIO()
        output = pdfkit.from_string(html, output_path=False)
        print(type(output))
        response = HttpResponse(content_type="application/pdf")
        response.write(output)
        return response
