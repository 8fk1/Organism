from click import pass_context
from django.test import TestCase
from django.urls import reverse

from organism import models
from organism import testing
from pprint import pprint


class TestOrganismList(TestCase):
    def _getTarget(self):
        return reverse('organism:list')

    def test_get(self):
        d1 = testing.factory_domain(name="テストドメイン`")
        k1 = testing.factory_kingdom(name="テスト界")
        o1 = testing.factory_organism(domain=d1, kingdom=k1)
        res = self.client.get(self._getTarget())
        self.assertTemplateUsed(res, 'organism/list.html')
        self.assertEqual(len(res.context['organisms']), 1)
        self.assertEqual(res.context['organisms'][0], o1)

    def test_get_paginate(self):
        organisms = []
        for _ in range(30):
            o = testing.factory_organism()
            organisms.append(o)
        pprint(organisms[:20])
        res = self.client.get(self._getTarget())
        self.assertTemplateUsed(res, 'organism/list.html')
        self.assertEqual(len(res.context['organisms']), 21)
        self.assertEqual(list(res.context['organisms']), organisms[:20])

    def test_get_paginate_invalid_param(self):
        o1 = testing.factory_organism()
        o2 = testing.factory_organism()
        res = self.client.get(self._getTarget(), data={'page': 'invalid_page'})
        self.assertTemplateUsed(res, 'organism/list.html')
        self.assertEqual(len(res.context['organisms']), 2)
        self.assertEqual(res.context['organisms'][0], o2)
        self.assertEqual(res.context['organisms'][1], o1)


    def test_get_paginate_too_big_page(self):
        o1 = testing.factory_organism()
        res = self.client.get(self._getTarget(), data={'page': '999999'})
        self.assertTemplateUsed(res, 'organism/list.html')
        self.assertEqual(len(res.context['organisms']), 1)
        self.assertEqual(res.context['organisms'][0], o1)

class TestOrganismDetail(TestCase):
    pass
