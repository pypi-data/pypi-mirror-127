from typing import *
import asyncio
import os.path
from starlette.routing import Route
from ..requests import Request, Response, routing, templates
from ..tools import CSTYLE, get_calling_app, array_from
from .. import config, logger, features


__all__ = [
    'context_loaders',
    'add_context_loader',
    'View',
    'TemplateView',
    'get_view',
    'init_view_public_assets',
    'register'
]


context_loaders: List[Callable] = []


def add_context_loader(f: Callable) -> None:
    context_loaders.append(f)


class View:
    _route_url: str
    _requires: List[str]

    assets_uuid: str = None
    public_statics: str = config.STATICS_URL
    public_css: str = None
    public_js: str = None
    public_media: str = f'{config.STATICS_URL}/media'
    public_fonts: str = f'{config.STATICS_URL}/fonts'

    name: str
    app: str
    route: Union[str, List[str]] = None
    requires: Optional[List[str]] = None

    ctx_loaders: Optional[List[Callable]] = None

    def __init__(self, request: Request):
        self.request: Request = request
        self.ctx: dict = {
            'request': self.request,
            'config': config,
            'features': features.all_features(),
            'assets_uuid': self.assets_uuid,
            'public_statics': self.public_statics,
            'public_css': self.public_css,
            'public_js': self.public_js,
            'public_media': self.public_media,
            'public_fonts': self.public_fonts
        }

    @classmethod
    def append_context_loader(cls, loader: Callable) -> None:
        if cls.ctx_loaders is None:
            cls.ctx_loaders = []
        cls.ctx_loaders.append(loader)

    async def use_context_loaders(self) -> None:
        if not context_loaders:
            return
        loaders: List[Callable] = context_loaders + (self.ctx_loaders or [])
        for f in loaders:
            if asyncio.iscoroutinefunction(f):
                ctx: Optional[dict] = await f(self)
            else:
                ctx: Optional[dict] = f(self)
            if not ctx:
                continue
            self.ctx = {**self.ctx, **ctx}

    @classmethod
    async def endpoint(cls, request: Request) -> Response:
        view: View = cls(request)
        await view.use_context_loaders()
        ctx: Optional[dict] = await view.get_context_data()
        if ctx:
            view.ctx = {**view.ctx, **ctx}
        return await view.render()

    async def get_context_data(self) -> Optional[dict]:
        pass

    async def render(self) -> Response:
        raise NotImplementedError


class TemplateView(View):
    template: str = None

    def get_template_filename(self) -> str:
        template: str = self.template
        if not template:
            raise ValueError("TemplateView.template must be set to the template filename prior to render!")
        if not isinstance(template, str):
            raise TypeError(f"TemplateView.template must be type (str), {type(template)} given instead")
        if not template.startswith('/'):
            template = os.path.join(self.app, template)
        return template

    async def render(self) -> Response:
        template_filename: str = self.get_template_filename()
        return templates.TemplateResponse(template_filename, self.ctx)


registered: Dict[str, Any] = {}


def get_view(name: str) -> ClassVar[View]:
    if name not in registered:
        return None
    return registered[name]


def init_view_public_assets() -> None:
    assets_uuid_fn: str = os.path.join(config.STATICS_ROOT, 'assets.uuid')
    if not os.path.isfile(assets_uuid_fn):
        return
        # raise FileNotFoundError("Cannot find statics assets UUID - probably 'manage.py build' was not ran!")
    assets_uuid: str
    with open(assets_uuid_fn, 'r') as f:
        assets_uuid = f.read().strip()
    if not assets_uuid:
        return
        # raise ValueError("Statics assets UUID is empty - probably 'manage.py build' was not ran!")
    View.assets_uuid = assets_uuid
    View.public_js = f"{config.STATICS_URL}/js/assets.{assets_uuid}.js"
    View.public_css = f"{config.STATICS_URL}/css/assets.{assets_uuid}.css"


def register(cls: ClassVar[View]) -> ClassVar[View]:
    name: str = cls.__name__

    def _make_requires(_scopes: Optional[List[str]]) -> List[str]:
        if not _scopes:
            return []
        return [
            (
                (_scope if '.' in _scope else '.'.join([get_calling_app(), _scope]))
                if _scope not in ('authenticated', 'guest')
                else _scope
            )
            for _scope in array_from(_scopes)
        ]

    def _make_routeurl(_app: str, _path: Optional[Union[str, bool]]) -> Optional[str]:
        if _path is False:
            return None
        if not _path:
            _path = name.lower()
        return routing.abs_url(_path, _app)

    app_name: str = get_calling_app()
    view_name: str = '_'.join([app_name, name])
    requires: Optional[List[str]] = getattr(cls, 'requires', None)

    route_s: Optional[Union[str, List[str]]] = getattr(cls, 'route', None)
    route_urls: Optional[List[str]]
    if not route_s:
        route_urls = None
    else:
        route_urls = [_make_routeurl(app_name, r) for r in array_from(route_s)]

    setattr(cls, '_route_urls', route_urls)
    setattr(cls, '_requires', _make_requires(requires))
    setattr(cls, 'app', app_name)
    setattr(cls, 'name', view_name)

    registered[view_name] = cls
    logger.debug(f"registered view {CSTYLE['green']}{view_name}{CSTYLE['clear']}")

    if route_urls:
        endpoint: Callable = getattr(cls, 'endpoint')
        [routing.append(Route(r, endpoint, methods=['GET'])) for r in route_urls]

    return cls


init_view_public_assets()

