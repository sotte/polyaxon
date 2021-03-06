import uuid

from django.conf import settings
from django.core.validators import validate_slug
from django.db import models

from db.models.abstract_jobs import TensorboardJobMixin
from db.models.utils import DescribableModel, DiffModel, TagModel
from libs.blacklist import validate_blacklist_name


class Project(DiffModel, DescribableModel, TagModel, TensorboardJobMixin):
    """A model that represents a set of experiments to solve a specific problem."""
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        null=False)
    name = models.CharField(
        max_length=256,
        validators=[validate_slug, validate_blacklist_name])
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='projects')
    is_public = models.BooleanField(
        default=True,
        help_text='If project is public or private.')

    def __str__(self):
        return self.unique_name

    class Meta:
        app_label = 'db'
        unique_together = (('user', 'name'),)

    @property
    def unique_name(self):
        return '{}.{}'.format(self.user.username, self.name)

    @property
    def has_code(self):
        return hasattr(self, 'repo')

    @property
    def notebook(self):
        return self.notebook_jobs.last()

    @property
    def has_notebook(self):
        notebook = self.notebook
        return notebook and notebook.is_running
