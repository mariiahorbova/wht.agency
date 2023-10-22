from django.urls import path

from team.views import TeamAddMembers, TeamDeleteMembers, TeamList, TeamDetail

urlpatterns = [
    path("", TeamList.as_view(), name="team-list"),
    path("<int:pk>/", TeamDetail.as_view(), name="team-detail"),
    path("<int:team_id>/add_members/",
         TeamAddMembers.as_view(), name="add-members"),
    path("<int:team_id>/delete_members/",
         TeamDeleteMembers.as_view(), name="delete-members"),
]
