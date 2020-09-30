print("__file__ = {0:<35} | __name__ = {1:<20} | __package__ = {2:<20}".format(__file__, __name__, str(__package__)))
if __package__ == None:
    from app import app
else:
    from .app import app #pylint: disable=relative-beyond-top-level

if __name__ == '__main__':
    ret = app.run()