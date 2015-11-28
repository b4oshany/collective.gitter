from datetime import datetime

from plone.app.layout.viewlets import ViewletBase
from plone import api
from zope.component import ComponentLookupError
from Products.CMFCore.interfaces import ISiteRoot
from zope.component import getMultiAdapter
from plone.app.layout.navigation.interfaces import INavigationRoot
from plone.api.exc import InvalidParameterError


class GitterViewlet(ViewletBase):
    """ viewlet that displays announcements """

    def data(self):
        _data = {
            "show_sidecar": False,
            "show_on_all_pages": True,
            "gitter_room": ""
        }
        prefix = "sidecar_gitter"
        fields = ["show_sidecar",
                  "show_on_all_pages",
                  "gitter_room"]
        for item in fields:
            try:
                _data[item] = self.get_registry_entry(
                    "%s.%s" % (prefix,item)
                )
            except InvalidParameterError:
                pass
        return _data

    def get_registry_entry(self,entry):
        _entry = None
        try:
            _entry = api.portal.get_registry_record(entry)
        except ComponentLookupError:
            pass
        return _entry

    def is_front_page(self):
        """
        Check if the viewlet is on a front page.
        Handle canonical paths correctly.
        based on docs: 
        http://docs.plone.org/develop/plone/serving/traversing.html#checking-if-an-item-is-the-site-front-page
        """
        # Get path with "Default content item" wrapping applied
        context_helper = getMultiAdapter((self.context, self.request), 
                                                 name="plone_context_state")
        canonical = context_helper.canonical_object()
        path = canonical.absolute_url_path()
        return INavigationRoot.providedBy(canonical)