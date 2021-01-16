from .models import *
from django.db.models import Q
import random
from.serializer import GetLobbyDetailsSerializer
def lobby_creation(request):
    msg = 'Invalid data'
    success = False
    try:
        post_data = request.POST
        # lobbyId = post_data.get('id')
        lobbyName = post_data.get('name')
        lobbyMemberSize = post_data.get('member_size')
        lobbyEntryFee = post_data.get('entry_fee')

        if lobbyName and lobbyMemberSize and lobbyEntryFee:
            # LobbyDetails.objects.filter(id = lobbyId).delete()

            lobby_obj = LobbyDetails()
            lobby_obj.name = lobbyName
            lobby_obj.member_size = lobbyMemberSize
            lobby_obj.entry_fee = lobbyEntryFee
            temp = float(lobbyMemberSize)*float(lobbyEntryFee)*0.05
            lobby_obj.house_charges = format(temp,'.4f')
            lobby_obj.save()
            msg = 'Lobby created successfully'
            success = True
    except Exception as e:
        print(e.args)
    return {'msg':msg,'success':success}

def adding_member(request):
    msg = 'Invalid data'
    success = False
    try:
        # import pdb
        # pdb.set_trace()
        post_data =request.POST
        lobbyId = post_data.get("lobby_id")
        memberName = post_data.get("member_name")
        lobby_obj = LobbyDetails.objects.filter(id = lobbyId)
        if lobby_obj:
            member_obj = LobbyMembers.objects.filter(lobby_id=lobbyId)
            if member_obj:
                if len(member_obj)<lobby_obj[0].member_size:
                    new_member_obj = LobbyMembers()
                    new_member_obj.lobby_id = lobbyId
                    new_member_obj.member_name = memberName
                    new_member_obj.save()
                    msg = 'Member added successfully'
                else:
                    msg = 'Lobby is Full'
        else:
            msg = 'No such lobby exist'

        success = True
    except Exception as e:
        print(e.args)
    return {'msg':msg,'success':success}


def check_winner(request):
    data =''
    msg = 'Invalid data'
    success = False
    try:
        # import pdb
        # pdb.set_trace()
        get_data = request.GET
        lobbyId = get_data.get("lobby_id")
        lobbyName = get_data.get("lobby_name")
        extra_field = Q(id = lobbyId)|Q(name = lobbyName)
        if extra_field:
            lobby_obj = LobbyDetails.objects.filter(extra_field)
            member_obj = LobbyMembers.objects.filter(lobby_id = lobbyId).values('member_name')
            if lobby_obj:
                lobby_obj=lobby_obj[0]
                if not lobby_obj.winner:
                    if member_obj:
                        if member_obj.count() == lobby_obj.member_size:
                            winner = random.choice(member_obj)
                            lobby_obj.winner = winner['member_name']
                            lobby_obj.save()
                            msg = 'Winner Announced'
                            data = winner['member_name'] + ' is the Winner'
                        else:
                            msg = 'Lobby is still not full'
                    else:
                        msg = 'Add members'
                else:
                    msg = 'Winner announced and lobby is closed'
            else:
                msg = 'No such lobby exist'

            success = True

    except Exception as e:
        print(e.args)
    return {'data':data,'msg':msg,'success':success}

def dashboard(request):
    data = []
    msg = 'no data'
    success = False
    try:
        import pdb
        pdb.set_trace()
        lobby_obj = LobbyDetails.objects.all()
        serializer = GetLobbyDetailsSerializer(lobby_obj,many=True)
        data = serializer.data
        msg = 'Data fetched successfully'
        success = True
    except Exception as e:
        print(e.args)
    return {'data':data,'msg':msg, 'success':success}
