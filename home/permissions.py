from rest_framework import permissions

class IsownerPermission(permissions.DjangoModelPermissions):
    def has_object_permission(self, request, view, obj):
        
        if obj.owner_id == request.user.id:
            return True

        return False