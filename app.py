from flask import Flask
from flask_restful import Api ,Resource ,abort,reqparse

app=Flask(__name__)
api=Api(app)

def abort_if_todo_doesnt_exists(to_id):
    if to_id not in todos.keys():
        abort(404,message = f"Todo {to_id} doesn't exist.")


todos = {
     1 : {"task": "Write Hello World Program", "summary": "write the code using python."},
     2 : {"task": "Task 2", "summary": "writingt task 2."},
     3 : {"task": "Task 3", "summary": "this is task 3."}
}

task_post_args = reqparse.RequestParser()
task_post_args.add_argument("task" ,type = str , help = "task is required" , required = True)
task_post_args.add_argument("summary" , type = str , help = "summary is required" ,required = True)

task_put_args = reqparse.RequestParser()
task_put_args.add_argument("task" ,type = str , help = "task is required" , required = True)
task_put_args.add_argument("summary" , type = str , help = "summary is required" ,required = True)

task_patch_args = reqparse.RequestParser()
task_patch_args.add_argument("task" ,type = str )
task_patch_args.add_argument("summary" , type = str )



class ToDOList(Resource):
    def get(self):
        return todos 

    def post(self):
        args = task_post_args.parse_args()
        if not todos:
            to_id = 1
        else:
            to_id = max(todos.keys())+1
        todos[to_id] = {"task":args['task'],"summary":args['summary']}
        return todos[to_id],201


class ToDo(Resource):  
    def get(self, to_id):
        abort_if_todo_doesnt_exists(to_id)
        return todos[to_id]

    def put(self , to_id):
        args = task_put_args.parse_args()
        if to_id not in todos:
            todos[to_id] = {"task":args['task'] , "summary" :args['summary']}
            return todos[to_id] , 201
        else:
            todos[to_id] = {"task" : args['task'] , "summary" : args['summary']}
            return todos[to_id] 

    def patch(self, to_id):
        abort_if_todo_doesnt_exists(to_id)
        args = task_patch_args.parse_args() 
        if args['task'] :
            todos[to_id]['task'] = args['task']
        if args['summary']:
            todos[to_id]['summary'] = args['summary']
        return todos[to_id]

    def delete(self,to_id):
        abort_if_todo_doesnt_exists(to_id)
        del todos[to_id]
        return "",204   # not content


api.add_resource(ToDOList,'/todos')
api.add_resource(ToDo,'/todos/<int:to_id>')


