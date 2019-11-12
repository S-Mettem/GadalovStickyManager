from django import template


register = template.Library()


def date_added(value, name='time'):
    return ' %1.2f %s' % (value, name)


register.filter('date_added', date_added)
