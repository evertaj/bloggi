from optparse import make_option
from django.core.management.base import AppCommand


class Command(AppCommand):
    option_list = AppCommand.option_list + (
        make_option('--count', action='store_true', dest='count', default=False,
                    help='Add object count information'),
        make_option('--items', action='store_true', dest='items', default=False,
                    help='Show articles and comments'),
    )
    help = 'Prints model names for given application and optional object count.'
    args = '[appname ...]'

    requires_model_validation = True

    def handle_app_config(self, app, **options):
        models = app.get_models()
        objects = []
        comments = []
        if app.name == 'Bloggi' and options["items"]:
            for model in models:
                if model.__name__ == 'Article':
                    objects = model.objects.all()
                elif model.__name__ == 'Comment':
                    comments = model
                else:
                    print('No articles')
            for item in objects:
                print("Comments for article: <%s>" % item)
                for i in comments.objects.filter(article = item.id):
                    print("%s:" % i.user, '"%s"' % i.text)

        else:
            for model in models:
                objects.append("%s" % model.__name__ + (options["count"] and " - %s objects"
                                                        % model._default_manager.count() or ""))
            print("\n".join(objects))
