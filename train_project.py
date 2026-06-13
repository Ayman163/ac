import os
from roboflow import Roboflow
from ultralytics import YOLO

def main():
    print("--- 1. بدء تحميل البيانات من Roboflow ---")
    # تم وضع مفتاح الـ API والبيانات الخاصة بمشروعك بناءً على ملف الـ Notebook الخاص بك
    rf = Roboflow(api_key="bXgZ0bX66gXlZ8XgXgXg") # تم حجب الجزء الحقيقي للأمان
    project = rf.workspace("accident-detection-vby8i").project("traffic-accidents-severity")
    
    # تحميل البيانات بصيغة متوافقة مع YOLOv11 أو YOLOv10
    dataset = version = project.version(1).download("yolov11")
    
    # تحديد مسار ملف data.yaml التلقائي الذي ينزل من roboflow
    yaml_path = os.path.join(dataset.location, "data.yaml")
    print(f"تم تحميل البيانات بنجاح في المسار: {dataset.location}")

    print("--- 2. تهيئة موديل YOLO للتدريب ---")
    # يمكنك كتابة 'yolov10x.pt' أو 'yolo11x.pt' حسب الموديل النهائي الذي استقريت عليه
    model = YOLO("yolo11s.pt") 

    print("--- 3. انطلاق عملية التدريب على كروت الـ GPU ---")
    # الإعدادات مخصصة لتوزيع الحمل على كروت الشاشة في السيرفر الجديد
    results = model.train(
        data=yaml_path,
        epochs=100,             # عدد دورات التدريب
        imgsz=640,              # حجم الصور
        batch=128,              # رفعنا الـ Batch لأن كروت السيرفر قوية وتتحمل
        device="0,1,2,3,4,5,6,7,8,9", # استخدام جميع الـ 10 كروت المتاحة في السيرفر المعروض
        workers=8,              # تسريع قراءة المعالج للصور من الهارد ديسك
        project="accident_detection",
        name="yolo_heavy_run",
        save=True               # حفظ الـ Checkpoints تلقائياً لحماية التقدم
    )
    print("--- تم اكتمال التدريب بنجاح! ---")

if __name__ == "__main__":
    main()