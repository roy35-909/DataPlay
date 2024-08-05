import os
import django
import json
from packagedrive import *
import requests
# Set the Django settings module environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dataplay.settings')
headers = {
    'Authorization': 'JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk3ODIzMjE5LCJqdGkiOiI3ZDczZDRhZGEwNDY0MTFhOGYxZjExOWIyOWFhNTMyMSIsInVzZXJfaWQiOjF9.K3lqf8Se8r6e-7WtLMu0l93vCC3Jx5xtX7AVRAfmiv4',
    'Cookie': 'sessionid=huicdfe9v8uv4he6iclgsjgvkg6onk62'
}
# Initialize Django
django.setup()

from home.models import Course, FileField, CourseContents
from django.core.files import File

# Define the directory path
current_directory = "C:\\Users\\kc508\\OneDrive\\Desktop\\dataplaycontent"

def save_file(file_path, upload_path):
    doc = FileField()
    with open(file_path, 'rb') as doc_file:
        doc.files.save(upload_path, File(doc_file), save=True)
    doc.save()
    return doc
def list_folders_and_files(directory):
    
    
    
    for item in os.listdir(directory):
        print(item)
        if os.path.isdir(os.path.join(directory, item)):
            course_detailes = os.path.join(directory, item,'meta.json')
            with open(course_detailes, 'r') as json_file:
                data = json.load(json_file)
            # print(data)
            payload = {
                'course_order':  item[:2],
                'title': item[2:],
                'description': data['desc'],
                'course_price': data['course_price'],
                'content_price': data['content_price'],
                'course_price_discounted': data['course_price_discounted'],
                'content_price_discounted': data['content_price_discounted']  
            }
           
            
            responsed = create_course( headers, payload, file_path)
            # print(response)
            for i in os.listdir(os.path.join(directory, item)):
                file_id = []
                for root, _, filenames in os.walk(os.path.join(directory, item,i)):
                        # filenames.remove
                        print(filenames,type(filenames))
                        filenames.remove('meta.json') 
                        print(filenames,type(filenames))
                        for filename in filenames:
                            file_path = os.path.join(directory, item,i, filename)
                            print(file_path)
                            upload_response = upload_file(file_path)
                            print(upload_response)
                            file_id.append(upload_response['id'])

                file_path = os.path.join(directory, item,'prop.jpeg')
                if os.path.isdir(os.path.join(directory, item,i)):
                    print(i)
                    chapter_detailes = os.path.join(directory, item,i,'meta.json')
                    with open(chapter_detailes, 'r') as json_file:
                        data = json.load(json_file)
                    # print(response  ,type(response ))
                    payload = {
                        'content_order': '1',
                        'title': i,
                        'description': data['desc'],
                        
                        'files': file_id,
                        'course': responsed['id']                  }

                    response = upload_content( headers, payload, file_path)
          

directory_path = current_directory

if os.path.exists(directory_path):
    print(f"Contents of {directory_path}:")
    list_folders_and_files(directory_path)
else:
    print("The specified directory does not exist.")