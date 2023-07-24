from django import template

register = template.Library()


@register.simple_tag
def like_title(product, user):
    photo_liked = product.like_set.filter(user=user).exists()
    result = 'Like'

    if photo_liked:
        result = 'Dislike'

    return result


@register.filter
def is_liked(product, user):
    photo_liked = product.like_set.filter(user=user).exists()

    if photo_liked:
        return True

    return False
