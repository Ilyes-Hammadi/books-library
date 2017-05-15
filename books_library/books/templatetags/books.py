from django import template

register = template.Library()




@register.filter('isliked')
def isliked(book, user):
    return user in book.likes.all()

@register.filter('viewed')
def viewed(books):
    return len(books.filter(read=True))

@register.filter('hasTwitter')
def hasTwitter(user):
    return user.history.social_data.filter(provider='twitter')

@register.filter('isBookmarked')
def isBookmarked(book, user):
    return user.history.books_action.filter(book=book, bookmarked=True).exists()
