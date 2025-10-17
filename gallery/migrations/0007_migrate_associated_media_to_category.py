from django.db import migrations

def forwards(apps, schema_editor):
    Category = apps.get_model('gallery', 'Category')
    Media = apps.get_model('gallery', 'Media')

    for cat in Category.objects.all():
        assoc_id = getattr(cat, 'associated_media_id', None)
        if assoc_id:
            try:
                m = Media.objects.get(pk=assoc_id)
            except Media.DoesNotExist:
                continue
            if getattr(m, 'category_id', None) != cat.pk:
                m.category_id = cat.pk
                m.save(update_fields=['category'])

def reverse(apps, schema_editor):
    Category = apps.get_model('gallery', 'Category')
    Media = apps.get_model('gallery', 'Media')

    # For each category, find a media that has category == this category
    # and restore Category.associated_media to point at that media (first found).
    # If none found, leave the existing value unchanged.
    for cat in Category.objects.all():
        m = Media.objects.filter(category_id=cat.pk).order_by('pk').first()
        if m:
            # restore the FK on Category to this media
            # use direct assignment to associated_media_id to avoid model-level validation
            if getattr(cat, 'associated_media_id', None) != m.pk:
                cat.associated_media_id = m.pk
                cat.save(update_fields=['associated_media'])


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0006_media_category'),
    ]

    operations = [
        migrations.RunPython(forwards, reverse),
    ]
