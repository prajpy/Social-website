from django.urls import path
from .views import (my_profile_view,
                    invites_received_view,
                    profile_list_view,
                    invite_profiles_list_view,
                    ProfileListView,
                    ProfileDetailView,
                    send_invataions,
                    remove_from_friends,
                    accept_invatations,
                    reject_invatations,
                    )

app_name='profiles'

urlpatterns = [
    path('', ProfileListView.as_view(),name='all_profiles-view'),
    path('myprofile/', my_profile_view, name='my-profile-view'),
    path('my-invites/', invites_received_view,name='my-invites-view'),
    path('to-invite/', invite_profiles_list_view,name='invite_profiles-view'),
    path('send-invite/', send_invataions,name='send-invite'),
    path('remove-friend/', remove_from_friends,name='remove-friend'),
    path('<slug>/', ProfileDetailView.as_view(),name='profile-detail-view'),
    path('my-invites/accept/', accept_invatations,name='accept-invite'),
    path('my-invites/reject/', reject_invatations,name='reject-invite'),
]