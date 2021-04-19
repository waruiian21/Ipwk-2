from flask import render_template
from . import main

# Handle errors
@main.app_errorhandler(404)
def page_not_found(error):
    '''
    Renders a 404 error page
    :param e:
    :return: render template 404.html
    '''
    return render_template('404.html'),404


