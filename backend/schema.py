import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from models import ToDo, db
from utils import format_response

class ToDoType(SQLAlchemyObjectType):
    class Meta:
        model = ToDo

class Query(graphene.ObjectType):
    get_todos = graphene.List(ToDoType)

    def resolve_get_todos(self, info):
        return ToDo.query.all()

class CreateToDo(graphene.Mutation):
    todo = graphene.Field(ToDoType)

    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String(required=True)
        time = graphene.String(required=True)
        image_url = graphene.String()

    def mutate(self, info, title, description, time, image_url=None):
        todo = ToDo(title=title, description=description, time=time, image_url=image_url)
        db.session.add(todo)
        db.session.commit()
        return format_response(todo)

class Mutation(graphene.ObjectType):
    create_todo = CreateToDo.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
