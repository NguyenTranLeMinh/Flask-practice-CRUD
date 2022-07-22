# Flask-practice-CRUD

1. Open a terminal in the project root directory and run:
```
python -m venv env
```

2. Then run the command:
```
env\Scripts\activate
```

3. Then install the dependencies:
```
(env) pip install -r requirements.txt
```

4. Finally start the web server:
```
(env) python app.py
```

Web server run at port 5000.

Đoạn code có 3 views và 3 templates. 

Index view để thêm task vào cơ sở dữ liệu và hiển thị các tasks.

Delete view để xóa task.

Update view để chỉnh sửa nội dung task đã có.

main là template chính và nó dược kế thừa bởi index và update templates.
