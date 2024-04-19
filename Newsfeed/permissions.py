from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users that are logged in to only view, upate their own profile"""

    def has_object_permission(self, request, view, obj):
        """Checks to see if the user has permission to update the object"""
        if request.method == 'GET':
            if obj.id == request.user.id or request.user.is_staff == True:
                return True
        
        return obj.id == request.user.id