# class Dad:
#     basketball=6
# class Son(Dad):
#     dance=1
#     basketball=9
#     def isdance(self):
#         return f"yes i dance {self.dance} no of times"
# class Grandson(Son):
#     dance=6
#     guitar=1
#     def isdance(self):
#         return f"jackson yeah yes i dance very awesomely {self.dance} no of times"

# darry=Dad()
# larry=Son()
# harry=Grandson()
# print(harry.isdance())
# print(harry.basketball)
# print(harry.guitar)
# print(darry.guitar)

# electronic device
# pocket gadget
# phone

class ElectronicDevice:
    num=100
    def get_nos(self):
        return f"the no electronic devices are {self.num}"
class PocketGadget(ElectronicDevice):
    num=50
    quality=20
    def get_nos(self):
        return f"the no of pocket gadgets are {self.num}"
class Phone(PocketGadget):
    num=10
    quality=50
    def get_nos(self):
        return f"the no of phones are {self.num}"
apple=Phone()
micromax=PocketGadget()
sony=ElectronicDevice()
print(apple.quality,apple.get_nos())
print(micromax.quality,micromax.get_nos())
print(sony.get_nos())