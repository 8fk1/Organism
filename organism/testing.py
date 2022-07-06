from . import models


def factory_domain(**kwargs):
    """ テスト用のDomainのデータを作成
    """
    d = {
        'name': 'テストドメイン'
    }
    d.update(kwargs)
    return models.Domain.objects.create(**d)


def factory_kingdom(**kwargs):
    """ テスト用のKingdomのデータを作成
    """
    d = {
        'name': 'テスト界'
    }
    d.update(kwargs)
    return models.Kingdom.objects.create(**d)


def factory_family(**kwargs):
    """ テスト用のFamilyのデータを作成
    """
    d = {
        'name': 'テスト科'
    }
    d.update(kwargs)
    return models.Family.objects.create(**d)


def factory_organism(**kwargs):
    """ テスト用のOrganismのデータを作成
    """
    d = {
        'name_ja': 'テスト生物',
        'name_en': 'test_organism',
        'domain': factory_domain(),
        'kingdom': factory_kingdom(),
        'family': factory_family(),
    }

    d.update(kwargs)
    return models.Organism.objects.create(**d)
