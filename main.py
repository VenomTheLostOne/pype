from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
import hashlib
import random as r
import settings as s
import artwork as a





#defining the app of it's name
app = Flask(__name__)





#These are temp variables that are used in the upload function
path = ''
file_nname = ''





#this is the upload function prodably the most important function in the code and the hardest one to code
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file:
        new_FILE = hashlib.sha3_512((file.filename).encode())
        new_FILE = new_FILE.hexdigest()
        new_random_number = r.randint(999, 999999999)
        new_random_number = str(new_random_number)
        new_FILE = new_FILE + new_random_number
        path = os.path.join(s.upload_directory, new_FILE)
        os.mkdir(path)
        file_nname = file.filename
        temp_upload_directory = s.upload_directory
        temp_upload_directory = s.upload_directory + new_FILE
        path = new_FILE
        file.save(os.path.join(temp_upload_directory, file.filename))
        download_linnk = s.domain + '/download/' + path + '/' + file_nname
        return render_template('upload.html', file_name1=file.filename, download_link=download_linnk, static_loc=s.static_directory)
    else:
        return 'No file selected.' #if the user does not select a file this will be shown also custom error pages are coming soon





#17 april not working might be due to python is going nuts, here the user can download the file from the server if the share code is correct
@app.route('/download/<code>/<filename>')
def download(code, filename):
    return render_template('portal.html', static_loc=s.static_directory, value=filename, value1 =code)





#Here the use can upload the file to the server the above was the backend of the upload function this is the like front end of the upload function
@app.route('/')
def index():
    return render_template('index.html', static_loc=s.static_directory)





#Beta function whihc i was too lazy to code so if you go to /remove you will be redirected to the link in settings.py
@app.route('/remove')
def remove():
    return redirect(s.beta_redirect)





#This is the function is what is used to turn on the server, it's perpous is to run the server and provice and good experien ce
def server_run():
    if __name__ == '__main__':
        service = a.artwork()
        service.print()
        files_to_check = ['settings.py', 'artwork.py', 'index.html', 'upload.html', 'portal.html']
        pype_share_dir = s.pype_share_dir
        templates_dir = s.templates_dir
        def check_file(file_path):
            if os.path.exists(file_path):
                print(f"{file_path} exists. Check Passed")
            else:
                exit(f"{file_path} does not exist. Check Failed Please make sure you have all the files in the right place")
                return f"{file_path} does not exist. Check Failed Please make sure you have all the files in the right place"
        for file_name in files_to_check:
            if file_name in ['settings.py', 'artwork.py']:
                file_path = os.path.join(pype_share_dir, file_name)
                check_file(file_path)
            elif file_name in ['index.html', 'upload.html', 'portal.html']:
                file_path = os.path.join(templates_dir, file_name)
                check_file(file_path)
        print("All Checks Passed")
        print("Starting Server")
        print(f'Server is running on {s.domain} on port {s.port}')
        print('------------------------------------------------------------')
        app.run(debug=True, host=s.host, port=s.port)
        
        
        
        
        
#calling the server_run function
server_run()













































#




































































































































































































































































































































































































































###





















































# woo if you reached here you are amazing because there is nothing here :D
# all the code is written and finished above this line :D like way above this like ;D