
class Login():
    
    def __init__(self,x):
        
        self.x = x
        
    def User(self,id):
        
        UserList = [['bb@yahoo.com','12345'],['00@0.com','000000'],['khqt001','qq123456'],['khqt001@gmail.com','qq123456']]

        if id ==0:
            UserID  = UserList[0][0]
            UserPW =  UserList[0][1]
        if id ==1:
            UserID =  UserList[1][0]
            UserPW =  UserList[1][1]
        if id ==2:
            UserID =  UserList[2][0]
            UserPW =  UserList[2][1]
        if id ==3:
            UserID =  UserList[3][0]
            UserPW =  UserList[3][1]
            
        return UserID,UserPW
                       
    def input(self):
        
        name = input("Click Here & Choice User:  (0).Admin  (1).User (2).Google (3).Facebook")

        return name
    


