import graphene
from graphene_django import DjangoObjectType,DjangoListField
# from .models import Books
from .model import collection


# class BooksType(DjangoObjectType):
#     class Meta:
#         model = Books
#         fields = ("id", "title", "excerpt")

class dataset(graphene.ObjectType):
    label = graphene.String()
    quantity = graphene.Int()
    image_url = graphene.List(graphene.String)


class Query(graphene.ObjectType):

    allResult=graphene.List(dataset)

    image_urls=graphene.List(dataset,label=graphene.String())

    def resolve_image_urls(root,info,label):
        datas = collection.find_one({"Label":label})
        result = []
        obj=dataset(
        label=datas['Label'],
        quantity=datas['Quantity'],
        image_url=datas['image_url']
        )
        result.append(obj)
        return result



    def resolve_allResult(root,info):
        
        datas = collection.find()
        result = []
        for data in datas:
            obj = dataset(
                label=data['Label'],
                quantity=data['Quantity'],
                image_url=data['image_url']
            )
            result.append(obj)
        return result


schema = graphene.Schema(query=Query)