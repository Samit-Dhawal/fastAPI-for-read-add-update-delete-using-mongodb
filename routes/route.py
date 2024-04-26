from fastapi import APIRouter, Request
# from fastapi.responses import HTMLResponse
# from fastapi.templating import Jinja2Templates
# from config.db import conn
from config.db import collectionName
from schemas.schema import noteEntities
from models.notes import Note
from bson import ObjectId

note = APIRouter()

# Get Request Method
@note.get('/')
async def get_notes():
    notes = noteEntities(collectionName.find())
    return notes


# Post Request Method

@note.post('/')
async def post_notes(note: Note):
    collectionName.insert_one(dict(note))

# Put Request Method

@note.put('/{id}')
async def put_notes(id: str, note: Note):
    collectionName.find_one_and_update({'_id': ObjectId(id)}, {'$set': dict(note)})



# Delete Request Method

@note.delete('/{id}')
async def delete_notes(id: str):
    collectionName.find_one_and_delete({'_id': ObjectId(id)})



















# note = APIRouter()
# templates = Jinja2Templates(directory="templates")

# @note.get("/", response_class=HTMLResponse)
# async def read_notes(request: Request):
#     docs = conn.notes.notes.find({})
#     newDocs = []
#     for doc in docs:
#         title = doc.get('title', 'Title Not Found')
#         desc = doc.get('desc', 'Description Not Found')
#         important = doc.get('important', False)
#         newDocs.append({
#             'id': doc['_id'],
#             'title': title,
#             'desc': desc,
#             'important': important,
#         })

#     return templates.TemplateResponse(
#         request=request, name="index.html", context={'newDocs': newDocs}
#     )

# @note.post('/')
# async def add_note(request: Request):
#     form = await request.form()
#     print('beforeDict: ',form)
#     formDict = dict(form)
#     print('afterDict: ',formDict)
#     important = formDict.get('important',False)
#     formDict['important'] = True if important == 'on' else False
#     insertedNote = conn.notes.notes.insert_one(formDict)
#     return {'Success': True}