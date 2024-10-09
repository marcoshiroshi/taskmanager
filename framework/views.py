from django.views.generic import TemplateView
from django.template import loader


class Framework(TemplateView):

    def get_template_names(self):
        path = self.request.path.replace("/framework", "")
        load_template = '/index.html' if path == '/' else path
        template = loader.get_template('00_framework' + load_template)
        self.template_name = template

        return self.template_name