from django.shortcuts import redirect


def isOwner(model):
    def decorator(function):
        def wrapper(*args, **kwargs):
            id = kwargs.get("id")
            author = args[0].user
            author = model.objects.get(id=id).author
            if author == author:
                return function(*args, **kwargs)
            return redirect("index")

        return wrapper

    return decorator
