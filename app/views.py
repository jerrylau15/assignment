from flask_appbuilder import ModelView
from flask_appbuilder.fieldwidgets import Select2Widget
from flask_appbuilder.models.sqla.interface import SQLAInterface
from .models import Employee, Department, Function, EmployeeHistory, Benefit, MenuItem, MenuCategory, News, \
    NewsCategory, Contact, ContactGroup, EventGroup, Movie
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from app import appbuilder, db
from flask_appbuilder.baseviews import expose, BaseView
from flask_appbuilder.widgets import ListThumbnail


def department_query():
    return db.session.query(Department)


class EmployeeHistoryView(ModelView):
    datamodel = SQLAInterface(EmployeeHistory)
    # base_permissions = ['can_add', 'can_show']
    list_columns = ['department', 'begin_date', 'end_date']


class EmployeeView(ModelView):
    datamodel = SQLAInterface(Employee)

    list_columns = ['full_name', 'department.name', 'employee_number']
    edit_form_extra_fields = {'department': QuerySelectField('Department',
                                                             query_factory=department_query,
                                                             widget=Select2Widget(extra_classes="readonly"))}

    related_views = [EmployeeHistoryView]
    show_template = 'appbuilder/general/model/show_cascade.html'


class FunctionView(ModelView):
    datamodel = SQLAInterface(Function)
    related_views = [EmployeeView]


class DepartmentView(ModelView):
    datamodel = SQLAInterface(Department)
    related_views = [EmployeeView]


class BenefitView(ModelView):
    datamodel = SQLAInterface(Benefit)
    add_columns = ['name']
    edit_columns = ['name']
    show_columns = ['name']
    list_columns = ['name']


class MenuItemView(ModelView):
    datamodel = SQLAInterface(MenuItem)
    list_columns = ['id', 'name', 'link', 'menu_category_id']


class MenuCategoryView(ModelView):
    datamodel = SQLAInterface(MenuCategory)
    list_columns = ['id', 'name']


class NewsView(ModelView):
    datamodel = SQLAInterface(News)
    list_columns = ['id', 'title', 'content', 'date', 'newsCat_id']


class NewsCategoryView(ModelView):
    datamodel = SQLAInterface(NewsCategory)
    list_columns = ['id', 'name']


class NewsPageView(BaseView):
    default_view = 'local_news'

    @expose('/local_news/')
    def local_news(self):
        param1 = 'Local News'
        self.update_redirect()
        return self.render_template('news.html', param1=param1)

    @expose('/global_news/')
    def global_news(self):
        param1 = 'Global News'
        self.update_redirect()
        return self.render_template('news2.html', param1=param1)


class CinemasPageView(BaseView):
    default_view = 'MOViE_MOViE_Cityplaza'

    @expose('/MOViE_MOViE_Cityplaza/')
    def MOViE_MOViE_Cityplaza(self):
        param1 = 'MOViE MOViE Cityplaza'
        self.update_redirect()
        return self.render_template('mapsMMC.html', param1=param1)

    @expose('/PALACE_ifc/')
    def PALACE_ifc(self):
        param1 = 'PALACE ifc'
        self.update_redirect()
        return self.render_template('mapsifc.html', param1=param1)

    @expose('/CYBERPORT/')
    def CYBERPORT(self):
        param1 = 'CYBERPORT'
        self.update_redirect()
        return self.render_template('mapsCP.html', param1=param1)

    @expose('/PREMIERE_ELEMENTS/')
    def PREMIERE_ELEMENTS(self):
        param1 = 'PREMIERE ELEMENTS'
        self.update_redirect()
        return self.render_template('mapsPE.html', param1=param1)

    @expose('/HOLLYWOOD/')
    def HOLLYWOOD(self):
        param1 = 'HOLLYWOOD'
        self.update_redirect()
        return self.render_template('mapsHW.html', param1=param1)

    @expose('/The_ONE/')
    def The_ONE(self):
        param1 = 'The ONE'
        self.update_redirect()
        return self.render_template('mapsTO.html', param1=param1)

    @expose('/CINEMATHEQUE/')
    def CINEMATHEQUE(self):
        param1 = 'CINEMATHEQUE'
        self.update_redirect()
        return self.render_template('mapsCT.html', param1=param1)

    @expose('/MONGKOK/')
    def MONGKOK(self):
        param1 = 'MONGKOK'
        self.update_redirect()
        return self.render_template('mapsMK.html', param1=param1)

    @expose('/PALACE_apm/')
    def PALACE_apm(self):
        param1 = 'PALACE apm'
        self.update_redirect()
        return self.render_template('mapsapm.html', param1=param1)

    @expose('/MY_CINEMA_YOHO_MALL/')
    def MY_CINEMA_YOHO_MALL(self):
        param1 = 'MY CINEMA YOHO MALL'
        self.update_redirect()
        return self.render_template('mapsMCYM.html', param1=param1)

    @expose('/KWAI_FONG/')
    def KWAI_FONG(self):
        param1 = 'KWAI FONG'
        self.update_redirect()
        return self.render_template('mapsKF.html', param1=param1)

    @expose('/TSUEN_WAN/')
    def TSUEN_WAN(self):
        param1 = 'TSUEN WAN'
        self.update_redirect()
        return self.render_template('mapsTW.html', param1=param1)

    @expose('/KINGSWOOD_GINZA/')
    def KINGSWOOD_GINZA(self):
        param1 = 'KINGSWOOD GINZA'
        self.update_redirect()
        return self.render_template('mapsKG.html', param1=param1)


class ContactModelView(ModelView):
    datamodel = SQLAInterface(Contact)
    label_columns = {'name': 'Name', 'contact_group': 'Contact group'}
    list_columns = ['name', 'mobile', 'birthday', 'contact_group']
    show_fieldsets = [
        (
            'Summary',
            {'fields': ['name', 'address', 'contact_group']}
        ),
        (
            'Personal Info',
            {'fields': ['birthday', 'mobile'], 'expanded': False}
        ),
    ]


class GroupModelView(ModelView):
    datamodel = SQLAInterface(ContactGroup)
    related_views = [ContactModelView]


class MovieModelView(ModelView):
    datamodel = SQLAInterface(Movie)
    list_widget = ListThumbnail
    label_columns = {'event_group_id': 'Event', 'photo_img': 'Photo', 'photo_img_thumbnail': 'Photo'}
    list_columns = ['id', 'photo_img', 'name', 'Type', 'rating', 'opening', 'time', 'subtitle', 'synopsis',
                    'cinema', 'Director', 'Cast', ]
    show_columns = ['photo_img', 'name']


class EventGroupModelView(ModelView):
    datamodel = SQLAInterface(EventGroup)
    related_views = [MovieModelView]


db.create_all()

""" Page View """
appbuilder.add_view(NewsPageView, 'Local News', category="News")
appbuilder.add_link("Global News", href="/newspageview/global_news/", category="News")

""" Cinemas Page View """
appbuilder.add_view(CinemasPageView, 'MOViE MOViE Cityplaza', icon="fa fa-map-marker", category="Cinemas",
                    category_icon='fa fa-location-arrow')
appbuilder.add_link("PALACE ifc", icon="fa fa-map-marker", href="/cinemaspageview/PALACE_ifc/", category="Cinemas")
appbuilder.add_link("CYBERPORT", icon="fa fa-map-marker", href="/cinemaspageview/CYBERPORT/", category="Cinemas")
appbuilder.add_link("PREMIERE ELEMENTS", icon="fa fa-map-marker", href="/cinemaspageview/PREMIERE_ELEMENTS/",
                    category="Cinemas")
appbuilder.add_link("HOLLYWOOD", icon="fa fa-map-marker", href="/cinemaspageview/HOLLYWOOD/", category="Cinemas")
appbuilder.add_link("The ONE", icon="fa fa-map-marker", href="/cinemaspageview/The_ONE/", category="Cinemas")
appbuilder.add_link("CINEMATHEQUE", icon="fa fa-map-marker", href="/cinemaspageview/CINEMATHEQUE/",
                    category="Cinemas")
appbuilder.add_link("MONGKOK", icon="fa fa-map-marker", href="/cinemaspageview/MONGKOK/", category="Cinemas")
appbuilder.add_link("PALACE apm", icon="fa fa-map-marker", href="/cinemaspageview/PALACE_apm/", category="Cinemas")
appbuilder.add_link("MY CINEMA YOHO MALL", icon="fa fa-map-marker", href="/cinemaspageview/MY_CINEMA_YOHO_MALL/",
                    category="Cinemas")
appbuilder.add_link("KWAI FONG", icon="fa fa-map-marker", href="/cinemaspageview/KWAI_FONG/", category="Cinemas")
appbuilder.add_link("TSUEN WAN", icon="fa fa-map-marker", href="/cinemaspageview/TSUEN_WAN/", category="Cinemas")
appbuilder.add_link("KINGSWOOD GINZA", icon="fa fa-map-marker", href="/cinemaspageview/KINGSWOOD_GINZA/",
                    category="Cinemas")

""" Custom Views """
appbuilder.add_view(MenuItemView, "MenuItem", icon="fa-folder-open-o", category="Admin",
                    category_icon='fa fa-users')
appbuilder.add_view(MenuCategoryView, "MenuCategory", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(NewsView, "News", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(NewsCategoryView, "NewsCategory", icon="fa-folder-open-o", category="Admin")

""" Contact """
appbuilder.add_view(GroupModelView, "List Groups", icon='fa-address-book-o', category='Contacts',
                    category_icon='fa-envelope')
appbuilder.add_view(ContactModelView, 'List Contacts', icon='fa-address-card-o', category='Contacts')

""" Movie """
appbuilder.add_view(EventGroupModelView, "Event Group", icon='fa fa-film', category='Movie',
                    category_icon='fa fa-film')
appbuilder.add_view(MovieModelView, "Movie list", icon='fa fa-film', category='Movie')
