#get set string
class Solution:
    string='helloworld'
    def set_string(self):
        self.string=input("Enter the string:")
    def get_string(self):
        print("Uppercase:")
        print(self.string.upper())
        print("Lowercase:")
        print(self.string.lower())
s1=Solution()
s1.set_string()
s1.get_string()