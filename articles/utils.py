from django.utils.text import slugify


def slugify_instance_title(instance, save=False):
    slug = slugify(instance.title)
    Class = instance.__class__
    qs = Class.objects.filter(slug=slug).exclude(id=instance.id)
    if qs.exists():
        slug = f"{slug}-{instance.id}"
    instance.slug = slug
    if save:
        instance.save()
    return instance
