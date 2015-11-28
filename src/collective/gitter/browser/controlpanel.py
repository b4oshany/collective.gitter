# -*- coding: utf-8 -*-
from datetime import datetime
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.z3cform import layout
from plone.app.textfield import RichText
from zope import schema
from zope.interface import Interface
from z3c.form.interfaces import INPUT_MODE
from z3c.form import form, field
from plone.app.z3cform.wysiwyg import WysiwygFieldWidget
from plone import api
from zope.component import adapter
from plone.registry.interfaces import IRecordModifiedEvent

from collective.gitter.interfaces import IGitterControlPanel


class GitterControlPanelForm(RegistryEditForm):
    # this should give us a richtext widget for editing
    schema = IGitterControlPanel
    schema_prefix = "sidecar_gitter"
    label = u'Gitter Settings'


GitterControlPanelView = layout.wrap_form(
    GitterControlPanelForm, ControlPanelFormWrapper)