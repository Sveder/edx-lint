"""These are bad uses of _()"""

# pylint: disable=missing-docstring

from string import lower as _, upper as gettext

def welcome(name):
    _("Hello"+"There")
    _(17)
    _("Hi, {0}".format(name))
    # pylint: disable=translation-of-non-string
    _(name)
    # pylint: enable=translation-of-non-string
    gettext("hi, %s" % name)
