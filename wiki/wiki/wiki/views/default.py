from pyramid.view import view_config

from ..models import MyModel


@view_config(context=MyModel, renderer='../templates/mytemplate.jinja2')
def my_view(request):
    return {'project': 'wiki'}
