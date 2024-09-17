from PIL import Image as PILImage
import imghdr
import os
import imagesize
import sys

################## Image Definition ######################

convertFormats = ['png', 'jpeg', 'bmp']

class Image:
    def __init__(self):
        self.filePath = None
        self.newPath = None
        self.fileType = None
        self.newType = None
        self.width = None
        self.height = None

    def canConvert(self):
        if self.newType.lower() not in convertFormats:
            print(f"Cannot convert {self.fileType} to {self.newType}")
            return False
        else:
            print(f"Can convert {self.fileType} to {self.newType}")
            return True

    def replaceExtension(self):
        base, _ = os.path.splitext(self.filePath)
        new_file_path = f"{base}.{self.newType}"
        return new_file_path


    def fetchData(self):
        if imghdr.what(self.filePath) != None:
            self.fileType = imghdr.what(self.filePath)
            self.width, self.height = imagesize.get(self.filePath)
            print(f"The file is a valid ({self.fileType}) file.")
            self.toString()
        else:
            self.fileType = imghdr.what(self.filePath)
            print(f"The file is invalid.")
            sys.exit()

    def toString(self):
        print(f"""Image File Details:
              Path: {self.filePath}
              isType: {self.fileType}
              width: {self.width}
              height: {self.height}\n""")



################## Image Input ######################

userImg = Image()
userImg.filePath = input("Enter the path to an image: ")

if not os.path.isfile(userImg.filePath):
    print("The file either does not exist, or is not a PNG file.")
    sys.exit()

userImg.fetchData()
print("What do you want to convert it to?\nSupported Formats: ", convertFormats)
userImg.newType = input("\n ->")

if not userImg.canConvert():
    print("Cannot Convert.")
    sys.exit()

if userImg.fileType == userImg.newType:
    print("Same type as input, no need to convert image.")
    sys.exit()


################## Image Conversion ######################


try:
    with PILImage.open(userImg.filePath) as userImage:
        match userImg.newType:
            case 'jpeg':
                if userImage.mode in ('RGBA', 'LA', 'P'):  # Check for modes that require conversion
                    userImage = userImage.convert('RGB')  # Convert to RGB for JPEG
                userImage.save(userImg.replaceExtension(), format=userImg.newType)
                print("Converted image to JPEG and saved output.")
            case 'png':
                userImage.save(userImg.replaceExtension(), format=userImg.newType)
                print("Converted image to PNG and saved output.")
            case 'bmp':
                userImage.save(userImg.replaceExtension(), format=userImg.newType)
                print("Converted image to BMP and saved output.")
            case _:
                print("Unsupported format.")
                sys.exit()
except Exception as e:
    print(f"An error occurred: {e}")
    sys.exit()