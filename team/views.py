from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from team.models import Team
from team.serializers import TeamSerializer
from employee.models import Employee


class TeamList(APIView):
    def get(self, request):
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeamDetail(APIView):
    def get_object(self, pk):
        try:
            return Team.objects.get(pk=pk)
        except Team.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        team = self.get_object(pk)
        serializer = TeamSerializer(team)
        return Response(serializer.data)

    def put(self, request, pk):
        team = self.get_object(pk)
        serializer = TeamSerializer(team, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        team = self.get_object(pk)
        team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TeamAddMembers(APIView):
    def post(self, request, team_id):
        try:
            team = Team.objects.get(pk=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"},
                            status=status.HTTP_404_NOT_FOUND)

        member_ids = request.data.get("member_ids", [])
        employees = Employee.objects.filter(id__in=member_ids)

        # Update the team field for each employee
        for employee in employees:
            employee.team = team
            employee.save()

        # Update the team's members
        team.members.add(*employees)

        return Response({"message": "Members added to the team successfully"})


class TeamDeleteMembers(APIView):
    def post(self, request, team_id):
        try:
            team = Team.objects.get(pk=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"},
                            status=status.HTTP_404_NOT_FOUND)

        member_ids = request.data.get("member_ids", [])

        members = Employee.objects.filter(id__in=member_ids)

        for member in members:
            team.members.remove(member)

        return Response({"message": "Members deleted successfully"})
