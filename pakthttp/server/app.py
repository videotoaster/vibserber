from functools import wraps

class PakTTP:

    routes = {}

    @staticmethod
    def route(path, methods):
        print("route")
        def inner(func):
            print("inner")
            @wraps(func)
            def wrapper_route(*args, **kwargs):
                print("wrapper")
                self.routes[str(path)] = {
                    "path": path,
                    "methods": methods,
                    "function": func
                }
                func()
        return inner
        return wrapper_route


bob = PakTTP()

@bob.route("/", methods=["POST"])
def root():
    return b"fuck"

print(bob.routes)