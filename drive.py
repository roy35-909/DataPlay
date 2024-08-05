
import os
# import django
import json
from packagedrive import *
import requests
def list_folders_and_files(directory, headers, create_course, upload_file, upload_content,base_url):
    """
    List folders and files in the specified directory, create courses and content, and upload files.

    Args:
    directory (str): Path to the directory containing course folders.
    headers (dict): Headers for API authentication.
    create_course (function): Function to create courses.
    upload_file (function): Function to upload files.
    upload_content (function): Function to upload content.

    Returns:
    None
    """

    # Loop through items in the directory
    for item in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, item)):
            # Path to course details file (meta.json)
            course_details_path = os.path.join(directory, item, 'meta.json')

            # Check if course details file exists
            if os.path.exists(course_details_path):
                with open(course_details_path, 'r') as json_file:
                    course_data = json.load(json_file)

                # Prepare payload for creating the course
                course_payload = {
                    'course_order': item[:2],
                    'title': item[2:],
                    'description': course_data.get('desc', ''),
                    'course_price': course_data.get('course_price', ''),
                    'content_price': course_data.get('content_price', ''),
                    'course_price_discounted': course_data.get('course_price_discounted', ''),
                    'content_price_discounted': course_data.get('content_price_discounted', '')
                }

                # Create the course
                course_response = create_course(headers, course_payload,base_url, file_path=os.path.join(directory, item, 'prop.jpeg'))
                print(course_response)
                # List and upload files within the current course folder
                file_ids = []
                for root, _, filenames in os.walk(os.path.join(directory, item)):
                    if 'meta.json' in filenames:
                        filenames.remove('meta.json')
                    for filename in filenames:
                        file_path = os.path.join(root, filename)
                        upload_response = upload_file(file_path,headers,base_url)
                        print(upload_response)
                        file_ids.append(upload_response.get('id'))

                # Loop through subdirectories (chapters) inside the course folder
                for chapter in os.listdir(os.path.join(directory, item)):
                    if os.path.isdir(os.path.join(directory, item, chapter)):
                        # Path to chapter details file (meta.json)
                        chapter_details_path = os.path.join(directory, item, chapter, 'meta.json')

                        # Check if chapter details file exists
                        if os.path.exists(chapter_details_path):
                            with open(chapter_details_path, 'r') as json_file:
                                chapter_data = json.load(json_file)

                            # Prepare payload for uploading content
                            content_payload = {
                                'content_order': '1',
                                'title': chapter,
                                'description': chapter_data.get('desc', ''),
                                'files': file_ids,
                                'course': course_response.get('id', '')
                            }

                            # Upload content
                            res = upload_content(headers, content_payload,base_url, file_path=os.path.join(directory, item, 'meta.json'))
                            print(res)
# Example usage of the function
# Specify the directory path, headers, and the functions for creating courses, uploading files, and uploading content


directory_path = 'C:\\Users\\kc508\\OneDrive\\Desktop\\dataplaycontent'

base_url = "https://api.dataplay.co.in"
url = f"{base_url}/auth/jwt/create/"

payload = json.dumps({
  "email": "kc508275@gmail.com",
  "password": "123456789kc"
})


headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  
}

response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)
# print(response.text,type(response.text))
data_dict = json.loads(response.text)
# print(data_dict['access'])
headers = {
    'Authorization': f"JWT {data_dict['access']}"
}

# # Call the function
list_folders_and_files(directory_path, headers, create_course, upload_file, upload_content,base_url)
