from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class SchemaColumnType(models.Model):
    schema_column_type_name = models.CharField(
        unique=True,
        blank=False,
        null=False,
        max_length=64,
        verbose_name=u'schema column type name'
    )

    def __str__(self):
        return self.schema_column_type_name

class SchemaColumn(models.Model):
    column_name = models.CharField(
        blank=False,
        null=False,
        max_length=128,
        verbose_name='schema column name'
    )
    column_type = models.ForeignKey(
        SchemaColumnType,
        null=False,
        verbose_name=u'schema column type',
        on_delete=models.CASCADE
    )
    schema = models.ForeignKey(
        'Schema',
        null=False,
        verbose_name=u'schema column type',
        on_delete=models.CASCADE
    )

class Schema(models.Model):
    schema_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
    schema_name = models.CharField(
        blank=False,
        null=False,
        max_length=256,
        verbose_name=u'schema name'
    )
    schema_column = models.ManyToManyField(
        SchemaColumnType,
        verbose_name=u'column',
        through='SchemaColumn'
    )

