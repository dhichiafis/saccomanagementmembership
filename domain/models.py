from dataclasses import dataclass
@dataclass
class User:
    user_id:int
    username:str 
    password:str
    is_active:str  


@dataclass 
class Member:
    person_id:int 
    member_number:int 
    fullnames:str 
    phonenumber:str 
    emailaddress:str 
