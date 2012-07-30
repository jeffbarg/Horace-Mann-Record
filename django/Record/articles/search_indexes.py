import datetime
from haystack import indexes
from articles.models import Article


class NoteIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    date_published = indexes.DateTimeField(model_attr='date_published')

    def get_model(self):
        return Article

    def index_queryset(self):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(date_published__lte=datetime.datetime.now())