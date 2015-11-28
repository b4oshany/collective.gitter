# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from collective.gitter.testing import COLLECTIVE_GITTER_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that collective.gitter is properly installed."""

    layer = COLLECTIVE_GITTER_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.gitter is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'collective.gitter'))

    def test_browserlayer(self):
        """Test that ICollectiveGitterLayer is registered."""
        from collective.gitter.interfaces import (
            ICollectiveGitterLayer)
        from plone.browserlayer import utils
        self.assertIn(ICollectiveGitterLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_GITTER_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['collective.gitter'])

    def test_product_uninstalled(self):
        """Test if collective.gitter is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'collective.gitter'))

    def test_browserlayer_removed(self):
        """Test that ICollectiveGitterLayer is removed."""
        from collective.gitter.interfaces import ICollectiveGitterLayer
        from plone.browserlayer import utils
        self.assertNotIn(ICollectiveGitterLayer, utils.registered_layers())
