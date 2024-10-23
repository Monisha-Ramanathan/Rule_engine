
from django.test import TestCase

class RuleEngineTests(TestCase):
    def test_create_rule(self):
        response = self.client.post('/create_rule/', {'rule_string': 'age > 30 AND salary > 50000'})
        self.assertEqual(response.status_code, 200)
