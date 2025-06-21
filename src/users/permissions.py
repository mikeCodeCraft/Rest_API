from rest_framework import permissions

class IsUserOwnerOrGetAndPostOnly(permissions.BasePermission):
    """
    Custom permission for UserViewSet to only allow users to edit their own user.Otherwise, only GET and POST methods are allowed.
    """

    def has_permission(self, request, view):
        return True
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if not request.user.is_anonymous:
            return request.user == obj
        return False
       
class IsProfileOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission for ProfileViewSet to only allow users to edit their own profile.
    Otherwise, only read-only access is allowed.
    """
    def has_permission(self, request, view):
        return True
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if not request.user.is_anonymous:
            return request.user.profile == obj
        return False