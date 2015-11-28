# -*- coding: utf-8 -*-
from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer

from zope.component import getUtility
from plone.registry.interfaces import IRegistry

from collective.gitter.interfaces import IGitterControlPanel


@implementer(INonInstallable)
class HiddenProfiles(object):

    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller"""
        return [
            'collective.gitter:uninstall',
        ]


def post_install(context):
    """Post install script"""
    registry = getUtility(IRegistry)
    registry.registerInterface(IGitterControlPanel)
    if context.readDataFile('collectivegitter_default.txt') is None:
        return
    # Do something during the installation of this package
    


def uninstall(context):
    """Uninstall script"""
    if context.readDataFile('collectivegitter_uninstall.txt') is None:
        return
    # Do something during the uninstallation of this package
