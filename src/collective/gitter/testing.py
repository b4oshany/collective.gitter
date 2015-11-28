# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import collective.gitter


class CollectiveGitterLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=collective.gitter)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.gitter:default')


COLLECTIVE_GITTER_FIXTURE = CollectiveGitterLayer()


COLLECTIVE_GITTER_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_GITTER_FIXTURE,),
    name='CollectiveGitterLayer:IntegrationTesting'
)


COLLECTIVE_GITTER_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_GITTER_FIXTURE,),
    name='CollectiveGitterLayer:FunctionalTesting'
)


COLLECTIVE_GITTER_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_GITTER_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='CollectiveGitterLayer:AcceptanceTesting'
)
