from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from employee.models import Employee
from team.models import Team
from team.serializers import TeamSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    @action(detail=True, methods=["POST"])
    def add_members(self, request, pk=None):
        team = self.get_object()
        member_ids = request.data.get("member_ids", [])

        members = Employee.objects.filter(id__in=member_ids)

        for member in members:
            team.members.add(member)

        return Response({"message": "Members added successfully"})

    @action(detail=True, methods=["POST"])
    def delete_members(self, request, pk=None):
        team = self.get_object()
        member_ids = request.data.get("member_ids", [])

        members = Employee.objects.filter(id__in=member_ids)

        for member in members:
            team.members.remove(member)

        return Response({"message": "Members deleted successfully"})
