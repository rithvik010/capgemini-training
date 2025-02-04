from abc import ABC,abstractmethod
class UserAuthentication(ABC):
    @abstractmethod
    def login(self):
        pass  
    @abstractmethod
    def logout(self):
        pass
class GoogleAuth(UserAuthentication):
    def login(self):
        return "Logged in using Google"
    def logout(self):
        return "Logged out from Google"
class FacebookAuth(UserAuthentication):
    def login(self):
        return "Logged  in using Facebook"
    def logout(self):
        return "Logged out from FaceBook"
google_1=GoogleAuth()
print(google_1.login())
print(google_1.logout())
facebook=FacebookAuth()
print(facebook.login())
print(facebook.logout())