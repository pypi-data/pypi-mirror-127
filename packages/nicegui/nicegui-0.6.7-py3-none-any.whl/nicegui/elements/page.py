import justpy as jp
from typing import Optional
from pygments.formatters import HtmlFormatter
from ..globals import config, page_stack, view_stack

class Page(jp.QuasarPage):

    def __init__(self, route: str, title: Optional[str] = None, favicon: Optional[str] = None):
        """Page

        Creates a new page at the given path.

        :param route: the route of the new page. All paths must start with '/', otherwise an error occurs.
        """
        super().__init__()

        self.delete_flag = False
        self.title = title or config.title
        self.favicon = favicon or config.favicon

        self.tailwind = True  # use Tailwind classes instead of Quasars
        self.css = HtmlFormatter().get_style_defs('.codehilite')
        self.head_html += '''
            <script>
                confirm = () => { setTimeout(location.reload.bind(location), 100); return false; };
            </script>
        '''  # avoid confirmation dialog for reload

        self.view = jp.Div(a=self, classes='q-ma-md column items-start', style='row-gap: 1em')
        self.view.add_page(self)

        jp.Route(route, lambda: self)

    def __enter__(self):
        page_stack.append(self)
        view_stack.append(self.view)
        return self

    def __exit__(self, *_):
        page_stack.pop()
        view_stack.pop()
