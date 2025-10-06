from jet.dashboard import modules
from jet.dashboard.dashboard import Dashboard
from screen.models import Work, Work_details, Art

class CustomDashboard(Dashboard):
    columns = 2

    def init_with_context(self, context):
        # Fetch data
        works = Work.objects.all()[:4]  # first 4 rows
        work_details = Work_details.objects.all()[:4]
        arts = Art.objects.all()[:4]

        # Custom HTML module for Works
        self.children.append(
            modules.LinkList(
                title='Works',
                children=[
                    {'title': f"{w.id} - {w.name}", 'url': f"/admin/screen/work/{w.id}/change/"}
                    for w in works
                ],
                column=1,
            )
        )

        # Work Details
        self.children.append(
            modules.LinkList(
                title='Work Details',
                children=[
                    {'title': f"{wd.id} - {wd.work.name}", 'url': f"/admin/screen/work_details/{wd.id}/change/"}
                    for wd in work_details
                ],
                column=1,
            )
        )

        # Art
        self.children.append(
            modules.LinkList(
                title='Art',
                children=[
                    {'title': f"{a.id} - {a.description[:20] if a.description else 'No description'}",
                     'url': f"/admin/screen/art/{a.id}/change/"}
                    for a in arts
                ],
                column=2,
            )
        )
