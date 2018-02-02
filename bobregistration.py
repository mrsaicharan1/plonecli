# -*- coding: utf-8 -*-


class RegEntry(object):
    def __init__(self):
        self.template = ''
        self.plonecli_alias = ''
        self.depend_on = None


# standalone template
def plone_addon():
    reg = RegEntry()
    reg.template = 'bobtemplates.plone:addon'
    reg.plonecli_alias = 'addon'
    return reg

#buildout
def plone_buildout():
    reg = RegEntry()
    reg.template = 'bobtemplates.plone:buildout'
    reg.plonecli_alias = 'run_buildout'
    return reg
    
# sub template
def plone_theme():
    reg = RegEntry()
    reg.template = 'bobtemplates.plone:theme'
    reg.plonecli_alias = 'theme'
    reg.depend_on = 'plone_addon'
    return reg