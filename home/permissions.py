from rest_framework import permissions

class IsownerPermission(permissions.BasePermission):
    message="Sorry your are not a owner."
    
    def has_object_permission(self, request, view, obj):
        
        if obj.owner_id == request.user:
            return True

        return False