from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users that are logged in to only view, upate their own profile 
    except admin who casn view only"""

    def has_object_permission(self, request, view, obj):
        """Checks to see if the user has permission to update the object"""
        if request.method == 'GET':
            if obj.id == request.user.id or request.user.is_staff == True:
                return True
        
        return obj.id == request.user.id

class IsAdminOrReadOnly(permissions.BasePermission):
    """Custom permission to only allow admin users to create, update, or delete news.    """

    def has_permission(self, request, view):
        # Read permissions are allowed to any request,so we'll always allow GET, HEAD, or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Check if the user is an admin for other methods.
        return request.user.id and request.user.is_staff


# class UpdateOwnNews(permissions.BasePermission):
#     """Allows users to view news, accept admin who can update news"""
#     def has_object_permission(self, request, view, obj):
#         """Checks to see if the user has permission to POST, PUT or PATCH object"""
#         if request.method != 'GET' and request.user.is_staff:
#             return True
        
#         if request.method == 'GET':
#             return True
#         return obj.author.id == request.user.id