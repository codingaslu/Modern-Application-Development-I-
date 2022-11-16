from flask_restful import Api, Resource, reqparse , fields, marshal_with,abort
from models import User as user_model, db

api = Api() 

user_req = reqparse.RequestParser() #this requestparser will parse the request and then create dictionary like this
user_req.add_argument("username",type=str, help="username is a string", required=True)#add_arguement create a key with username and check whether it can converted into a string otherwise it will print the help
user_req.add_argument("email",type=str, help="email is a string") 

#user_req={
#    'username':'narendra'
#    'email':'narendra@gmail'    
#}   

user_field ={
    'id':fields.Integer,
    'username':fields.String,
    'email': fields.String, 
    'url' : fields.Url(absolute=True) #it will send url of the resource
}
   
class User(Resource):  #when the user will send a get request for the user resources this method will trigger and whatever this method will return will be return to the user
    @marshal_with(user_field)
    def get(self, id=None): #get is to retreive the resource
        user = user_model.query.get(id)
        if not user:
            abort(404, message="user does not exist")   #abort used to throw http exception
        else:  
            return user
#next step is you need to register User resource.That means you need to map your resource with a url(end point).So that when the client wants to get the user resource,it will communicate using that url.
    
    
    @marshal_with(user_field)#it is asking the program to marshal the return statement of this post methode to use this user_field dictionary inorder to convert the user object into a JSON serailiazabel oblect.
    def post(self): #post is to create the resourse
        data= user_req.parse_args() #using parse_args you are accessing that dictionary and storing it in the data and returning the data back
        user = user_model(username=data["username"],email=data["email"])
        db.session.add(user)
        db.session.commit()
        return user,400,{'Auther-Name':'Narendra'} #here we can manipulate the statuscode 
    
    def put(self): #put is used to update the resource
        return "hello from the put"
    
    def delete(self): #delete is used to delete the resource
        return "hello from delete"
    
#api.add_resource(User,'/api/users')#first arguenment is Resource name and second is the end point.Whenever the client will send a get requiest to this end point. the above method will be triggered.
api.add_resource(User,"/api/users","/api/users/<int:id>")#we can also give two paths



#Note :- In post method we cant pass arguent as path,So we are getting the values using request parse and accepting it using add arguent.then parse_arge used to bind it with the function.
#Note :- style of output is fields and marshal_with is used for serialization and connect with the function