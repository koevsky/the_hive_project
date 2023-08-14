from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect


class CustomPermissionUserMixin(AccessMixin):

    def dispatch(self, request, group_names, current_user, *args, **kwargs):

        dispatch = super().dispatch(request, group_names, current_user, *args, **kwargs)

        user_group = request.user.groups.values_list('name', flat=True)

        if set(group_names).intersection(user_group):
            return dispatch

        elif request.user.is_superuser:
            return dispatch

        elif request.user == current_user:
            return dispatch

        else:
            return self.handle_no_permission()

    def handle_no_permission(self):

        return redirect('index')



