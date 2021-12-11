from django import template
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown

from ..models import Post

register = template.Library()

@register.simple_tag
def post_total():
    return Post.published.count()

@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_post = Post.published.order_by('-publish')[:count]
    return {'latest_post': latest_post}

@register.inclusion_tag('blog/post/most_comments.html')
def show_most_comments(count=5):
    most_comments = Post.published.annotate(
        total_comments = Count('comments')
    ).order_by('-total_comments')[:count]
    return {'most_comments': most_comments}

@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))