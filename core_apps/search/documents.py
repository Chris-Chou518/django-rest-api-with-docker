from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from core_apps.articles.models import Article


@registry.register_document
class ArticleDocument(Document):
    title = fields.TextField(attr="title")
    description = fields.TextField(attr="description")
    body = fields.TextField(attr="body")
    author_first_name = fields.TextField()
    author_last_name = fields.TextField()
    tags = fields.KeywordField()

    slug = fields.KeywordField(attr="slug")
    author = fields.TextField()  # 整合的欄位，展示完整的作者名稱

    class Index:
        name = "articles"
        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = Article
        fields = ["created_at"]

    def prepare_author(self, instance):
        # 合併作者的名字和姓氏作為 author 的字串，避免傳遞 User 物件
        if instance.author:
            return f"{instance.author.first_name} {instance.author.last_name}"
        return ""

    def prepare_author_first_name(self, instance):
        return instance.author.first_name

    def prepare_author_last_name(self, instance):
        return instance.author.last_name

    def prepare_tags(self, instance):
        return [tag.name for tag in instance.tags.all()]
