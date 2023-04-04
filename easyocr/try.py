# from source.easyocr import easyocr
import easyocr

reader = easyocr.Reader(['en']) # need to run only once to load model into memory
result = reader.readtext('/home/aharnish/Documents/AhmedabadUniversity/ml/InsightScan-ML/easyocr/test/Similarity/F4.jpeg')




# result = reader.readtext('/home/aharnish/Documents/AhmedabadUniversity/ml/InsightScan-ML/easyocr/test/test4-lays.jpeg')
# result = reader.readtext('/home/aharnish/Documents/AhmedabadUniversity/ml/prj/easyocr/test/test3-cropped.jpg')
# result = reader.readtext('test/test1.png')

print(result)

for i in result:
    print(i[1])
