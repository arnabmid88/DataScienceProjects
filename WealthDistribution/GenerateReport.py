# -*- coding: utf-8 -*-
from jinja2 import Environment,FileSystemLoader
from datetime import datetime
def write(context):
    path = "report-%s.html" %datetime.now().strftime("%Y%m%d")
    jinjaenv = Environment(loader = FileSystemLoader('template'))
    template = jinjaenv.get_template('report.html')
    template.stream(context).dump(path)