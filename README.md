# AirBnB clone - The console

## Description of the project

The AirBnB Clone is a project to build a console where we can create objects through classes starting from the BaseModel to other classes. This creation will be with data in json format. You have to create scripts or use commands to use those classes. We have a generator called file_storage.py where are created the json objects. All the data is stored in a file called file.json and the program requests the creations made.

## description of the command interpreter

The command interpreter or console is a way to connect the user with the program through command lines to different purposals. With this interpreter you can create objects depending the class the user chooses.

## how to start it

To start the command interpreter, you have to download this repository in your computer and open your terminal. Then, you have to type "./console.py".

example command interpreter : ./console.py

example output : (hbnb) 

## how to use it

To use the command interpreter, you have to define what you want to do. Remember, you have the following classes: 

BaseModel

User

City

Amenity

Place

Review

State

## create instance of a class

If you want to create an instance of a specific class, you have to use this:

structure : create --Class--

example command interpreter : create BaseModel

example output : 49faff9a-6318-451f-87b6-910505c55907 

Note : The output will be different when you prove it. The output is the id of the created instance.

## request all the instances

If you want to request all the instances, you have to use this:

structure : all

example command interpreter : all

output : 

[BaseModel] (af9b4cbd-2ce1-4e6e-8259-f578097dd15f) {'id': 'af9b4cbd-2ce1-4e6e-8259-f578097dd15f', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 12, 971521), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 12, 971544)}

[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'id': '38f22813-2753-4d42-b37c-57a17f1e4f88', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848291), 'email': 'airbnb@holbertonshool.com', 'first_name': 'Betty', 'last_name': 'Holberton', 'password': 'root'}

Note : the output will be different when you prove it

## request all the instances of a specific class

If you want to request all the instances of a specific class, you have to use this:

structure : all --Class--

example command interpreter : all BaseModel

output : 

[BaseModel] (af9b4cbd-2ce1-4e6e-8259-f578097dd15f) {'id': 'af9b4cbd-2ce1-4e6e-8259-f578097dd15f', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 12, 971521), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 12, 971544)}

Note : the output will be different when you prove it

## show a specific instance

If you want to show a specific instance, you have to use this:

structure : show --Class-- --id--

example command interpreter : show BaseModel 49faff9a-6318-451f-87b6-910505c55907

output : 

[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}

Note : the output will be different when you prove it

## destroy a specific instance

If you want to destroy a specific instance, you have to use this:

structure : destroy --Class-- --id--

example command interpreter : destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907

output : No output

Note : If you wanna confirm your deletion, use show command

## update a specific instance

If you want to update a specific instance, you have to use this:

structure : update --Class-- --id-- --attribute name-- "--attribute value--"

example command interpreter : update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"

example output : 

[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}

Note : The output will be different when you prove it.

## quit the command interpreter

If you want to quit the console, you have to use this:

structure : quit

example command interpreter : quit

output : guillaume@ubuntu:~/AirBnB$ 

Note : the output will be different when you prove it

## find help about a command interpreter

If you want to get information about a command, you have to use this:

structure : help --Command--

example command interpreter : help quit

output : Quit command to exit the program
