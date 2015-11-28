from Products.CMFCore.utils import getToolByName
from zope.component import getUtility
from plone.registry.interfaces import IRegistry
from collective.gitter.interfaces import IGitterControlPanel


PROFILE_ID = "profile-collective.gitter:default"


def update_registry(context):
    registry = getUtility(IRegistry)
    registry.registerInterface(IGitterControlPanel)