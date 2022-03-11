from fastapi import APIRouter,Body,status,Request
import Controller.Googlemap.googlemap as gmap

router = APIRouter(
        prefix="/time/api",
        tags=["googlemaps"],
        responses={404: {"description": "Notfound"}}
    )

@router.post('/searchmap')
async def onsearchmap(request:Request,payload: dict= Body(...)):
    response = gmap.onSearchMap(payload['keyword'])
    print(request.client.host+'host')
    return {
        "status":status.HTTP_200_OK,
        "data":response
        }
