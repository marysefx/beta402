"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from polydag.models import Node, CycleError

class SimpleTest(TestCase):
    def testAttach(self):
        #parent -> child1 -> child2
        #   |-------------------^
        parent = Node.objects.create(name="root")
        child1 = Node.objects.create(name="child1")
        child2 = Node.objects.create(name="child2")
        self.assertTrue(parent.add_child(child1))
        self.assertTrue(child2.add_parent(parent))
        self.assertTrue(child1.add_child(child2))
        self.assertRaises(CycleError, child2.add_child, (child1))

        self.assertIn(child1, parent.children())
        self.assertIn(parent, child1.parents())

        self.assertIn(child2, parent.children())
        self.assertIn(parent, child2.parents())

        self.assertIn(child2, child1.children())
        self.assertIn(child1, child2.parents())

        self.assertNotIn(child1, child2.children())
        self.assertNotIn(child2, child1.parents())

    def testClassBasename(self):
        self.assertEqual('Node', Node().classBasename())
        class Carapils(Node):
            pass
        self.assertEqual('Carapils', Carapils().classBasename())

