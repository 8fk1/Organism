from organism.models import Organism
from pprint import pprint


class Favorite:
    def __init__(self, items=None):
        # お気に入りされている生物
        self.items = items or []
        # インスタンス化後に編集があったかどうかのフラグ、セッションに保存するかどうかの判定用
        self.edited = False

    def as_json(self):
        ret = []
        for item in self.items:
            ret.append({'id': item['organism'].id})
        return ret

    @classmethod
    def from_json(cls, items):
        conv_items = []
        for item in items:
            conv_items.append({
                'organism': Organism.objects.filter(id=item['id']).first()
            })
        return cls(conv_items)

    def add_favorite(self, organism):
        """ お気に入り追加
        """

        self.edited = True
        self.items.insert(0, {
            'organism': organism

        })

    def delete_favorite(self, organism):
        """ カート内から引数 ticket を除外する
        """
        self.edited = True
        filtered_items = []
        for item in self.items:
            if item['organism'] != organism:
                filtered_items.append(item)
        self.items = filtered_items

    def delete_all(self):
        self.edited = True
        self.items = []

        # 'id': organism.id,
        # 'name_ja': organism.name_ja,
        # 'name_en': organism.name_en,
        # 'domain': organism.domain,
        # 'kingdom': organism.kingdom,
        # 'family': organism.family,
        # 'status': organism.status
