from django.contrib import admin

from .models import (
    Activity,
    Language,
    AssignmentActivity,
    Module,
    SupportMaterial,
    StudentsGroup,
    AssignmentDelivery,
    Project,
)


admin.site.register(Activity)
admin.site.register(Language)
admin.site.register(AssignmentActivity)
admin.site.register(Module)
admin.site.register(SupportMaterial)
admin.site.register(StudentsGroup)
admin.site.register(AssignmentDelivery)
admin.site.register(Project)