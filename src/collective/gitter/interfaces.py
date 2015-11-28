# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from zope import schema
from zope.interface import Interface


class IGitterControlPanel(Interface):

    show_sidecar = schema.Bool(
        title=u'Show gitter chatbox.',
        default=True,
        required=False,
    )
    show_on_all_pages = schema.Bool(
        title=u'Show on all pages',
        description=u'Show on all pages not just the front page',
        default=False,
        required=False,
    )
    gitter_room = schema.Text(
        title=u'Gitter room name',
        required=False,
    )


class ICollectiveGitterLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""
