# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']  # รับข้อมูล username จากฟอร์ม
        password = request.POST['password']  # รับข้อมูล password จากฟอร์ม
        
        # ตรวจสอบชื่อผู้ใช้และรหัสผ่านจากฐานข้อมูล
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)  # ถ้าผู้ใช้ถูกต้อง ทำการล็อคอิน
            return redirect('index')  # หลังจากล็อคอินสำเร็จ ไปที่หน้า index
        else:
            # แจ้งเตือนหากข้อมูลไม่ถูกต้อง
            messages.error(request, 'Invalid username or password')  

    # แสดงฟอร์มล็อคอินถ้าไม่มีการ POST
    return render(request, 'login.html')
